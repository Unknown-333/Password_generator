import random
import string

def generate_password(words, length):
    
    combined_words = "".join(words)

    
    remaining_length = max(0, length - len(combined_words))
   
    
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length))

    
    password = combined_words + random_chars

    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def main():
    print("Welcome to the Password Generator!")

    
    words_input = input("Enter words separated by spaces: ").strip()
    words = words_input.split()

    password_length = int(input("Enter the desired length of the password: "))

    generated_password = generate_password(words, password_length)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()