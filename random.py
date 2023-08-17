import random

def main():
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    print(f"Generated random number: {random_number}")

    if random_number % 2 == 0:
        print("The random number is even.")
    else:
        print("The random number is odd.")

if __name__ == "__main__":
    main()
