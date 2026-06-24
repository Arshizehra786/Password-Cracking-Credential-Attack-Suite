import os

def generate_dictionary(name, dob):
    words = []

    words.append(name)
    words.append(name + dob)

    words.append(name.capitalize())
    words.append(name + "123")
    words.append(name + "@123")

    os.makedirs("data", exist_ok=True)
    with open("data/generated_wordlist.txt", "w") as f:
        for word in words:
            f.write(word + "\n")

    print("Wordlist Generated Successfully")


if __name__ == "__main__":
    generate_dictionary("arshi", "2000")