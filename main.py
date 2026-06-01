import streamlit as st
from tools.helper import extract_text_from_pdf, ask_openai, analyze_resume_comprehensive
from tools.job_api import fetch_linkedin_jobs, fetch_naukri_jobs
from styles import DARK_THEME_STYLES
from ui_icons import icon, stat_card, feature_card, process_step, upload_hero_header
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

st.set_page_config(
    page_title="AI Job Recommender | UniConnect",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Clear any cached data to ensure fresh load
st.cache_data.clear()

# Load styling from styles.py
st.markdown(DARK_THEME_STYLES, unsafe_allow_html=True)

# Header Section
st.markdown(f"""
    <div class="hero-wrap">
        <div class="hero-badge" style="display:inline-flex;align-items:center;gap:8px;">
            <span style="display:inline-flex;color:#2563eb;">{icon("sparkles", 16, "#2563eb")}</span>
            AI-Powered Career Intelligence
        </div>
        <div class="header-title">Find Your <span class="highlight-text">Dream Role</span> — Faster</div>
        <div class="header-subtitle">
            Upload your resume for instant ATS analysis, skill insights, and curated job matches — built for candidates and hiring teams.
        </div>
    </div>
""", unsafe_allow_html=True)

stat_c1, stat_c2, stat_c3 = st.columns(3)
with stat_c1:
    st.markdown(stat_card("checklist", "#dbeafe", "#2563eb", "4 Steps", "Full analysis flow"), unsafe_allow_html=True)
with stat_c2:
    st.markdown(stat_card("robot", "#cffafe", "#0891b2", "AI Scoring", "ATS resume review"), unsafe_allow_html=True)
with stat_c3:
    st.markdown(stat_card("briefcase", "#d1fae5", "#059669", "60+ Jobs", "Matched listings"), unsafe_allow_html=True)

# Feature Boxes Section
feature_col1, feature_col2, feature_col3 = st.columns(3)
with feature_col1:
    st.markdown(feature_card("target", "#dbeafe", "#2563eb", "Smart Matching", "Roles aligned to your skills & experience"), unsafe_allow_html=True)
with feature_col2:
    st.markdown(feature_card("chart", "#ede9fe", "#7c3aed", "ATS Insights", "Professional, recruiter-ready analysis"), unsafe_allow_html=True)
with feature_col3:
    st.markdown(feature_card("bolt", "#fef3c7", "#d97706", "Instant Results", "Summary, gaps & jobs in minutes"), unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# How it works — visual journey (not a text list)
st.markdown(f"""
    <div style="text-align:center;margin-bottom:1.5rem;">
        <div class="section-label" style="display:inline-flex;align-items:center;gap:6px;">
            <span style="display:inline-flex;color:#2563eb;">{icon("insights", 14, "#2563eb")}</span> YOUR JOURNEY
        </div>
        <div class="section-heading">From resume to offer-ready insights</div>
        <p style="color:#64748b;font-size:0.95rem;max-width:520px;margin:0 auto;">
            A guided pipeline — each step builds on the last until you see matched roles.
        </p>
    </div>
    <div style="margin:0 6% 1.25rem;height:4px;border-radius:4px;
        background:linear-gradient(90deg,#2563eb 0%,#06b6d4 33%,#7c3aed 66%,#059669 100%);opacity:0.85;"></div>
""", unsafe_allow_html=True)

step_c1, step_c2, step_c3, step_c4 = st.columns(4)
with step_c1:
    st.markdown(process_step(1, "upload", "Upload PDF", "Drop your latest resume", "#2563eb"), unsafe_allow_html=True)
with step_c2:
    st.markdown(process_step(2, "cpu", "AI Analysis", "ATS scan & skill mapping", "#0891b2"), unsafe_allow_html=True)
with step_c3:
    st.markdown(process_step(3, "insights", "Review Insights", "Summary & gap tips", "#7c3aed"), unsafe_allow_html=True)
with step_c4:
    st.markdown(process_step(4, "jobs", "Get Jobs", "Naukri matches for you", "#059669"), unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown(f"""
    <div class="upload-section-title">
        <div class="section-label" style="display:inline-flex;align-items:center;justify-content:center;gap:6px;">
            <span style="display:inline-flex;color:#2563eb;">{icon("upload", 14, "#2563eb")}</span> GET STARTED
        </div>
        <div class="section-heading" style="display:flex;align-items:center;justify-content:center;gap:8px;margin-top:0.25rem;">
            <span style="display:inline-flex;color:#2563eb;">{icon("pdf", 22, "#2563eb")}</span> Upload your resume
        </div>
        <p style="color:#64748b;font-size:0.92rem;margin:0.5rem auto 0;max-width:420px;">
            One file starts your full career analysis — takes less than a minute.
        </p>
    </div>
""", unsafe_allow_html=True)

_u_left, _u_center, _u_right = st.columns([1, 2, 1])
with _u_center:
    st.markdown(
        f'<div class="upload-hero-card">{upload_hero_header()}</div>',
        unsafe_allow_html=True,
    )
    uploaded_file = st.file_uploader(
        "Resume (PDF)",
        type=["pdf"],
        label_visibility="collapsed",
        help="Upload your resume in PDF format",
    )

st.markdown(f"""
    <p class="upload-footer-note">
        {icon("shield", 12, "#94a3b8")}
        Max 200 MB · PDF format · Processed securely in your session only
    </p>
""", unsafe_allow_html=True)

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
    st.markdown(f"""
        <div class='success-notification'>
            <div class="success-notification-icon" style="color:#059669;">{icon("check", 22, "#059669")}</div>
            <div>
                <h4 style="display:flex;align-items:center;gap:8px;">{icon("sparkles", 18, "#047857")} Analysis complete</h4>
                <p>Your resume has been processed. Review the insights below.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Display Results in Cards
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="results-header">
            <div>
                <div class="section-label" style="display:flex;align-items:center;gap:6px;"><span style="display:inline-flex;">{icon("chart", 14, "#2563eb")}</span> Insights</div>
                <div class="section-heading" style="margin:0;display:flex;align-items:center;gap:8px;"><span style="display:inline-flex;">{icon("user", 20, "#2563eb")}</span> Your resume analysis</div>
            </div>
            <div class="results-header-bar"></div>
        </div>
    """, unsafe_allow_html=True)
    
    # Format content for better display
    formatted_analysis = format_content_as_html(analysis_result)
    formatted_summary = format_content_as_html(summary)
    formatted_gaps = format_content_as_html(skill_gaps)
    
    # Full Analysis Card
    st.markdown(f"""
        <div class="card">
            <div class="card-title"><span class="card-title-icon">{icon("search", 18, "#2563eb")}</span> ATS Resume Analysis</div>
            <div class="card-content">{formatted_analysis if formatted_analysis else 'Analyzing...'}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Resume Summary Card
    st.markdown(f"""
        <div class="card">
            <div class="card-title"><span class="card-title-icon">{icon("user", 18, "#2563eb")}</span> Professional Summary</div>
            <div class="card-content">{formatted_summary if formatted_summary else 'Summarizing...'}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Skill Gaps Card
    st.markdown(f"""
        <div class="card">
            <div class="card-title"><span class="card-title-icon">{icon("trend", 18, "#2563eb")}</span> Skill Gaps & Recommendations</div>
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
            st.markdown(f"""
                <div class="section-label" style="display:flex;align-items:center;gap:6px;"><span style="display:inline-flex;">{icon("tag", 14, "#2563eb")}</span> Matching</div>
                <div class="section-heading" style="margin-top:0;display:flex;align-items:center;gap:8px;"><span style="display:inline-flex;">{icon("briefcase", 20, "#2563eb")}</span> Recommended job titles</div>
            """, unsafe_allow_html=True)
            keyword_list = [kw.strip() for kw in search_keywords_clean.split(",")]
            badges_html = "".join([
                f'<span class="badge" style="display:inline-flex;align-items:center;gap:6px;">{icon("briefcase", 12, "#1d4ed8")} {kw}</span>'
                for kw in keyword_list
            ])
            st.markdown(f'<div class="keywords-wrap">{badges_html}</div>', unsafe_allow_html=True)
            
            with st.spinner("⏳ Fetching job listings..."):
                naukri_jobs = fetch_naukri_jobs(search_keywords_clean, location="india", rows=60)
            
            if naukri_jobs:
                st.markdown(f"""
                    <div class="section-label" style="display:flex;align-items:center;gap:6px;"><span style="display:inline-flex;">{icon("star", 14, "#2563eb")}</span> Opportunities</div>
                    <div class="section-heading" style="margin-top:0;display:flex;align-items:center;gap:8px;"><span style="display:inline-flex;">{icon("briefcase", 20, "#2563eb")}</span> Top matches from Naukri</div>
                """, unsafe_allow_html=True)
                st.markdown(
                    f'<p style="color:#64748b;font-size:0.9rem;margin:0 0 1rem;"><strong>{len(naukri_jobs)}</strong> roles found matching your profile</p>',
                    unsafe_allow_html=True,
                )
                st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
                
                for idx, job in enumerate(naukri_jobs[:15], 1):  # Display top 15 jobs
                    job_title = job.get('title', 'N/A')
                    company_name = job.get('companyName', 'N/A')
                    location = job.get('location', 'N/A')
                    salary = job.get('salary', 'Not specified')
                    experience = job.get('experience', 'N/A')
                    
                    st.markdown(f"""
                        <div class="job-card">
                            <div style='display: flex; justify-content: space-between; align-items: flex-start; gap: 12px;'>
                                <div>
                                    <div class="job-title">{idx}. {job_title}</div>
                                    <div class="job-company" style="display:flex;align-items:center;gap:6px;"><span style="display:inline-flex;">{icon("building", 14, "#64748b")}</span> {company_name}</div>
                                </div>
                                <div class="job-salary-pill">{salary}</div>
                            </div>
                            <div class="job-meta">
                                <span style="display:inline-flex;align-items:center;gap:4px;">{icon("pin", 14, "#64748b")} {location}</span>
                                <span style="display:inline-flex;align-items:center;gap:4px;">{icon("clock", 14, "#64748b")} {experience}</span>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("⚠️ No jobs found for your keywords. Try different search terms.")

# Bottom Features Section
ft1, ft2, ft3, ft4 = st.columns(4)
_footer_items = [
    ("robot", "#dbeafe", "#2563eb", "AI-Powered Analysis", "Enterprise-grade resume intelligence"),
    ("briefcase", "#ede9fe", "#7c3aed", "Curated Matches", "Roles from leading job boards"),
    ("star", "#fef3c7", "#d97706", "Personalized", "Tailored to each candidate profile"),
    ("chart", "#d1fae5", "#059669", "Actionable Insights", "Clear gaps and next-step guidance"),
]
for col, (ic, bg, clr, title, desc) in zip([ft1, ft2, ft3, ft4], _footer_items):
    with col:
        st.markdown(f"""
            <div style="background:#fff;border:1px solid #e2e8f0;border-radius:14px;padding:1.25rem;
                text-align:center;box-shadow:0 4px 16px rgba(15,23,42,0.05);">
                <div style="width:48px;height:48px;margin:0 auto 0.6rem;border-radius:12px;background:{bg};
                    display:flex;align-items:center;justify-content:center;color:{clr};">
                    {icon(ic, 24, clr)}
                </div>
                <div style="font-weight:700;color:#0f172a;font-size:0.88rem;">{title}</div>
                <div style="color:#64748b;font-size:0.78rem;margin-top:0.3rem;line-height:1.4;">{desc}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown(f"""
    <div class="app-footer" style="display:flex;align-items:center;justify-content:center;gap:8px;">
        <span style="display:inline-flex;color:#2563eb;">{icon("briefcase", 16, "#2563eb")}</span>
        <strong>AI Job Recommender</strong> · Built for modern hiring workflows
    </div>
""", unsafe_allow_html=True)

        
