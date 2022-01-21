
import streamlit as st
import cv2
import os
import keras
from keras.models import load_model

from helper_functions import *

def save_uploadedfile(uploadedfile):
    path = os.path.join("uploads", uploadedfile.name)
    with open(path, "wb") as f:
         f.write(uploadedfile.getbuffer())
    return path

st.title("Chess Positions -  FEN description")

uploaded_file = st.file_uploader("Choose a file", type=["jpeg", "png"])

if uploaded_file is not None:
    uploaded_file_path = save_uploadedfile(uploaded_file)
    img = cv2.imread(uploaded_file_path, cv2.IMREAD_GRAYSCALE)
    data = split_chessboard_into_64_images(img)
    data = np.array(data)
    data = data.reshape(data.shape + (1,))

    model = load_model("chess_model_v1.h5")

    pred = model.predict(data)
    pred = pred.argmax(axis=1).reshape(-1, 8, 8)
    st.image(img, caption='Chessboard Image.', width=200)
    st.write("Prediction: {}".format(fen_from_onehot(pred[0])))

    