import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.title('Atividade dia 16/04')

num_color = st.selectbox("Quantas cores?", \
    (2, 4, 8, 16, 32, 64, 128))

image = Image.open('unsplash.jpg')
imagem_color_arr = np.array(image)
img_gray = np.mean(imagem_color_arr, axis=2)
st.text(img_gray.shape)

if(num_color == 2):
    img_gray[img_gray < 127]  = 0
    img_gray[img_gray >= 127]  = 255
else:
    ax = int(255/num_color)
    for x in range(0,num_color):
        if(x == 0):
            img_gray[img_gray < ((ax+1)*1)] = 0
            img_gray[img_gray > (255-ax)]  = 255
        else:
            img_gray[(((ax+1)*x) < img_gray) & (img_gray <((ax+1)*(x+1)))] = (ax+1)*x

new_image = Image.fromarray(img_gray)
st.image([new_image.convert("L"), image], caption=['Cinza', 'colorida'], width=480,)

image1 = Image.open('monte_fuji.jpg')
imagem_color_arr1 = np.array(image1)
img_gray1 = np.mean(imagem_color_arr1, axis=2)
st.text(img_gray1.shape)

if(num_color == 2):
    img_gray1[img_gray1 < 127]  = 0
    img_gray1[img_gray1 >= 127]  = 255
else:
    ax = int(255/num_color)
    for x in range(0,num_color):
        if(x == 0):
            img_gray1[img_gray1 < ((ax+1)*1)] = 0
            img_gray1[img_gray1 > (255-ax)]  = 255
        else:
            img_gray1[(((ax+1)*x) < img_gray1) & (img_gray1 <((ax+1)*(x+1)))] = (ax+1)*x

new_image1 = Image.fromarray(img_gray1)
st.image([new_image1.convert("L"), image1], caption=['Cinza', 'colorida'], width=480,)