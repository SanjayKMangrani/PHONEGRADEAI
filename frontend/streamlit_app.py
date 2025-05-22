import streamlit as st
import requests

# Set up page config
st.set_page_config(page_title="PhoneGradeAI", page_icon="📱")

# Title and project purpose
st.title("📱 PhoneGradeAI")

st.markdown("""
Welcome to **PhoneGradeAI** – a personal project created for my portfolio to demonstrate how AI can be used to detect **damaged mobile phones** from images.

⚠️ **Note:** This is a hobby project and not intended for commercial or diagnostic use.

Real-World Application: This solution can be adapted and embedded into real-world industrial settings, such as phone refurbishment or repair centers. 
By integrating this model with a camera sensor and a conveyor belt system, companies can automatically assess the physical condition of mobile phones at scale.
This automation can significantly enhance quality control, speed up processing, and reduce manual inspection errors in high-volume repair facilities.

---

### 📸 How to Use:
1. Take a clear photo of the **mobile phone screen** or find it from web.
2. Upload the image below (supported formats: `.jpg`, `.png`, `.jpeg`).
3. Click **"Check Condition"** to see if the phone is classified as **Good** or **Damaged**.

""")

# File upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded image", use_container_width=True)

    if st.button("Check Condition"):
        # Reset the file pointer to start in case it was read by st.image
        uploaded_file.seek(0)
        files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post("https://phonegrade-backend-production.up.railway.app/predict", files=files)

        if response.status_code == 200:
            result = response.json()
            st.success(f"📋 **Condition:** {result['condition']}")
            st.info(f"📊 **Confidence:** {result['confidence']}%")
        else:
            st.error("❌ Failed to get prediction from server. Please try again.")
