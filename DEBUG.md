# Debugging Guide - AI Job Recommender

## Why Analysis Fields Were Not Showing

The analysis cards (Professional Summary, Skill Gaps & Missing Areas) should display after uploading a resume PDF. If they weren't showing, here are the common reasons:

### 1. **API Key Issues**
- The Groq API key wasn't set in your `.env` file
- Missing `GROQ_API_KEY` environment variable
- **Fix**: Ensure your `.env` has: `GROQ_API_KEY=your_actual_key`

### 2. **PDF Processing Error**
- The PDF extraction failed silently
- Resume text was empty or corrupted
- **Fix**: Try a different PDF file, ensure it's text-based (not scanned image)

### 3. **API Response Timeout**
- Groq API took too long to respond
- Request was interrupted
- **Fix**: Check your internet connection and API rate limits

### 4. **Empty Analysis Response**
- The AI model returned empty or invalid data
- **Fix**: Check API usage in Groq console

## Recent Changes Made

### ✅ Separated Styles to `styles.py`
- All CSS styles moved to a dedicated file
- Main.py now imports styles from `styles.py`
- Benefits: 
  - Cleaner code
  - Easier to maintain styles
  - Reusable across files

### ✅ Updated API to Groq
- Switched from Google Gemini to Groq (faster & free tier)
- Uses `llama3-8b-8192` model
- Better error handling with retries

### ✅ Fixed Styling
- Success notification now uses CSS class
- Improved dark theme consistency
- Better visual hierarchy

## Testing the App

To verify everything is working:

```bash
# 1. Set your Groq API key
# Edit .env file and add: GROQ_API_KEY=your_key_here

# 2. Run the app
streamlit run main.py

# 3. Upload a PDF resume
# You should see:
# - Step 1/4: Extract text
# - Step 2/4: Analyze resume
# - Step 3/4: Extract summary
# - Step 4/4: Extract skill gaps

# 4. Success notification appears
# 5. Analysis cards display with:
#    - ATS Resume Analysis (full analysis)
#    - Professional Summary
#    - Skill Gaps & Missing Areas
```

## File Structure After Changes

```
c:\WEATHER-MCP\
├── main.py                 # Main application (imports styles)
├── styles.py              # All CSS styles (NEW)
├── tools/
│   ├── helper.py          # Groq API functions
│   ├── job_api.py         # Job scraping
│   └── __init__.py
├── .env                   # API keys (GROQ_API_KEY required)
└── requirements.txt
```

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| "API Error" message | Check GROQ_API_KEY in .env |
| No analysis cards | Wait for Steps 1-4 to complete |
| Timeout errors | Check internet, retry upload |
| Blank cards | PDF file quality issue, try another |

## Need Help?

1. Check the .env file has `GROQ_API_KEY`
2. Verify PDF is not a scanned image
3. Check browser console for errors (F12)
4. Ensure all dependencies installed: `pip install -r requirements.txt`
