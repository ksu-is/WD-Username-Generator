import random
from tkinter import *

usernames = ['cool', 'awesome', 'ninja', 'hacker', 'gamer', 'wizard', 'master', 'savage']

def generate_random_username():
    
    random_words = random.sample(usernames, k=random.randint(2, 3))
    
    random_number = random.randint(10, 4000)

    username = ''.join(random_words) + str(random_number)
    
    output_label.config(text=username)

root = Tk()

def button_clicked():
    generate_random_username()
