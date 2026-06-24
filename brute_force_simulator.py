import itertools
import string

target_password = "abc"

characters = string.ascii_lowercase

attempts = 0

for length in range(1, 4):

    for guess in itertools.product(characters, repeat=length):

        attempts += 1

        guess = ''.join(guess)

        if guess == target_password:

            print("Password Found:", guess)
            print("Attempts:", attempts)
            exit()