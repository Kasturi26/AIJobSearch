import streamlit as st
from tools.helper import extract_text_from_pdf, ask_openai, analyze_resume_comprehensive
from tools.job_api import fetch_linkedin_jobs, fetch_naukri_jobs
from styles import DARK_THEME_STYLES
import re

def format_content_as_html(content):
    """Convert text content with numbered sections into formatted HTML"""
    if not content:
        return content
    
    # Split by numbered sections
    lines = content.split('\n')
    html_content = []
    in_list = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        # Check for main numbered section (e.g., "*1. Section Title*")
        if re.match(r'^\*+\d+\.', stripped):
            if in_list:
                html_content.append('</ul>')
                in_list = False
            # Format as h4 header
            title = re.sub(r'^\*+|\*+$', '', stripped)
            html_content.append(f'<h4>{title}</h4>')
        
        # Check for table-like items with pipe separators (e.g., "| Item | Content |")
        elif '|' in stripped and stripped.count('|') >= 2:
            item_parts = [p.strip() for p in stripped.split('|') if p.strip()]
            if len(item_parts) >= 2:
                if in_list:
                    html_content.append('</ul>')
                    in_list = False
                # Format as section item with left border
                html_content.append(f'<div class="section-item"><strong>{item_parts[0]}</strong><br>{" | ".join(item_parts[1:])}</div>')
            else:
                # Regular line
                if not in_list:
                    html_content.append('<ul>')
                    in_list = True
                html_content.append(f'<li>{stripped}</li>')
        
        # Check for bullet or list items (starting with ** or -)
        elif stripped.startswith('**') or stripped.startswith('-') or stripped.startswith('*'):
            if not in_list:
                html_content.append('<ul>')
                in_list = True
            clean_line = re.sub(r'^[\*\-\s]+', '', stripped)
            html_content.append(f'<li>{clean_line}</li>')
        
        # Regular content
        else:
            if in_list:
                html_content.append('</ul>')
                in_list = False
            html_content.append(f'<p>{stripped}</p>')
    
    # Close list if still open
    if in_list:
        html_content.append('</ul>')
    
    return '\n'.join(html_content)

st.set_page_config(page_title="Job Recommender", page_icon="💼", layout="wide")

# Clear any cached data to ensure fresh load
st.cache_data.clear()

# Load styling from styles.py
st.markdown(DARK_THEME_STYLES, unsafe_allow_html=True)

# Header Section
st.markdown('<div class="header-title">Find Your <span class="highlight-text">Dream Job</span><br>with AI</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="header-subtitle">
    Upload your resume, get AI analysis of your skills, experiences, and credentials to recommend jobs that are perfect for you.
    </div>
""", unsafe_allow_html=True)

# Feature Boxes Section
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

feature_col1, feature_col2, feature_col3 = st.columns(3)
with feature_col1:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Smart Matching</div>
            <div class="feature-desc">Intelligent matching with jobs</div>
        </div>
    """, unsafe_allow_html=True)

with feature_col2:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📊</div>
            <div class="feature-title">NLP Scores</div>
            <div class="feature-desc">Advanced text analysis</div>
        </div>
    """, unsafe_allow_html=True)

with feature_col3:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Instant Results</div>
            <div class="feature-desc">Get recommendations instantly</div>
        </div>
    """, unsafe_allow_html=True)

# File Upload Section
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("### 📄 Upload Your Resume")

