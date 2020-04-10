import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.title('Aula do dia 09/04')
image = Image.open('monte_fuji.jpg')
imagem_color_arr = np.array(image)
img_gray = np.mean(imagem_color_arr, axis=2)
st.text(img_gray.shape)

limiar64 = st.slider('Limiar 1?', 0, 64, 0)
limiar128 = st.slider('Limiar 2?', 64, 128, 64)
limiar192 = st.slider('Limiar 3?', 128, 192, 128)
limiar255 = st.slider('Limiar 4?', 192, 255, 192)
st.text(limiar64)

img_gray = np.mean(imagem_color_arr, axis=2)

img_gray[img_gray < limiar64] = 0
img_gray[(img_gray < limiar128).all() and (img_gray > limiar64).all()] = 64
img_gray[(img_gray < limiar192).all() and (img_gray > limiar128).all()] = 128
img_gray[img_gray > limiar192] = 192

new_image = Image.fromarray(img_gray)
plt.axis('off')
plt.imshow(new_image)
plt.show()
st.pyplot()