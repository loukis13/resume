import streamlit as st
import os

# Streamlit page setup
st.set_page_config(page_title="Thanos' Resume", page_icon="📄", layout="wide")

# Custom Styles
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #0077b5;
    }
    .subtitle {
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .description-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
    }
    .description-text {
        font-size: 16px;
        line-height: 1.5;
        max-width: 600px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown('<h1 class="title">Welcome to Thanos\' Resume Page</h1>', unsafe_allow_html=True)

# Profile Picture and Description (Side-by-Side Layout)
st.markdown('<h2 class="subtitle">👋 About Me</h2>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])  # Adjust width ratio

with col1:
    # LinkedIn Profile

