import streamlit as st
import pandas as pd
import numpy as np
import cv2

from scripts.imageEnhancement import applyCLAHE, applyRedFree

st.title('Image Enhancement Demo')

@st.cache
def getImage(imagePath: str):
    image = cv2.imread(str(imagePath))

    return image

image_load_state = st.text('Loading Demo Image...')
image = getImage('dataSample/demoImage.JPG')
image_load_state.text("Done! (using st.cache)")

st.subheader('Source Image')

imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
st.image(
    imageRGB,
    caption='Source Image (Demo)',
    use_column_width=True)

if st.checkbox('Show CLAHE Output'):

    st.subheader('CLAHE Output Image')

    claheOutput = applyCLAHE(image)
    claheOutputRGB = cv2.cvtColor(claheOutput, cv2.COLOR_BGR2RGB)

    st.image(
        claheOutputRGB,
        caption='CLAHE Output',
        use_column_width=True)

if st.checkbox('Show Red Free Output'):

    st.subheader('Red Free Output Image')

    redFreeOutput = applyRedFree(image)
    redFreeOutputRGB = cv2.cvtColor(redFreeOutput, cv2.COLOR_BGR2RGB)

    st.image(
        redFreeOutputRGB,
        caption='CLAHE Output',
        use_column_width=True)

if st.checkbox('Show Red Free & CLAHE Output'):

    st.subheader('Show Red Free & CLAHE Image')

    claheImage = applyCLAHE(image)
    claheRedFreeOutput = applyRedFree(claheImage)

    claheRedFreeOutputGB = cv2.cvtColor(claheRedFreeOutput, cv2.COLOR_BGR2RGB)

    st.image(
        claheRedFreeOutputGB,
        caption='CLAHE & Red Free Output',
        use_column_width=True)