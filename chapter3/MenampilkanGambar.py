from PIL import Image, ImageTk
import tkinter as tk


root = tk.Tk()
root.title("Multimedia Application")

# Memuat gambar menggunakan Pillow
image = Image.open('merah.jpg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()


# Menjalankan loop acara Tkinter
root.mainloop()