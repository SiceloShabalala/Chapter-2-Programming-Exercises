# convert.py
#   A program to convert Celsius temps to Fahrenheit
#   by: Sicelokuhle Siyabonga Shabalala

def main():

    # Introduction
    print("This is a simple program that computes and prints a table of")
    print("Celsius temperature and the Fahrenheit temperature equivalents")
    print("every 10 degrees from 0 degrees celscius to 100 degrees celscius.")
    print()

    print("______________________")
    print("Celscius   |Fahrenheit")
    print("______________________")
    for celsius in range(0,101):
        # Input
        #celsius = eval(input("What is the Celsius temperature? "))
    
        # Process
        if(celsius%10==0):
            fahrenheit = 9/5 * celsius + 32

            if(celsius==0):
                print(celsius,fahrenheit,sep="          |")
            elif(celsius==100):
                print(celsius,fahrenheit,sep="        |")
            else:
                print(celsius,fahrenheit,sep="         |")
        # Output
        #print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        #print()\
    print("______________________")
main()