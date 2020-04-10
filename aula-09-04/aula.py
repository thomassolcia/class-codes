import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.title('Aula do dia 09/04')

image = Image.open('monte_fuji.jpg')
imagem_color_arr = np.array(image)
img_gray = np.mean(imagem_color_arr, axis=2)

limiar64 = st.slider('Limiar 1?', 0, 64, 50)
limiar128 = st.slider('Limiar 2?', 64, 128, 100)
limiar192 = st.slider('Limiar 3?', 128, 192, 150)
limiar255 = st.slider('Limiar 4?', 192, 255, 200)

img_gray = np.mean(imagem_color_arr, axis=2)

img_gray[img_gray < limiar64] = 0
img_gray[(img_gray < limiar128).all() and (img_gray > limiar64).all()] = 64
img_gray[(img_gray < limiar192).all() and (img_gray > limiar128).all()] = 128
img_gray[img_gray > limiar192] = 192

new_image = Image.fromarray(img_gray)
plt.axis('off')
st.text(img_gray.shape)
plt.imshow(new_image)
plt.show()
st.pyplot()

image1 = Image.open('unsplash.jpg')
imagem_color_arr1 = np.array(image1)
img_gray1 = np.mean(imagem_color_arr1, axis=2)

img_gray1 = np.mean(imagem_color_arr1, axis=2)

img_gray1[img_gray1 < limiar64] = 0
img_gray1[(img_gray1 < limiar128).all() and (img_gray1 > limiar64).all()] = 64
img_gray1[(img_gray1 < limiar192).all() and (img_gray1 > limiar128).all()] = 128
img_gray1[img_gray1 > limiar192] = 192

st.text(img_gray1.shape)

# st.text ('limiar < ',limiar64,' -> 0')
# st.text ('limiar < ',limiar128,'e limiar > ',limiar64,' ->','64')
# st.text ('limiar < ',limiar192,'e limiar > ',limiar128, ' ->','128')
# st.text ('limiar < ',limiar255, ' ->','192')

new_image1 = Image.fromarray(img_gray1)
plt.axis('off')
plt.imshow(new_image1)

plt.show()
st.pyplot()