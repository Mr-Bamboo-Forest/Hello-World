import string
from time import sleep

def cool():
    target = "Hello World!"
    print("Hello World:\n")  # Initial heading

    result = ""  # Holds the progressively built string

    for char in target:
        for letter in (string.ascii_letters + " !"):  # Include space and exclamation mark
            current_guess = result + letter
            print(current_guess)  # Print each guess on a new line
            sleep(0.015)

            if letter == char:  # Stop when the correct letter is found
                result += letter
                break  

    print("\nFinal output:", result)  # Display final result at the end

cool()
