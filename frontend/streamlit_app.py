import streamlit as st
import requests

st.set_page_config(page_title="PhoneGradeAI", page_icon="📱")

st.title("📱 PhoneGradeAI")
st.markdown("Upload a phone image to check if it's **Good** or **Damaged**.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded image", use_container_width=True)

    if st.button("Check Condition"):
        # Reset the file pointer to start in case it was read by st.image
        uploaded_file.seek(0)
        files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post("http://127.0.0.1:5000/predict", files=files)

        if response.status_code == 200:
            result = response.json()
            st.success(f"📋 **Condition:** {result['condition']}")
            st.info(f"📊 **Confidence:** {result['confidence']}%")
        else:
            st.error("Failed to get prediction from server.")
