# _*_ coding:utf-8 _*_

import streamlit as st
from PIL import Image

def main():
    img = Image.open('data/image_03.jpg')
    st.image(img)

    with open('data/secret_of_success.mp4', 'rb') as rb:
        video_file = rb.read()
        st.video(video_file, start_time=1)
        
    with open('data/song.mp3', 'rb') as rb:
        audio_file = rb.read()
        st.video(audio_file, format='audio/mp3')

if __name__ == "__main__":
    main()