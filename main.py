#!/usr/bin/python3

# import all nececery modules
import random
import os
from art import logo,vs_logo
from game_data import data

# Display the logo 
def generate_opponents():
    opponent = random.choice(data)
    name = opponent["name"]
    follower = opponent["follower_count"]
    description = opponent["description"]
    country = opponent["country"]
    return [name, follower, description, country]

def clear_the_screen():
    os.system("clear")
    print(logo)
clear_the_screen()

def game_generator():
    opponent_a = generate_opponents()
    game_over = False
    correct_answer = "b"
    score = 0
    while not game_over:
        opponent_b = generate_opponents()
        if opponent_b != opponent_a:
            print(f"Compare A: {opponent_a[0]}, {opponent_a[2]}, {opponent_a[3]}.")
            print(vs_logo)
            print(f"Compare B: {opponent_b[0]}, {opponent_b[2]}, {opponent_b[3]}.")
            answer = input("Who has more followers? type 'A' or 'B': ").lower()
            if opponent_a[1] > opponent_b[1]:
                correct_answer = "a"
            if answer == correct_answer:
                score += 1
                clear_the_screen()
                print(f"You're right! current score: {score}")
                opponent_a = opponent_b
            else:
                game_over = True
                clear_the_screen()
                print(f"Sorry, that's wrong. Final score: {score}")

# compare between the correct answer and the player answer

game_generator()







