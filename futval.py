# futval.py
#   A program to compute the value of an investment
#   carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of an n-year(s) investment.")
    print()

    # Input
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years: "))
    compInterPeriod = eval(input("Enter the number of yearly compunding interest periods: "))

    # Process
    apr = (apr/compInterPeriod)/100

    initalPrincipal = principal

    for i in range(years*compInterPeriod):
        principal = principal * (1 + apr)
        principal += initalPrincipal

    # Output
    print("The value in",years,"years is:",str(principal))

main()