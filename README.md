# 💼 AI Job Recommender System

An AI-powered job recommender system that analyzes your resume and provides personalized job recommendations from top job portals like Naukri.

## ✨ Features

- 📄 **Resume Analysis** - Extract and analyze resume content
- 🎯 **Skill Assessment** - Identify skill gaps and areas for improvement
- 🗺️ **Career Roadmap** - Get personalized career development suggestions
- 💼 **Job Recommendations** - Find jobs matching your profile from Naukri
- 🤖 **AI-Powered** - Powered by Google's Gemini API
- 🎨 **Modern UI** - Beautiful, responsive Streamlit interface

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API Key (get it at https://ai.google.dev)
- Apify API Key (for job scraping)

### Installation

1. **Clone the repository**
```bash
git clone <repo-url>
cd WEATHER-MCP
```

2. **Create and activate virtual environment**
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Copy `.env.example` to `.env` and fill in your API keys:
```bash
cp .env.example .env
```

Edit `.env`:
```
GEMINI_API_KEY=your_gemini_api_key_here
APIFY_API_KEY=your_apify_api_key_here
```

### Get Your API Keys

**Gemini API Key:**
1. Visit https://ai.google.dev
2. Click "Get API Key"
3. Create new API key in Google Cloud Console
4. Copy and paste in `.env`

**Apify API Key:**
1. Visit https://apify.com
2. Sign up for free account
3. Get your API key from dashboard
4. Copy and paste in `.env`

### Run the Application

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`

## 📝 How to Use

1. **Upload Resume** - Click the upload button and select your PDF resume
2. **Wait for Analysis** - The app will:
   - Extract text from your PDF
   - Generate a resume summary
   - Identify skill gaps
   - Create a career roadmap
3. **Get Job Recommendations** - Click the button to:
   - Extract relevant job keywords
   - Search for matching jobs on Naukri
   - Display results with details

## 📁 Project Structure

```
WEATHER-MCP/
├── main.py                 # Main Streamlit app
├── tools/
│   ├── helper.py          # API utilities (Gemini, PDF extraction)
│   ├── job_api.py         # Job scraping functions
│   └── __init__.py
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This file
```

## 🔧 Technologies Used

- **Streamlit** - Web framework
- **Google Generative AI (Gemini)** - LLM for resume analysis
- **PyMuPDF** - PDF text extraction
- **Apify** - Job scraping
- **Python 3.8+**

## 📊 API Models

- **Gemini**: `gemini-1.5-flash` (fast and cost-effective)

## ⚠️ Troubleshooting

**"API quota exceeded" error:**
- Check your Gemini API quota at https://ai.google.dev
- Ensure API key is correctly set in `.env`

**"No jobs found" warning:**
- Try different keywords
- Check Apify credit balance at https://apify.com

**PDF extraction fails:**
- Ensure PDF is not corrupted
- Try a different PDF file

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues or questions, please open an issue on the repository.

---

**Built with ❤️ using Streamlit and Gemini API**
