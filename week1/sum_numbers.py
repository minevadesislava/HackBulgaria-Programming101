import sys


def main():
	filename = "file.txt"
    f = open(argv[2], "r")
    sum = 0
    for line in f:
    	for word in line.split():
            sum +=  int(word)
    return sum

if __name__ == '__main__':
    main()