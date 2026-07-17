#Challenge: The smart ATM Withdrawal Simulator
#Setting a fixed variable representing a bank balance
balance = 16500000

#Asking how much the user wants to withdraw
withdrawal_amount = int(input("Enter the amount you want to withdraw: "))

#if request is less or equal to the balance, deduct amoutn and print
if withdrawal_amount <= 0:
    print("Invalid amount. Please enter an amount greater than R0.")

elif withdrawal_amount <= balance:
    balance = balance - withdrawal_amount
    print(f"Withdrawal successful! Remaining balance: R{balance}")

else:
    print("Declined. Insufficient funds.")
