import time
import random


if __name__ == "__main__":
  print("Hi, I'm DeepSeek. How can I help you today?")
  while(1):
    user_input = input()
    time.sleep(random.randint(3, 6))
    print("The server is busy. Please try again later.")

