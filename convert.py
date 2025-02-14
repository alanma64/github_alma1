#
# Author: Alan Ma
# Firsst edit: 1/Feb/2025
# Last edit:   2/Feb/2025
# A program to convert Celsius temps to Fahrenheit

def main():
	celsius = input("What is the Celsius temperature? ")
	fah = ( 9.0 / 5.0) * float(celsius) + 32
	print ("The temperature is", fah ," degress Fahrenheit.")
	
main()