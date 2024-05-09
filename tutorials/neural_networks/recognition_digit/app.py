# libraries
import os
import cv2
import numpy as np
import tensorflow as tf

import streamlit as st
from PIL import Image
import requests
import tempfile

# function 1 : to classify the image
def classify_digit(model, image):
    img = cv2.imread(image)[:,:,0]
    img = np.invert(np.array([img]))
    prediction = model.predict(img)
    return prediction

# function 2 : to resize the image
def resize_image(image, target_size):
    img = Image.open(image)
    resized_image = img.resize(target_size)
    return resized_image

# page name
st.set_page_config('Digit Recognition', page_icon= '🔢')

# example of the title, markdown, etc
st.title('Handwritten Digit Recognition 🔢')
st.caption('by Dmytro Varich')

st.markdown(r'''This simple application is designed to recognize a number from 0-9 from a PNG file with a resolution of 28x28 pixels. 
            While it may not achieve 100% accuracy, but its performance is consistently high.''')
st.subheader("Explore the model's effectiveness 😊")

uploaded_image = st.file_uploader('Insert a picture of a number from 0-9', type= 'png')

if uploaded_image is not None:

    image_np = np.array(Image.open(uploaded_image))

    temp_image_path = os.path.join(tempfile.gettempdir(), 'temp_image.png')
    cv2.imwrite(temp_image_path, image_np)

    resized_image = resize_image(uploaded_image, (300, 300))

    col1, col2, col3 = st.columns(3)
    # Placing the image in the second column will ensure it is displayed in the center of the application.
    with col2:
        st.image(resized_image)

    # here we make a button to predict the image
    submit = st.button('Predict')

    if submit:
      # load the model
      model_url = r'https://raw.githubusercontent.com/dmytro-varich/Programming-Problems-Solutions/main/tutorials/neural_networks/recognition_digit/handwrittendigit.keras'
      # Path to save the model locally
      local_model_path = 'handwrittendigit.keras'
      # Loading a model from a remote source and saving to a local file
      response = requests.get(model_url)
      with open(local_model_path, 'wb') as f:
          f.write(response.content)
      # Loading a model from a local file
      model = tf.keras.saving.load_model(local_model_path)
      # use the model to predict new image
      prediction = classify_digit(model, temp_image_path)
      st.subheader('Prediction Result')
      # Using np.argmax(prediction) will reveal the number with the highest probability as predicted by our model
      st.success(f'The digit is probably a {np.argmax(prediction)}')

    os.remove(temp_image_path)
