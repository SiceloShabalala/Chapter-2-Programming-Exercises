# convertV_1.py
#   A program to convert Fahrenheit temperatures to Celscius
#   by: Sicelokuhle Siyabonga Shabalala

def main():
    # Introduction
    print("This is a simple program that converts")
    print("Celsius temperature to Fahrenheit temperature")
    print()

    # Input
    fahrenheit = eval(input("Enter a temperature in degrees Fahrenheit: "))

    # Process
    celsius = 5/9 * (fahrenheit - 32)
    
    # Output
    print("The eqivalent temperature in degrees celscius is",celsius)

main()