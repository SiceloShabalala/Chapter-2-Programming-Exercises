# factorial.py
#   This program computes the factorial of a number
#   Illustrates fro loop with an accumulator

def main():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact *= factor
    print("The factorial of",n,"is",fact)

main()