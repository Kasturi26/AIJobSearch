import streamlit as st
from tools.helper import extract_text_from_pdf, ask_openai
from tools.job_api import fetch_linkedin_jobs, fetch_naukri_jobs

st.set_page_config(page_title="Job Recommender", page_icon="💼", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
        /* Main container */
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Header styling */
        .header-title {
            font-size: 3em;
            font-weight: bold;
            color: #667eea;
            text-align: center;
            margin-bottom: 0.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .header-subtitle {
            font-size: 1.1em;
            color: #555;
            text-align: center;
            margin-bottom: 2em;
            line-height: 1.6;
        }
        
        /* Card styling */
        .card {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.15);
            border-left: 5px solid #667eea;
            margin: 15px 0;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 35px rgba(102, 126, 234, 0.25);
        }
        
        .card-title {
            font-size: 1.5em;
            font-weight: 600;
            color: #667eea;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .card-content {
            font-size: 1em;
            color: #333;
            line-height: 1.8;
        }
        
        /* Button styling */
        .stButton>button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 12px 30px;
            font-weight: 600;
            font-size: 1.05em;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.6);
        }
        
        /* File uploader styling */
        .uploadedFile {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 10px;
            padding: 20px;
        }
        
        /* Badge styling */
        .badge {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 600;
            margin: 5px 5px 5px 0;
        }
        
        .job-card {
            background: white;
            padding: 20px;
            margin: 10px 0;
            border-radius: 12px;
            border-left: 4px solid #667eea;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
        }
        
        .job-card:hover {
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.2);
            transform: translateX(5px);
        }
        
        .job-title {
            font-size: 1.2em;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 8px;
        }
        
        .job-company {
            font-size: 1.05em;
            font-weight: 600;
            color: #764ba2;
            margin-bottom: 8px;
        }
        
        .job-meta {
            color: #777;
            font-size: 0.95em;
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }
        
        .section-divider {
            height: 3px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            border-radius: 2px;
            margin: 30px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="header-title">💼 AI Job Recommender System</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="header-subtitle">
    🚀 Powered by AI | Find your dream job based on your skills<br>
    <small>Upload your resume and get personalized job recommendations from top job portals</small>
    </div>
""", unsafe_allow_html=True)

# File Upload Section
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("### 📄 Upload Your Resume")
    uploaded_file = st.file_uploader("Select a PDF file", type=["pdf"], help="Upload your resume in PDF format")

if uploaded_file:
    # Progress indicators
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Step 1: Extract Text
    status_text.text("📊 Step 1/4: Extracting resume text...")
    with st.spinner("🔄 Processing..."):
        resume_text = extract_text_from_pdf(uploaded_file)
    progress_bar.progress(25)
    
    # Step 2: Summarize
    status_text.text("📊 Step 2/4: Analyzing and summarizing...")
    with st.spinner("🔄 Processing..."):
        summary = ask_openai(f"Summarize the following resume highlighting the skills, education and experience in a few sentences:\n\n{resume_text}", max_tokens=80)
    progress_bar.progress(50)
    
    # Step 3: Skill Gaps
    status_text.text("📊 Step 3/4: Identifying skill gaps...")
    with st.spinner("🔄 Processing..."):
        skill_gaps = ask_openai(f"Analyze this resume and highlight missing skills, certification and experiences needed for better job opportunities:\n\n{resume_text}", max_tokens=80)
    progress_bar.progress(75)
    
    # Step 4: Roadmap
    status_text.text("📊 Step 4/4: Creating career roadmap...")
    with st.spinner("🔄 Processing..."):
        future_roadmap = ask_openai(f"Based on the following resume suggest a future roadmap for career development(skill to learn, certifications needed):\n\n{resume_text}", max_tokens=80)
    progress_bar.progress(100)
    
    # Clear progress indicators
    status_text.empty()
    progress_bar.empty()
    
    # Success notification
    st.markdown("""
        <div style='background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%); 
                    padding: 15px 20px; 
                    border-radius: 10px; 
                    margin: 20px 0;
                    border-left: 5px solid #2ecc71;'>
            <h4 style='color: #27ae60; margin: 0;'>✅ Analysis Complete!</h4>
            <p style='color: #27ae60; margin: 5px 0 0 0;'>Your resume has been successfully analyzed.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Display Results in Cards
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("## 📈 Your Resume Analysis")
    
    # Resume Summary Card
    st.markdown(f"""
        <div class="card">
            <div class="card-title">👤 Resume Summary</div>
            <div class="card-content">{summary}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Skill Gaps Card
    st.markdown(f"""
        <div class="card">
            <div class="card-title">🎯 Skill Gaps & Missing Areas</div>
            <div class="card-content">{skill_gaps}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Career Roadmap Card
    st.markdown(f"""
        <div class="card">
            <div class="card-title">🗺️ Career Roadmap & Preparation</div>
            <div class="card-content">{future_roadmap}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Get Job Recommendations
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔍 Get Job Recommendations", use_container_width=True):
            with st.spinner("⏳ Extracting job keywords..."):
                keywords = ask_openai(f"Based on this resume summary, suggest the best job titles and keywords for a searching jobs. Give a comma-separated list only no explanations:\n\n{summary}",
                max_tokens=30)
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
                    st.markdown(f"Experience Required: {job.get('experience')}")
                    st.markdown(f"Salary: {job.get('salary')}")
                    st.markdown(f"[Apply Here]({job.get('url')})")
                    st.markdown("-----")
            else:
                st.markdown("No job listings found.")
        
        

        
