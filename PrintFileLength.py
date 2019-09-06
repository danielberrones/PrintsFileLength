## Reads the contents of a file in Terminal
## Created by Daniel Berrones

from sys import argv
filename = argv[1]

def main():
	f = open(filename,"r")
	data = f.read()
	length = len(data)
	print("\n\n************************************************")
	print(f"\tCONTENTS OF FILE: {filename}")
	print("************************************************")
	print("\n\n",data)
	print("\n************************************************")
	print("************* FILE LENGTH: {}".format(length), "*************")
	print("************************************************")

if __name__ == "__main__":
	main()
