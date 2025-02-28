import itertools
import string
import hashlib

# Benutzerinput für den Hash
md5_hash = input("Gib den MD5-Hash ein: ")
start_string = input("Gib den Anfang des Strings ein (optional): ")

# Zeichen, die getestet werden sollen (alle möglichen Zeichen)
chars = string.printable.strip()

# Funktion zum Brute-Forcen
def brute_force_md5(target_hash, prefix=""):
    # Prüfe zuerst den mitgegebenen Anfangsstring
    if prefix:
        hashed_prefix = hashlib.md5(prefix.encode()).hexdigest()
        print(f"Test: {prefix}")
        if hashed_prefix == target_hash:
            print(f"MD5-Hash entschlüsselt: {prefix}")
            return prefix
    
    length = 1
    while True:
        for combination in itertools.product(chars, repeat=length):
            word = prefix + ''.join(combination)
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            print(f"Test: {word}")
            
            if hashed_word == target_hash:
                print(f"MD5-Hash entschlüsselt: {word}")
                return word
        length += 1

# Starte den Brute-Force-Prozess
brute_force_md5(md5_hash, start_string)
