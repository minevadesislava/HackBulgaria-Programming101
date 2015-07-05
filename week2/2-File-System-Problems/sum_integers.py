import sys

def sum_integers():
    file = open(sys.argv[1], "r")
    contents = file.read().split(" ")
    result = sum([int(x) for x in contents])
    file.close
    return result

if __name__ == '__main__':
    print(sum_integers())
