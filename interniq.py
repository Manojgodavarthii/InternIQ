# -*- coding: utf-8 -*-
"""interniq.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W3tKs521947b6V183NsJn38vwM03YRUG
"""

import hmac
import hashlib
import time

# Function to generate an OTP using a secret key and a counter
def generate_otp(secret_key, counter):
    key = base32_decode(secret_key)
    counter_bytes = counter.to_bytes(8, byteorder='big')

    # Use HMAC-SHA1 to generate the OTP
    h = hmac.new(key, counter_bytes, hashlib.sha1)
    digest = h.digest()

    # Extract the OTP from the digest
    offset = digest[-1] & 0x0F
    otp = ((digest[offset] & 0x7F) << 24 |
           (digest[offset + 1] & 0xFF) << 16 |
           (digest[offset + 2] & 0xFF) << 8 |
           (digest[offset + 3] & 0xFF))

    otp = otp % 10 ** 6  # 6-digit OTP
    return str(otp).zfill(6)

# Function to verify an OTP
def verify_otp(secret_key, user_otp):
    # To account for time-based OTPs, you may need to adjust the counter based on the current time
    counter = int(time.time()) // 30  # A typical time step for TOTP is 30 seconds
    for i in range(-1, 2):  # Check the current counter and the previous two counters
        otp = generate_otp(secret_key, counter + i)
        if otp == user_otp:
            return True
    return False

# Helper function to decode base32-encoded keys
def base32_decode(secret_key):
    import base64
    import struct

    key = base64.b32decode(secret_key, casefold=True)
    return struct.pack("16B", *key)

if __name__ == "__main__":
    # Generate a secret key for the user (keep this secret)
    user_secret_key = "JBSWY3DPEHPK3PXP"

    # Generate an OTP
    generated_otp = generate_otp(user_secret_key, int(time.time()) // 30)
    print(f"Generated OTP: {generated_otp}")

    # Simulate user input
    user_input_otp = input("Enter the OTP: ")

    # Verify the OTP
    if verify_otp(user_secret_key, user_input_otp):
        print("OTP is valid. Access granted.")
    else:
        print("OTP is invalid. Access denied.")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# In-memory user data for demonstration
users = []

def register(username, password):
    for user in users:
        if user.username == username:
            return "Username already exists. Please choose another."

    new_user = User(username, password)
    users.append(new_user)
    return "Registration successful."

def login(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return "Sign-in successful."

    return "Incorrect username or password."

if __name__ == '__main__':
    while True:
        print("1. Register")
        print("2. Sign-In")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            result = register(username, password)
            print(result)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            result = login(username, password)
            print(result)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

import time

class Stopwatch:
    def __init__(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time

    def end(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def manual_stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def display_time(self):
        if self.running:
            current_time = time.time() - self.start_time
        else:
            current_time = self.elapsed_time

        mins, secs = divmod(current_time, 60)
        hours, mins = divmod(mins, 60)
        return f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}"

def main():
    stopwatch = Stopwatch()

    while True:
        print("1. Start")
        print("2. End")
        print("3. Manual Stop")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            stopwatch.start()
        elif choice == "2":
            stopwatch.end()
        elif choice == "3":
            stopwatch.manual_stop()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

        print(f"Elapsed time: {stopwatch.display_time()}")

if __name__ == "__main__":
    main()

import time

class Stopwatch:
    def __init__(self):
        self.running = False
        self.start_time = 0

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()

    def display_time(self):
        current_time = time.time() - self.start_time
        mins, secs = divmod(current_time, 60)
        hours, mins = divmod(mins, 60)
        return f"{int(hours):02d}:{int(mins):02d}:{int(secs):02.2f}"

def main():
    stopwatch = Stopwatch()

    while True:
        print("1. Start")
        print("2. Display Time")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            stopwatch.start()
        elif choice == "2":
            if stopwatch.running:
                print(f"Running time: {stopwatch.display_time()}")
            else:
                print("Stopwatch is not running.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import random

def get_user_choice():
  """Prompt the user to choose rock, paper, or scissors."""
  choices = ['rock', 'paper', 'scissors']
  print('Choose rock, paper, or scissors:')
  user_choice = input()
  while user_choice not in choices:
    print('Invalid choice! Please choose rock, paper, or scissors:')
    user_choice = input()
  return user_choice

def get_computer_choice():
  """Generate a random choice (rock, paper, or scissors) for the computer."""
  return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
  """Determine the winner based on the user's choice and the computer's choice."""
  if user_choice == computer_choice:
    return 'tie'
  elif (user_choice == 'rock' and computer_choice == 'scissors') or \
      (user_choice == 'paper' and computer_choice == 'rock') or \
      (user_choice == 'scissors' and computer_choice == 'paper'):
    return 'user'
  else:
    return 'computer'

def display_result(user_choice, computer_choice, winner):
  """Show the user's choice, the computer's choice, and the result."""
  print('Your choice:', user_choice)
  print('Computer choice:', computer_choice)
  if winner == 'tie':
    print('It\'s a tie!')
  elif winner == 'user':
    print('You win!')
  else:
    print('Computer wins!')

def play_again():
  """Ask the user if they want to play another round."""
  print('Do you want to play again? (y/n)')
  play_again = input()
  return play_again == 'y'


def main():
  while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)
    if not play_again():
      break


if __name__ == '__main__':
  main()