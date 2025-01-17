#!/usr/bin/env python3
from decimal import Decimal
from decimal import ROUND_HALF_UP

# Calculates values
def get_interest_rate(amount, interest_rate):
    loan_amount_rounded = amount.quantize(Decimal("0.01"), ROUND_HALF_UP)
    interest_rate_rounded = interest_rate.quantize(Decimal("0.01"), ROUND_HALF_UP)
    print(f"{'Loan amount:':16} ${amount}")
    print(f"{'Interest rate:':16} {interest_rate:10,}%")
        

    interest_amount = (amount * interest_rate) / 100
    interest_amount = interest_amount.quantize(Decimal("0.01"), ROUND_HALF_UP)        
    print(f"{'Interest amount:':16} ${interest_amount:10,}")
    print()

def main():
    print("Interest Calculator")
    print()

    # Loops project until the user breaks
    while True:
        loan_amount = Decimal(input("Enter loan amount:   "))
        interest_rate = Decimal(input("Enter interest rate: "))
        print()
        
        get_interest_rate(loan_amount, interest_rate)
        
        continue_message = input("Continue? (y/n): ")
        print()
        if continue_message.lower() == "n":
            break
        elif continue_message.lower() == "y":
            continue
            
    print("Bye!")

if __name__ == "__main__":
    main()
