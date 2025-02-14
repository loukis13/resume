import streamlit as st
import os

# Streamlit page setup
st.set_page_config(page_title="Thanos' Resume", page_icon="📄", layout="centered")

# Page Title
st.title("Welcome to My Resume Page")
st.write("""
### 📌 View or Download My Resume
Click the button below to access my resume.
""")

# Resume File Path
resume_path = "Athanasios Loukakos CV.pdf"  # Make sure this file is in the same folder

# Check if the file exists before displaying the button
if os.path.exists(resume_path):
    with open(resume_path, "rb") as resume_file:
        resume_bytes = resume_file.read()
    
    # Download Button
    st.download_button(
        label="📄 Download My Resume",
        data=resume_bytes,
        file_name="Athanasios_Loukakos_CV.pdf",
        mime="application/pdf"
    )
else:
    st.error("❌ Resume file not found. Please check the file name and location.")

# Footer
st.markdown("""
---
**Contact Me**  
📧 Email: thanos.loukakos@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/thanos-loukakos-2180ba210/)
""")
