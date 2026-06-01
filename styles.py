# Light professional theme — forces light UI over Streamlit defaults

DARK_THEME_STYLES = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=DM+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
    /* Force light theme — overrides Streamlit dark mode */
    :root {
        --bg: #f0f4f8;
        --surface: #ffffff;
        --text: #0f172a;
        --text-secondary: #475569;
        --text-muted: #64748b;
        --primary: #2563eb;
        --primary-light: #dbeafe;
        --accent: #0891b2;
        --accent-light: #cffafe;
        --success: #059669;
        --border: #e2e8f0;
        --shadow: 0 4px 20px rgba(15, 23, 42, 0.06);
        --radius: 14px;
    }

    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"] > section.main,
    .main .block-container {
        background-color: #f0f4f8 !important;
        color: #0f172a !important;
        font-family: 'Inter', 'DM Sans', system-ui, sans-serif !important;
    }

    [data-testid="stHeader"] {
        background: #ffffff !important;
        border-bottom: 1px solid #e2e8f0 !important;
    }

    #MainMenu, footer { visibility: hidden; height: 0; }

    h1, h2, h3, h4, h5, h6, p, label, span, div, li,
    [data-testid="stMarkdownContainer"] {
        font-family: 'Inter', 'DM Sans', system-ui, sans-serif !important;
    }

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li {
        color: #334155 !important;
    }

    .main .block-container {
        padding-top: 1.5rem !important;
        max-width: 1100px !important;
    }

    /* ── Hero ── */
    .hero-wrap {
        text-align: center;
        padding: 2rem 1rem 1.5rem;
        background: linear-gradient(180deg, #ffffff 0%, #f0f4f8 100%);
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: var(--shadow);
        margin-bottom: 1.5rem;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        color: #1d4ed8;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        padding: 8px 16px;
        border-radius: 999px;
        margin-bottom: 1rem;
    }

    .hero-badge i { color: #2563eb; }

    .header-title {
        font-family: 'DM Sans', 'Inter', sans-serif !important;
        font-size: clamp(1.85rem, 4.5vw, 2.75rem) !important;
        font-weight: 800 !important;
        color: #0f172a !important;
        line-height: 1.2 !important;
        margin: 0 0 0.75rem !important;
        letter-spacing: -0.03em;
    }

    .highlight-text {
        color: #2563eb !important;
        background: linear-gradient(135deg, #2563eb, #0891b2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .header-subtitle {
        font-size: 1.05rem !important;
        color: #475569 !important;
        max-width: 580px;
        margin: 0 auto !important;
        line-height: 1.65 !important;
        font-weight: 400 !important;
    }

    .hero-stats {
        display: flex !important;
        flex-direction: row !important;
        justify-content: center !important;
        flex-wrap: wrap !important;
        gap: 1rem !important;
        margin-top: 1.75rem !important;
        padding-top: 1.5rem !important;
        border-top: 1px solid #e2e8f0 !important;
    }

    .hero-stat {
        display: flex !important;
        align-items: center !important;
        gap: 12px !important;
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        padding: 12px 20px !important;
        min-width: 160px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .hero-stat-icon {
        width: 44px;
        height: 44px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.15rem;
        flex-shrink: 0;
    }

    .hero-stat-icon.blue { background: #dbeafe; color: #2563eb; }
    .hero-stat-icon.teal { background: #cffafe; color: #0891b2; }
    .hero-stat-icon.green { background: #d1fae5; color: #059669; }

    .hero-stat-text strong {
        display: block;
        font-size: 1.1rem;
        font-weight: 800;
        color: #0f172a !important;
        line-height: 1.2;
    }

    .hero-stat-text span {
        font-size: 0.72rem;
        font-weight: 600;
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    /* ── Feature cards ── */
    .feature-box {
        background: #ffffff !important;
        padding: 1.5rem 1.25rem !important;
        border-radius: var(--radius) !important;
        text-align: center !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: var(--shadow) !important;
        min-height: 160px;
        transition: transform 0.2s, box-shadow 0.2s;
    }

    .feature-box:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(37, 99, 235, 0.12) !important;
        border-color: #93c5fd !important;
    }

    .feature-icon-wrap {
        width: 56px;
        height: 56px;
        border-radius: 14px;
        margin: 0 auto 0.85rem;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.4rem;
    }

    .feature-icon-wrap.ic-blue { background: #dbeafe; color: #2563eb; }
    .feature-icon-wrap.ic-purple { background: #ede9fe; color: #7c3aed; }
    .feature-icon-wrap.ic-amber { background: #fef3c7; color: #d97706; }

    .feature-title {
        font-size: 1rem !important;
        font-weight: 700 !important;
        color: #0f172a !important;
        margin-bottom: 0.35rem !important;
    }

    .feature-desc {
        font-size: 0.85rem !important;
        color: #64748b !important;
        line-height: 1.5 !important;
    }

    /* ── Section headers ── */
    .section-label {
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #2563eb !important;
        margin-bottom: 0.25rem;
    }

    .section-heading {
        font-family: 'DM Sans', sans-serif !important;
        font-size: 1.4rem !important;
        font-weight: 800 !important;
        color: #0f172a !important;
        margin: 0 0 1.25rem !important;
    }

    .section-divider {
        height: 1px;
        background: #e2e8f0;
        margin: 2rem 0;
        border: none;
    }

    /* ── Steps ── */
    .steps-row {
        display: grid !important;
        grid-template-columns: repeat(4, 1fr) !important;
        gap: 1rem !important;
        width: 100% !important;
    }

    @media (max-width: 768px) {
        .steps-row { grid-template-columns: repeat(2, 1fr) !important; }
    }

    .step-card {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: var(--radius) !important;
        padding: 1.25rem !important;
        box-shadow: var(--shadow) !important;
        text-align: left !important;
    }

    .step-icon {
        width: 48px;
        height: 48px;
        border-radius: 12px;
        background: linear-gradient(135deg, #2563eb, #0891b2);
        color: #fff !important;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        margin-bottom: 0.75rem;
    }

    .step-num-badge {
        display: inline-block;
        background: #eff6ff;
        color: #2563eb;
        font-size: 0.7rem;
        font-weight: 800;
        padding: 3px 8px;
        border-radius: 6px;
        margin-bottom: 0.4rem;
    }

    .step-title {
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        color: #0f172a !important;
        margin-bottom: 0.25rem !important;
    }

    .step-desc {
        font-size: 0.8rem !important;
        color: #64748b !important;
        line-height: 1.45 !important;
    }

    /* ── Upload section (centered) ── */
    .upload-section-title {
        text-align: center !important;
        max-width: 640px;
        margin: 0 auto 1.25rem !important;
    }

    .upload-hero-card {
        max-width: 520px;
        margin: 0 auto 0 !important;
        padding: 2rem 2rem 1rem;
        background: #ffffff;
        border-radius: 20px 20px 0 0;
        border: 1px solid #e2e8f0;
        border-bottom: none;
        box-shadow: 0 8px 32px rgba(37, 99, 235, 0.08);
        position: relative;
        overflow: hidden;
    }

    .upload-hero-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #2563eb, #06b6d4, #7c3aed);
    }

    /* Center file uploader inside upload column */
    [data-testid="column"] [data-testid="stFileUploader"],
    [data-testid="stFileUploader"] {
        max-width: 520px !important;
        margin: 0 auto 2rem !important;
    }

    [data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"] {
        border: 1px solid #e2e8f0 !important;
        border-top: 2px dashed #93c5fd !important;
        background: #ffffff !important;
        border-radius: 0 0 20px 20px !important;
        padding: 1.5rem 1.5rem 1.75rem !important;
        text-align: center !important;
        box-shadow: 0 16px 48px rgba(37, 99, 235, 0.1), 0 4px 12px rgba(15, 23, 42, 0.04) !important;
        transition: border-color 0.2s, background 0.2s, box-shadow 0.2s !important;
    }

    [data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"]:hover {
        border-color: #2563eb !important;
        background: #eff6ff !important;
        box-shadow: 0 4px 16px rgba(37, 99, 235, 0.1) !important;
    }

    [data-testid="stFileUploader"] label,
    [data-testid="stFileUploader"] label span {
        display: none !important;
    }

    [data-testid="stFileUploader"] small {
        color: #64748b !important;
        font-size: 0.8rem !important;
        text-align: center !important;
        display: block !important;
    }

    [data-testid="stFileUploader"] button {
        background: linear-gradient(135deg, #2563eb, #4f46e5) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 0.5rem 1.25rem !important;
        margin: 0.5rem auto !important;
    }

    [data-testid="stFileUploader"] button:hover {
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35) !important;
    }

    .upload-footer-note {
        text-align: center;
        font-size: 0.78rem;
        color: #94a3b8 !important;
        margin: -1rem auto 2rem !important;
        max-width: 520px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb, #0891b2) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-family: 'Inter', sans-serif !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3) !important;
    }

    .stButton > button:hover {
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4) !important;
    }

    [data-testid="stProgress"] > div > div {
        background: linear-gradient(90deg, #2563eb, #0891b2) !important;
    }

    /* ── Result cards ── */
    .card {
        background: #ffffff !important;
        padding: 1.5rem !important;
        border-radius: var(--radius) !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: var(--shadow) !important;
        margin: 1rem 0 !important;
    }

    .card-title {
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        color: #0f172a !important;
        margin-bottom: 1rem !important;
        padding-bottom: 0.75rem !important;
        border-bottom: 1px solid #e2e8f0 !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
    }

    .card-title-icon {
        width: 38px;
        height: 38px;
        border-radius: 10px;
        background: #eff6ff;
        color: #2563eb;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 1rem;
    }

    .card-content {
        font-size: 0.92rem !important;
        color: #334155 !important;
        line-height: 1.7 !important;
    }

    .card-content h4 { color: #1d4ed8 !important; font-weight: 700 !important; }

    .card-content .section-item {
        background: #f8fafc !important;
        border-left: 3px solid #2563eb;
        padding: 10px 14px;
        border-radius: 0 8px 8px 0;
        margin: 8px 0;
    }

    /* ── Success ── */
    .success-notification {
        background: #ecfdf5 !important;
        border: 1px solid #6ee7b7 !important;
        border-radius: 12px !important;
        padding: 1rem 1.25rem !important;
        display: flex !important;
        align-items: center !important;
        gap: 14px !important;
        margin: 1rem 0 !important;
    }

    .success-notification-icon {
        width: 44px;
        height: 44px;
        background: #d1fae5;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #059669;
        font-size: 1.25rem;
    }

    .success-notification h4 {
        color: #047857 !important;
        margin: 0 !important;
        font-weight: 700 !important;
    }

    .success-notification p {
        color: #065f46 !important;
        margin: 0 !important;
        font-size: 0.9rem !important;
    }

    .results-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 0.5rem;
    }

    .results-header-bar {
        flex: 1;
        height: 3px;
        background: linear-gradient(90deg, #2563eb, #0891b2);
        border-radius: 2px;
    }

    /* ── Jobs ── */
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #eff6ff !important;
        color: #1d4ed8 !important;
        border: 1px solid #bfdbfe;
        padding: 6px 14px;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 600;
        margin: 4px 6px 4px 0;
    }

    .keywords-wrap {
        background: #ffffff !important;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0 1rem;
    }

    .job-card {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        padding: 1.2rem 1.3rem !important;
        margin: 0.6rem 0 !important;
        box-shadow: var(--shadow) !important;
    }

    .job-card:hover {
        border-color: #93c5fd !important;
        box-shadow: 0 8px 24px rgba(37, 99, 235, 0.1) !important;
    }

    .job-title {
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        color: #0f172a !important;
    }

    .job-company {
        color: #64748b !important;
        font-size: 0.9rem !important;
    }

    .job-salary-pill {
        background: linear-gradient(135deg, #2563eb, #4f46e5) !important;
        color: #ffffff !important;
        padding: 6px 14px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
    }

    .job-meta {
        color: #64748b !important;
        font-size: 0.85rem;
        display: flex;
        gap: 1rem;
        margin-top: 0.5rem;
    }

    /* ── Footer ── */
    .features-grid {
        display: grid !important;
        grid-template-columns: repeat(4, 1fr) !important;
        gap: 1rem !important;
        margin-top: 2.5rem !important;
        padding-top: 2rem !important;
        border-top: 1px solid #e2e8f0 !important;
    }

    @media (max-width: 768px) {
        .features-grid { grid-template-columns: repeat(2, 1fr) !important; }
    }

    .bottom-feature {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        padding: 1.25rem 1rem !important;
        text-align: center !important;
        box-shadow: var(--shadow) !important;
    }

    .bottom-feature-icon {
        width: 48px;
        height: 48px;
        margin: 0 auto 0.6rem;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
    }

    .bottom-feature-icon.fi-1 { background: #dbeafe; color: #2563eb; }
    .bottom-feature-icon.fi-2 { background: #ede9fe; color: #7c3aed; }
    .bottom-feature-icon.fi-3 { background: #fef3c7; color: #d97706; }
    .bottom-feature-icon.fi-4 { background: #d1fae5; color: #059669; }

    .bottom-feature-title {
        font-weight: 700 !important;
        color: #0f172a !important;
        font-size: 0.88rem !important;
    }

    .bottom-feature-desc {
        color: #64748b !important;
        font-size: 0.78rem !important;
        margin-top: 0.3rem !important;
    }

    .app-footer {
        text-align: center;
        padding: 2rem 1rem;
        color: #94a3b8 !important;
        font-size: 0.82rem;
    }

    .app-footer strong { color: #2563eb !important; }
</style>
"""

APP_STYLES = DARK_THEME_STYLES
__all__ = ["DARK_THEME_STYLES", "APP_STYLES"]
