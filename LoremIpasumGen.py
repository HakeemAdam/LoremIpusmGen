"""
LoremIpsumGen

============================================================
A Conceptual Poetry Generator

This application rearranges an exiting poem to create an recite a new poem
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import markovify
import Pmw
from gtts import gTTS
import vlc

root = tk.Tk()
root.geometry("500x500")

top = tk.Frame(root, bd=5)
top.pack()


def openfile():
    """
    Reads the file from a directory


        :return: new_file
    """
    new_file = filedialog.askopenfilename(initialdir="/Users/hakeem/Desktop/LoremIpsumGen/app", title="Open File",
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

    try:
        if new_file:
            the_file = open(new_file)
        elif new_file == '':
            messagebox.showinfo("Cancel")
    except IOError:
        messagebox.showinfo("Error")

    return new_file


def createPoem(file):
    """
        Using the Markofiy module to rearrange the poem into a new poem

            :param file: txt file
            :param type: object

            :return: newPoem
    """

    with open(file) as f:
        text = f.read()

    text_model = markovify.Text(text, state_size=1)
    newtext = text_model.make_sentence()

    with open('/Users/hakeem/Desktop/LoremIpsumGen/app/results/results.txt', 'a') as f:
        newPoem = f.write(newtext + '\n')

    return newPoem


def readpoem():
    """
        Using Google text to speech to read poem

        :return: none

    """
    myobj = gTTS(text=message, lang=language, slow=False)
    myobj.save("LoremIpsumGen.mp3")


def openPoem(newpoem):
    """
            Using the Markofiy module to rearrange the poem into a new poem

                :param newpoem: txt file
                :param type: object

                :return: none
        """
    filename = newpoem
    text = Pmw.ScrolledText(top,
                            borderframe=10,
                            vscrollmode='dynamic',
                            hscrollmode='dynamic',
                            labelpos='n',
                            label_text='file %s' % filename,
                            text_width=40,
                            text_height=20,
                            text_wrap='none',
                            )
    text.pack()
    text.insert('end', open(filename, 'r').read())


def playPoem():
    """
        Using Vlc to read and play the poem

        :return: none

     """
    p = vlc.MediaPlayer("/Users/hakeem/Desktop/LoremIpsumGen/app/sound_result/LorenIpsum.mp3")
    p.play()


tk.Button(top, text='Open', command=openfile).pack(pady=5)
tk.Button(top, text='Generate', command=createPoem(openfile())).pack(pady=5)
tk.Button(top, text='Display', command=lambda: openPoem(openfile())).pack(pady=5)
tk.Button(top, text='Play', command=playPoem).pack(pady=5)
tk.Button(top, text='Quit', command=root.destroy).pack(pady=5)
root.mainloop()
