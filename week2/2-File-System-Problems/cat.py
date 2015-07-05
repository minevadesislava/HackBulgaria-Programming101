import sys

'''def read_file():
    if len(sys.argv) > 1:
    	filename= sys.argv[]
    	text_file=open(filename, "r")
    	text
    	texy_file.close()

    	return 
    else:
        print("Give me a file to read!")

if __name__=='__main__':
	print (read_file())
'''
import sys


def main():
	filename = "boilerplate.txt"
	file = open(filename, "r")
	content = file.read()
	print(content)
	file.close()

if __name__ == '__main__':
    main()