import pickle
import numpy as np
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
import pygame
# Disabling tensorflow import error messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing import image_dataset_from_directory

# Loading trained model
model_file = '/home/olli/Desktop/Koodauskrääsää/githubs/tori_classifier/tori_classifier_model.sav'
model = pickle.load(open(model_file, 'rb'))

# Preprocessing image for the model's preferred input
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_final = preprocess_input(img_batch)
    return img_final

def predict():
    file = entry.get()
    img = preprocess_image(file)
    prediction = model.predict(img)
    prediction = prediction.round()
    if prediction == 0:
        showinfo(title='Result', message="Not a chair")
    else:
        showinfo(title='Result', message="Category")

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("bg_music.mp3")
    pygame.mixer.music.play(loops=100)

root = tk.Tk()
root.geometry("")
root.title("Tori Category Autofiller 2000")
root.configure(bg='white')

window_final= tk.Frame(root, bg='white')
window_final.pack(padx=10, pady=10, expand=True)
img = ImageTk.PhotoImage(Image.open('tori.png'))
label_img = tk.Label(window_final, image = img, pady=10, bg='white')
label_img.pack()

label = tk.Label(window_final, text="Enter Image: ", bg='white')
entry = tk.Entry(window_final, fg="red", bg="white", width=50)
entry.focus()

label.pack()
entry.pack()

enter_button = tk.Button(
    window_final, 
    text="upload image", 
    command=predict, 
    justify='center',
    activebackground='red'
    )
enter_button.pack(side='bottom')

play()
root.mainloop()
