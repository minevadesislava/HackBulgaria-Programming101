import sys
from random import randint



def main():
    file = open(sys.argv[1], "w")
    list1= []
    for i in range(0,int(sys.argv[2])):
        number = randint(1, 1000)
        list1.append(str(number))
    file.write(" ".join(list1))



if __name__ == '__main__':
    main()