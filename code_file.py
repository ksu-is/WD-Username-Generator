import random
from tkinter import *

usernames = ['cool', 'awesome', 'ninja', 'hacker', 'gamer', 'wizard', 'master', 'savage', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generate_random_username():

    random_words = random.sample(usernames, k=random.randint(2, 3))

    random_number = random.randint(10, 4000)
    
    username = ''.join(random_words) + str(random_number)

    output_label.config(text=username)
    
root = Tk()

def button_clicked():
    generate_random_username()

