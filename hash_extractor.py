import os


def identify_hash(hash_value):

    if hash_value.startswith("$6$"):
        return "SHA-512"

    elif len(hash_value) == 32:
        return "MD5"

    elif len(hash_value) == 40:
        return "SHA1"

    else:
        return "Unknown"


input_path = os.path.join("data", "hashes.txt")

if not os.path.exists(input_path):
    os.makedirs(os.path.dirname(input_path), exist_ok=True)
    with open(input_path, "w") as file:
        file.write("# Add one hash per line\n")
    print(f"Created missing input file: {input_path}")
    print("Please add hashes to this file and run the script again.")
else:
    with open(input_path, "r") as file:
        for line in file:
            hash_value = line.strip()
            if not hash_value or hash_value.startswith("#"):
                continue
            print(hash_value, "->", identify_hash(hash_value))