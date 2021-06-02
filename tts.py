#this script works, but if you press the save button twice it crashes
#can't overwrite the file

#Linux:
#sudo apt install python3-tk
#pip3 install pyttsx3
#sudo apt install espeak
#sudo apt install ffmpeg

#https://pypi.org/project/pyttsx3/
#you can also change things like volume ect

from tkinter import *
import pyttsx3

root = Tk()

engine = pyttsx3.init()
#set the speed of the voice
engine.setProperty('rate', 125)

def talk():
  engine.say(my_input.get())
  engine.runAndWait()
  my_input.delete(0, END)

def save():
  #you can save a file to .mp3 or .wav works both  
  engine.save_to_file(my_input.get(), '/home/bf/Coding/Python/PyTTS/test.wav')
  engine.runAndWait()

#make an input box
my_input = Entry(root, width = 60)
my_input.pack()

my_button = Button(root, text = "speak", command = talk)
my_button.pack()

save_button = Button(root, text = "save to file", command = save)
save_button.pack()

root.mainloop()
