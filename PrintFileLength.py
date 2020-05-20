## Displays text file in Terminal 
## Created by Daniel Berrones [email: Daniel.A.Berrones@gmail.com]

from sys import argv
filename = argv[1]


def main():
	f = open(filename,"r")
	data = f.read()
	length = len(data)
	print(f"\tCONTENTS OF FILE: {filename}")
	print("************************************************")
	print("\n\n",data)
	print("\n************* FILE LENGTH: {}".format(length), "*************")
	print("************************************************\n")


if __name__ == "__main__":
	main()
