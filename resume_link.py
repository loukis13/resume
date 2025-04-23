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
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .button-style {
        font-size: 20px;
        font-weight: bold;
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

# LinkedIn Profile Image (Smaller size)
linkedin_image_path = "linkedin picture.jpg"  # Ensure this file is in the same directory
if os.path.exists(linkedin_image_path):
    with col1:
        st.image(linkedin_image_path, width=150, caption="Thanos (Athanasios) Loukakos")

# Description
with col2:
    st.write("""
    **Highly motivated and results-oriented Economics and Finance student (Northeastern University, expected May 2025)**  
    Proven track record of leveraging **data analytics and programming skills (Python, SQL, Power BI)** to drive **process improvements and efficiency gains** in financial services.

    Seeking a **challenging role in Fintech/Finance** where I can apply my **analytical abilities** and contribute to **data-driven decision-making**.
    """)

# Section: Resume Download
st.markdown('<h2 class="subtitle">📌 View or Download My Resume</h2>', unsafe_allow_html=True)
resume_path = "Athanasios (Thanos) Loukakos Resume.pdf"  # Updated file name

# Check if the file exists before displaying the button
if os.path.exists(resume_path):
    with open(resume_path, "rb") as resume_file:
        resume_bytes = resume_file.read()

    # Display the download button with adjusted font size
    st.download_button(
        label="📄 Download My Resume",
        data=resume_bytes,
        file_name="Athanasios_Loukakos_Resume.pdf",
        mime="application/pdf",
        help="Click to download my resume",
        key="download_resume"
    )
else:
    st.error("❌ Resume file not found. Please check the file name and location.")

# Sidebar Contact Details
st.sidebar.markdown("## 📬 Contact Me")
st.sidebar.write("📧 Email: thanos.loukakos@gmail.com")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/thanos-loukakos-2180ba210/)")

# Add a fun interactive button
if st.button("Say Hi 👋"):
    st.success("Hello! Thanks for visiting my page. Feel free to reach out!")

# Footer
st.markdown("---")
st.markdown("© 2025 Athanasios (Thanos) Loukakos | Powered by Streamlit 🚀")
