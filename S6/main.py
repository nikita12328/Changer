import random
from main2 import ferz


def main():
    positions = list(range(1, 9))  
    for i in range(4):  
        random.shuffle(positions)  
        while not ferz(positions):  
            random.shuffle(positions)
        print(positions)  

if __name__ == '__main__':
    main()