upload_col1, upload_col2, upload_col3 = st.columns([0.5, 2, 0.5])
with upload_col2:
    st.markdown("""
        <div class="upload-section">
            <div class="upload-icon">📤</div>
            <div class="upload-text">Drag & drop your resume here</div>
            <div class="upload-subtext">or click to browse files</div>
        </div>
    """, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed", help="Upload your resume in PDF format")

if uploaded_file:
    # Progress indicators
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Step 1: Extract Text
    status_text.text("📊 Step 1/4: Extracting resume text...")
    with st.spinner("🔄 Processing..."):
        resume_text = extract_text_from_pdf(uploaded_file)
    progress_bar.progress(25)
    
    # Step 2: Comprehensive Analysis
    status_text.text("📊 Step 2/4: Analyzing resume with ATS Analyzer...")
    with st.spinner("🔄 Processing..."):
        analysis_result = analyze_resume_comprehensive(resume_text)
    progress_bar.progress(50)
    
    # Step 3: Extract Summary
    status_text.text("📊 Step 3/4: Extracting professional summary...")
    with st.spinner("🔄 Processing..."):
        summary = ask_openai(f"Provide a brief professional summary of this person based on the resume:\n\n{resume_text}\n\nSummary (2-3 sentences):", max_tokens=500)
    progress_bar.progress(75)
    
    # Step 4: Extract Skill Gaps
    status_text.text("📊 Step 4/4: Identifying skill gaps...")
    with st.spinner("🔄 Processing..."):
        skill_gaps = ask_openai(f"Based on this resume, what are the key skill gaps and areas for improvement? List them with explanations:\n\n{resume_text}\n\nSkill gaps and recommendations:", max_tokens=500)
    progress_bar.progress(100)
    
    # Ensure responses are not empty
    if not analysis_result or analysis_result.strip() == "":
        analysis_result = "Analysis is being processed. Please try again."
    if not summary or summary.strip() == "":
        summary = "Unable to extract summary at this time. Please ensure your resume is properly formatted."
    if not skill_gaps or skill_gaps.strip() == "":
        skill_gaps = "Unable to identify skill gaps at this time. Please try again."
    
    # Normalize whitespace - replace multiple newlines with single newline
    analysis_result = '\n'.join(line.rstrip() for line in analysis_result.split('\n') if line.strip())
    summary = '\n'.join(line.rstrip() for line in summary.split('\n') if line.strip())
    skill_gaps = '\n'.join(line.rstrip() for line in skill_gaps.split('\n') if line.strip())
    
    # Clear progress indicators
    status_text.empty()
    progress_bar.empty()
    
    # Success notification
    st.markdown("""
        <div class='success-notification'>
            <h4>✅ Analysis Complete!</h4>
            <p>Your resume has been successfully analyzed.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Display Results in Cards
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("## 📈 Your Resume Analysis")
    
    # Format content for better display
    formatted_analysis = format_content_as_html(analysis_result)
    formatted_summary = format_content_as_html(summary)
    formatted_gaps = format_content_as_html(skill_gaps)
    
    # Full Analysis Card
    st.markdown(f"""
        <div class="card">
            <div class="card-title">🔍 ATS Resume Analysis</div>
            <div class="card-content">{formatted_analysis if formatted_analysis else 'Analyzing...'}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Resume Summary Card
    st.markdown(f"""
        <div class="card">
            <div class="card-title">👤 Professional Summary</div>
            <div class="card-content">{formatted_summary if formatted_summary else 'Summarizing...'}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Skill Gaps Card
    st.markdown(f"""
        <div class="card">
            <div class="card-title">🎯 Skill Gaps & Missing Areas</div>
            <div class="card-content">{formatted_gaps if formatted_gaps else 'Identifying gaps...'}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Get Job Recommendations
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Analyze Resume & Find Jobs", use_container_width=True):
            with st.spinner("⏳ Extracting job keywords..."):
                keywords = ask_openai(f"Based on this resume, what are the top 5-7 job titles that would be a good fit? Return only the job titles as a comma-separated list, nothing else:\n\n{resume_text}",
                max_tokens=150)
                search_keywords_clean = keywords.replace("\n", "").strip()
            
            # Display keywords as badges
            st.markdown("### 🏷️ Job Keywords Found:")
            keyword_list = [kw.strip() for kw in search_keywords_clean.split(",")]
            badges_html = "".join([f'<span class="badge">{kw}</span>' for kw in keyword_list])
            st.markdown(f'<div style="margin: 15px 0;">{badges_html}</div>', unsafe_allow_html=True)
            
            with st.spinner("⏳ Fetching job listings..."):
                naukri_jobs = fetch_naukri_jobs(search_keywords_clean, location="india", rows=60)
            
            if naukri_jobs:
                st.markdown('### 💼 Top Job Recommendations from Naukri')
                st.markdown(f"<small>Found **{len(naukri_jobs)} job opportunities** matching your profile</small>", unsafe_allow_html=True)
                st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
                
                for idx, job in enumerate(naukri_jobs[:15], 1):  # Display top 15 jobs
                    job_title = job.get('title', 'N/A')
                    company_name = job.get('companyName', 'N/A')
                    location = job.get('location', 'N/A')
                    salary = job.get('salary', 'Not specified')
                    experience = job.get('experience', 'N/A')
                    
                    st.markdown(f"""
                        <div class="job-card">
                            <div style='display: flex; justify-content: space-between; align-items: start;'>
                                <div>
                                    <div class="job-title">#{idx} {job_title}</div>
                                    <div class="job-company">🏢 {company_name}</div>
                                </div>
                                <div style='background: #667eea; color: white; padding: 8px 15px; border-radius: 20px; font-size: 0.9em;'>
                                    {salary}
                                </div>
                            </div>
                            <div class="job-meta">
                                <span>📍 {location}</span>
                                <span>📊 {experience}</span>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("⚠️ No jobs found for your keywords. Try different search terms.")

# Bottom Features Section
st.markdown("""
    <div class="features-grid">
        <div class="bottom-feature">
            <div class="bottom-feature-icon">🤖</div>
            <div class="bottom-feature-title">AI Powered Analysis</div>
            <div class="bottom-feature-desc">Advanced resume analysis with AI</div>
        </div>
        <div class="bottom-feature">
            <div class="bottom-feature-icon">💼</div>
            <div class="bottom-feature-title">Top Job Matches</div>
            <div class="bottom-feature-desc">Best curated job listings</div>
        </div>
        <div class="bottom-feature">
            <div class="bottom-feature-icon">⭐</div>
            <div class="bottom-feature-title">Personalized Results</div>
            <div class="bottom-feature-desc">Recommendations tailored for you</div>
        </div>
        <div class="bottom-feature">
            <div class="bottom-feature-icon">🔔</div>
            <div class="bottom-feature-title">Job Alerts</div>
            <div class="bottom-feature-desc">Stay updated with new openings</div>
        </div>
    </div>
""", unsafe_allow_html=True)

        
