#!/usr/bin/env python3
"""
Quick test to verify styling is loading correctly
Run: streamlit run test_ui.py
"""

import streamlit as st
from styles import DARK_THEME_STYLES

st.set_page_config(page_title="UI Test", layout="wide")

# Load styles
st.markdown(DARK_THEME_STYLES, unsafe_allow_html=True)

# Test 1: Header
st.markdown('<div class="header-title">Find Your <span class="highlight-text">Dream Job</span><br>with AI</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="header-subtitle">
    Upload your resume, get AI analysis of your skills, experiences, and credentials to recommend jobs that are perfect for you.
    </div>
""", unsafe_allow_html=True)

# Test 2: Section Divider
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Test 3: Feature Boxes
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Smart Matching</div>
            <div class="feature-desc">Intelligent matching with jobs</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">📊</div>
            <div class="feature-title">NLP Scores</div>
            <div class="feature-desc">Advanced text analysis</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Instant Results</div>
            <div class="feature-desc">Get recommendations instantly</div>
        </div>
    """, unsafe_allow_html=True)

# Test 4: Card
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.markdown("""
    <div class="card">
        <div class="card-title">👤 Professional Summary</div>
        <div class="card-content">This is a test card to verify styling is working correctly. All text should be clearly visible.</div>
    </div>
""", unsafe_allow_html=True)

# Test 5: Button
st.button("✨ Test Button")

st.success("✅ If you can see all elements above clearly, styling is working correctly!")
