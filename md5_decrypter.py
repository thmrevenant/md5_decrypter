import hashlib
import itertools
import string

def md5_crack(md5_hash, start_str, end_str, length):
    chars = string.ascii_letters + string.digits + string.punctuation  # Zeichenraum (Buchstaben + Zahlen + Sonderzeichen)
    attempt_counter = 0
    
    for mid_part in itertools.product(chars, repeat=length):
        attempt_counter += 1
        candidate = start_str + ''.join(mid_part) + end_str
        generated_hash = hashlib.md5(candidate.encode()).hexdigest()
        print(f"[{attempt_counter}] Testing: {candidate}")
        
        if generated_hash == md5_hash:
            print(f"Match found! Password: {candidate}")
            return candidate
    
    print("No match found.")
    return None

if __name__ == "__main__":
    md5_hash = input("Enter MD5 hash to crack: ").strip()
    start_str = input("Enter the starting string: ").strip()
    end_str = input("Enter the ending string: ").strip()
    length = int(input("Enter the number of characters between start and end: "))
    
    md5_crack(md5_hash, start_str, end_str, length)
