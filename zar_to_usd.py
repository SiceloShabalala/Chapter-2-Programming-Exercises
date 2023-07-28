# zar_to_usd.py
#   This program is a currency conversion of the South African Rand to the United States Dollar on the 21/04/2023
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 21/04/2023
#   This program has to be updated on a daily basis!!!

def main():
    # Introduction
    print("This is a asimple currency conversion of the South African Rand to the United States Dollar!")
    print()

    # Input
    zar = eval(input("Enter the amount of South African Rands to Convert: "))

    # Process
    usd = zar * 0.056

    # Output
    print("The  equvalent of",zar,"zar(s) is",usd,"usd(s)")

main()