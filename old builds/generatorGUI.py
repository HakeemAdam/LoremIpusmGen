import random
import sys
import os
import tkinter as tk
from tkinter import font
import requests
from gtts import gTTS

height = 700
width = 700

language = 'en-uk'
index = 1
chain = {}
count = 100

# Read poem
existing_text = open('LoremIpsum.txt').read()

# break poem into list
existing_text = ''.join([i for i in existing_text if not i.isdigit()]).replace("\n", " ").split(' ')

# extracting letter from text and adding them to a chain Very important step. Here we slice the list and refer to the
# index of each word in the list to randomly sequence as new poem. for loop finds index of each word and if statement
# but rearranges them to avoid repeats

for word in existing_text[index:]:  # selecting  first index. 1. ie 1-1= 0 positing on list
    letter = existing_text[index - 1]
    if letter in chain:
        chain[letter].append(word)  # add words to create chain based on position
    else:
        chain[letter] = [word]  # avoid repeats and iterate over count
    index += 1

# composing words from string of letters
word1 = random.choice(list(chain.keys()))
message = word1.capitalize()

if __name__ == "__main__":

    # composing poem by choosing words

    while len(message.split(' ')) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2

    # Saving Poem and reading in terminal

    with open("results.txt", "w") as file:
        file.write(message)
    output = open("results.txt", "r")
    print(output.read())

    # using Google text to speech to read poem
    myobj = gTTS(text=message, lang=language, slow=False)
    myobj.save("LorenIpsum.mp3")
