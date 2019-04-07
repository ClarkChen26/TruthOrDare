import random 
import sys
import re
import codecs
def main():
    with open(sys.argv[1], encoding = 'utf-8') as f:
        name_list = f.readlines()
        result = random.choice(name_list)
        print(result)    
if __name__ == "__main__":
    main()