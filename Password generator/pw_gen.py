import random
import string

def generate_password(words, length):
    # Combine all the words provided by the user
    combined_words = "".join(words)

    # Calculate how many random characters and digits we need to complete the password
    remaining_length = max(0, length - len(combined_words))
   
    # Generate random characters and digits to complete the password
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length))

    # Combine the words and random characters
    password = combined_words + random_chars

    # Shuffle the password to make it harder to guess
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def password_strength(password):
    # Determine password strength based on criteria
    length_score = min(len(password) / 12, 1.0)
    uppercase_score = any(c.isupper() for c in password)
    digits_score = any(c.isdigit() for c in password)
    symbols_score = any(c in string.punctuation for c in password)

    strength_score = length_score + uppercase_score + digits_score + symbols_score
    if strength_score < 2:
        return "Weak"
    elif strength_score < 3:
        return "Moderate"
    else:
        return "Strong"

def main():
    print("Welcome to the Unique Password Generator!")
    words_input = input("Enter words separated by spaces: ").strip()
    words = words_input.split()

    password_length = int(input("Enter the desired length of the password: "))

    # Ask the user if they want to add a prefix or suffix to the password
    add_prefix = input("Do you want to add a prefix to the password? (y/n): ").lower() == 'y'
    add_suffix = input("Do you want to add a suffix to the password? (y/n): ").lower() == 'y'

    generated_password = generate_password(words, password_length)

    if add_prefix:
        prefix = input("Enter the prefix: ")
        generated_password = prefix + generated_password

    if add_suffix:
        suffix = input("Enter the suffix: ")
        generated_password += suffix

    print("\nGenerated Password:", generated_password)
    print("Password Strength:", password_strength(generated_password))

if __name__ == "__main__":
    main()