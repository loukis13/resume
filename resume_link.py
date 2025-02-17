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
    .center {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown('<h1 class="title">Welcome to Thanos\' Resume Page</h1>', unsafe_allow_html=True)

# LinkedIn Profile Image
linkedin_image_path = "linkedin picture.jpg"  # Ensure this file is in the same directory
if os.path.exists(linkedin_image_path):
    st.image(linkedin_image_path, width=200, caption="Thanos Loukakos", use_column_width=False)

# Section: Resume Download
st.markdown('<h2 class="subtitle">📌 View or Download My Resume</h2>', unsafe_allow_html=True)
resume_path = "Athanasios Loukakos Resume.pdf"  # Updated file name

# Check if the file exists before displaying the button
if os.path.exists(resume_path):
    with open(resume_path, "rb") as resume_file:
        resume_bytes = resume_file.read()

    # Display the download button with a more interactive style
    st.markdown('<div class="center">', unsafe_allow_html=True)
    st.download_button(
        label="📄 Download My Resume",
        data=resume_bytes,
        file_name="Athanasios_Loukakos_Resume.pdf",
        mime="application/pdf",
        help="Click to download my resume"
    )
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.error("❌ Resume file not found. Please check the file name and location.")

# Sidebar Contact Details
st.sidebar.markdown("## 📬 Contact Me")
st.sidebar.write("📧 Email: thanos.loukakos@gmail.com")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/thanos-loukakos-2180ba210/)")

# Interactive About Me Section
st.markdown("---")
st.markdown('<h2 class="subtitle">👋 About Me</h2>', unsafe_allow_html=True)

with st.expander("Click to learn more about me"):
    st.write("""
    I am a highly motivated individual with a background in Economics and Finance. 
    With hands-on experience in **data analysis, compliance, automation**, and **financial modeling**, 
    I bring a mix of technical and business expertise.

    Skills:
    - 📊 **Data Analytics & Visualization:** Excel, Power BI, Tableau
    - 🐍 **Programming:** Python (Pandas, NumPy, Streamlit)
    - 🔍 **Financial Risk & Compliance:** SQL, Alteryx, Corporate Finance
    - 🎯 **Passions:** Basketball 🏀, Ironman training 🏊‍♂️🚴‍♂️🏃‍♂️, and Tech Enthusiasm 💻

    Feel free to connect with me for opportunities or collaborations!
    """)

# Add a fun interactive button
if st.button("Say Hi 👋"):
    st.success("Hello! Thanks for visiting my page. Feel free to reach out!")

# Footer
st.markdown("---")
st.markdown("© 2025 Thanos Loukakos | Powered by Streamlit 🚀")
