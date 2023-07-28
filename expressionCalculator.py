# expressionCalculator.py
""" This is an interactive Pytyhon calculator, it takjea MATHEMATHICAL EXPRESSIONS from a user
    and then prints out the value. The progra, contaiins a for loop for the user to enter
    expression mutiple times
    To quit early, the user can crash the program by typing a bad expression or closing the window
    that the calculator program is running in
    @author: Sicelokuhle Siyabonga Shabalala
    @date: 21/07/2023
"""

def main():
    # Introduction
    print("This program allows a user to type a mathematical expression, and then prints the value")
    print("of the expression")
    print()

    # Input Process

    for i in range(101):
        mathExpression = eval(input("Enter a mathematical expression to evaluate: "))
        
        # Output
        print("The value of the mathematical expression is", mathExpression)
        
main()