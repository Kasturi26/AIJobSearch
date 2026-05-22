# Central styling file for the Job Recommender application

DARK_THEME_STYLES = """
    <style>
        /* Main container - Dark theme */
        .main {
            background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
            color: #e0e0e0;
        }
        
        /* Header styling */
        .header-title {
            font-size: 3.2em;
            font-weight: 900;
            color: #000000;
            text-align: center;
            margin-bottom: 0.8em;
            line-height: 1.2;
            text-shadow: 0 2px 10px rgba(102, 126, 234, 0.3);
        }
        
        .highlight-text {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 900;
        }
        
        .header-subtitle {
            font-size: 1.3em;
            color: #000000;
            text-align: center;
            margin-bottom: 1.2em;
            line-height: 1.6;
            padding: 0 20px;
            font-weight: 500;
        }
        
        /* Main content wrapper */
        .stContainer {
            padding: 5px !important;
        }
        
        /* Column spacing */
        [data-testid="column"] {
            padding: 10px !important;
        }
        
        /* Feature boxes styling */
        .feature-box {
            background: linear-gradient(135deg, #252d3d 0%, #2d3a4f 100%);
            padding: 15px 12px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(102, 126, 234, 0.15);
            border: 2px solid #667eea;
            transition: all 0.3s ease;
            min-height: 60px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        
        .feature-box:hover {
            box-shadow: 0 12px 48px rgba(102, 126, 234, 0.3);
            transform: translateY(-8px);
            border-color: #764ba2;
        }
        
        .feature-icon {
            font-size: 2.2em;
            margin-bottom: 5px;
            display: block;
            opacity: 1;
        }
        
        .feature-title {
            font-size: 0.95em;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 4px;
            display: block;
            opacity: 1;
        }
        
        .feature-desc {
            font-size: 0.9em;
            color: #b0b8c1;
            display: block;
            opacity: 1;
        }
        
        /* Card styling */
        .card {
            background: linear-gradient(135deg, #1e2635 0%, #252d3d 100%);
            padding: 18px;
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(102, 126, 234, 0.2);
            border: 2px solid #667eea;
            margin: 14px 0;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 50px rgba(102, 126, 234, 0.35);
            border-color: #764ba2;
        }
        
        .card-title {
            font-size: 1.4em;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .card-content {
            font-size: 0.95em;
            color: #e0e0e0;
            line-height: 1.6;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }
        
        .card-content h4, .card-content h5 {
            color: #667eea;
            margin-top: 12px;
            margin-bottom: 8px;
            font-weight: 600;
            font-size: 0.98em;
        }
        
        .card-content h4:first-child, .card-content h5:first-child {
            margin-top: 0;
        }
        
        .card-content ul, .card-content ol {
            margin: 8px 0 8px 20px;
            padding: 0;
        }
        
        .card-content li {
            margin: 5px 0;
            padding-left: 8px;
            color: #e0e0e0;
        }
        
        .card-content li strong {
            color: #667eea;
            font-weight: 600;
        }
        
        .card-content .section-item {
            background: rgba(102, 126, 234, 0.05);
            padding: 10px 12px;
            margin: 8px 0;
            border-left: 3px solid #667eea;
            border-radius: 4px;
        }
        
        .card-content .section-item strong {
            color: #667eea;
        }
        
        .card-content p {
            margin: 8px 0;
            padding: 0;
        }
        
        .card-content br {
            display: none;
        }
        
        /* Button styling */
        .stButton>button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: black;
            border: none;
            border-radius: 25px;
            padding: 12px 30px;
            font-weight: 900;
            font-size: 1.05em;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 40px rgba(102, 126, 234, 0.8);
        }
        
        /* File uploader styling */
        .uploadedFile {
            background: linear-gradient(135deg, #1e2635 0%, #252d3d 100%);
            border-radius: 10px;
            padding: 20px;
            border: 2px solid #667eea;
        }
        
        .upload-section {
            background: linear-gradient(135deg, #1e2635 0%, #252d3d 100%);
            padding: 30px 25px;
            border-radius: 12px;
            border: 3px dashed #667eea;
            text-align: center;
            margin: 10px 0;
            transition: all 0.3s ease;
        }
        
        .upload-section:hover {
            border-color: #764ba2;
            box-shadow: 0 12px 40px rgba(102, 126, 234, 0.25);
        }
        
        .upload-icon {
            font-size: 3.5em;
            margin: 15px 0 20px 0;
        }
        
        .upload-text {
            color: #667eea;
            font-size: 1.05em;
            font-weight: 600;
            margin-bottom: 8px;
        }
        
        .upload-subtext {
            color: #8892a0;
            font-size: 0.9em;
            margin-bottom: 0;
        }
        
        /* Badge styling */
        .badge {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 600;
            margin: 5px 5px 5px 0;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        
        .job-card {
            background: linear-gradient(135deg, #1e2635 0%, #252d3d 100%);
            padding: 20px;
            margin: 10px 0;
            border-radius: 12px;
            border: 2px solid #667eea;
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.15);
            transition: all 0.3s ease;
        }
        
        .job-card:hover {
            box-shadow: 0 10px 35px rgba(102, 126, 234, 0.3);
            transform: translateX(8px);
            border-color: #764ba2;
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
            color: #8892a0;
            font-size: 0.95em;
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }
        
        .section-divider {
            height: 3px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            border-radius: 2px;
            margin: 15px 0;
            box-shadow: 0 0 20px rgba(102, 126, 234, 0.3);
        }
        
        /* Bottom features section */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 25px;
            margin-top: 50px;
            padding-top: 40px;
            border-top: 2px solid #667eea;
        }
        
        .bottom-feature {
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #1e2635 0%, #252d3d 100%);
            border-radius: 12px;
            border: 1px solid #667eea;
            transition: all 0.3s ease;
        }
        
        .bottom-feature:hover {
            border-color: #764ba2;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.25);
            transform: translateY(-5px);
        }
        
        .bottom-feature-icon {
            font-size: 2em;
            margin-bottom: 10px;
        }
        
        .bottom-feature-title {
            font-weight: 600;
            color: #ffffff;
            font-size: 0.95em;
        }
        
        .bottom-feature-desc {
            color: #8892a0;
            font-size: 0.85em;
            margin-top: 5px;
        }
        
        /* Success notification */
        .success-notification {
            background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
            padding: 15px 20px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 5px solid #2ecc71;
        }
        
        .success-notification h4 {
            color: #27ae60;
            margin: 0;
        }
        
        .success-notification p {
            color: #27ae60;
            margin: 5px 0 0 0;
        }
    </style>
"""
