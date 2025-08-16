import streamlit as st
from PIL import Image

# Start the camera
st.title("Color to Grayscale Converter")
st.subheader("This website allows you to easily convert a photo"
             "to grayscale version")
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    #create a pillow image instance
    img = Image.open(camera_image)

    #convert the pillow image to grayscale
    gray_img = img.convert("L")

    #display the grayscale image on the webpage
    st.image(gray_img)

if uploaded_image:
    uploaded_img = Image.open(uploaded_image)
    uploaded_gray_img = uploaded_img.convert("L")
    st.image(uploaded_gray_img)