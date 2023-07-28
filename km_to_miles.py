# km_to_miles.py
#   This program converts kilometers to miles
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 21/07/2023

def main():
    # Introduction
    print("This is a converter program that turns KILOMETERS to MILES!")
    print()

    # Input
    kilometer = eval(input("Enter a km distance to be converted to miles (exclude the units): "))

    # Process
    miles = 0.62 * kilometer

    # Output
    print(kilometer,"km","is",miles,"mi")

main()