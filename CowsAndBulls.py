import random
# Task: SLC-2 and SLC-3 - Implemented generate_number() and cows_and_bulls logic
def generate_number():
    digits = list("0123456789")
    random.shuffle(digits)
    if digits[0] == "0":  # avoid leading zero
        digits[0], digits[1] = digits[1], digits[0]
    return "".join(digits[:4])

def cows_and_bulls(secret, guess):
    cows = sum(secret[i] == guess[i] for i in range(4))
    bulls = sum((guess[i] in secret) and (guess[i] != secret[i]) for i in range(4))
    return cows, bulls
def main():
    print("Welcome to the Cows and Bulls Game!")
    secret_number = generate_number()
    attempts = 0
    guessed = set()  # <-- NEW: Track all previous guesses (SLC-7)

    while True:
        guess = input("Enter a 4-digit number: ")

        # NEW: Check for duplicate guesses
        if guess in guessed:
            print(" You already guessed this number, try a new one.")
            continue

        # Add current guess to the set
        guessed.add(guess)

        # Input validation (SLC-4)
        if not guess.isdigit() or len(guess) != 4:
            print("Invalid input. Please enter a 4-digit number.")
            continue

        attempts += 1  # SLC-5 Attempt Counter
        cows, bulls = cows_and_bulls(secret_number, guess)
        print(f"{cows} cows, {bulls} bulls")

        if cows == 4:
            print(f" You guessed {secret_number} in {attempts} attempts!")
            break

if __name__ == "__main__":
    main()
