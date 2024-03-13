import random

def is_even_or_odd():
    number = random.randint(1, 100)
    if number % 2 == 0:
        print(f"The generated number {number} is even.")
    else:
        print(f"The generated number {number} is odd.")

if __name__ == "__main__":
    is_even_or_odd()
