#
# Author: Alan Ma
# A program to convert Celsius temps to Fahrenheit

def main():
	celsius = input("What is the Celsius temperature? ")
	fah = ( 9.0 / 5.0) * float(celsius) + 32
	print ("The temperature is", fah ," degress Fahrenheit.")
	
main()