import random 
import sys

def main():
    with open('name') as f:
        name_list = f.read().splitlines()
        name = random.choice(name_list)
        print(name)    
if __name__ == "__main__":
    main()