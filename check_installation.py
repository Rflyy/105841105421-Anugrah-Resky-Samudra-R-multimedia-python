import pygame
import PIL
import cv2
import moviepy.editor as mp
import pydub
import tkinter as tk
import subprocess

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    
    # Mendapatkan versi MoviePy menggunakan pip
    result = subprocess.run(["pip", "show", "moviepy"], stdout=subprocess.PIPE, text=True)
    for line in result.stdout.splitlines():
        if line.startswith("Version:"):
            moviepy_version = line.split(" ")[1]
            print("✅ MoviePy version:", moviepy_version)
            break
    else:
        print("⚠️ MoviePy version not found.")
    
    # Mendapatkan versi pydub menggunakan pip
    result = subprocess.run(["pip", "show", "pydub"], stdout=subprocess.PIPE, text=True)
    for line in result.stdout.splitlines():
        if line.startswith("Version:"):
            pydub_version = line.split(" ")[1]
            print("✅ Pydub version:", pydub_version)
            break
    else:
        print("⚠️ Pydub version not found.")
    
    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()
