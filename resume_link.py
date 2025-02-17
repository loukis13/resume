import streamlit as st
import os
from PIL import Image
import time

# Streamlit page setup
st.set_page_config(page_title="Thanos' Resume", page_icon="📄", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Contact"])

# Load LinkedIn Picture
image_path = "linkedin picture.jpg"
if os.path.exists(image_path):
    profile_image = Image.open(image_path)
else:
    profile_image = None

if page == "Home":
    # Profile Section
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if profile_image:
            st.image(profile_image, caption="Athanasios Loukakos", width=200)
        else:
            st.warning("Profile image not found.")
    
    with col2:
        st.title("Welcome to Thanos's Resume Page ✨")
        st.write("""
        **Hello! I'm Athanasios 'Thanos' Loukakos, an aspiring professional in finance and data analytics.**
        
        Explore my resume, connect with me on LinkedIn, or send me an email. Looking forward to networking!
        """)
        
        # Animated loading effect
        with st.spinner("Loading resume..."):
            time.sleep(1)

        # Resume Download Section
        resume_path = "Athanasios Loukakos Resume.pdf"
        if os.path.exists(resume_path):
            with open(resume_path, "rb") as resume_file:
                resume_bytes = resume_file.read()
            
            st.download_button(
                label="📄 Download My Resume",
                data=resume_bytes,
                file_name="Athanasios_Loukakos_Resume.pdf",
                mime="application/pdf",
                help="Click to download my latest resume."
            )
        else:
            st.error("❌ Resume file not found. Please check the file name and location.")
    
elif page == "Contact":
    st.title("📞 Contact Me")
    st.write("""
    Feel free to reach out to me via email or LinkedIn.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("📧 **Email:** thanos.loukakos@gmail.com")
        st.button("Send Email", on_click=lambda: st.write("Copy my email: thanos.loukakos@gmail.com"))
    
    with col2:
        st.write("🔗 **LinkedIn:** [Visit my profile](https://www.linkedin.com/in/thanos-loukakos-2180ba210/)")
        st.button("Open LinkedIn", on_click=lambda: st.write("Click the link above to visit my profile."))

# Footer
st.markdown("""
---
💡 *Built with Streamlit* | 🚀 *Interactive Resume Site*
""")
