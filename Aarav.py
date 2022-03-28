'''
    PROBLEM STATEMENT
    Pooja would like to withdraw X $US from an ATM.
    The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges).
    For each successful withdrawal the bank charges 0.50 $US.
    Calculate Pooja's account balance after an attempted transaction.

    Input
    Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.
    Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance.

    Output
    Output the account balance after the attempted transaction, given as a number with two digits of precision.
    If there is not enough money in the account to complete the transaction, output the current bank balance.

    EXAMPLE
    A) Successful Transaction

     *****TERMS-AND-CONDITION*****
 1) Number shuld be greater then ZERO
 2) Number should be divisible by 5
 3) Maximum withydrawal Ammount is 2000
Enter the ammount : 1300

Number is greater then ZERO
Number is divisible by 5
Value is under the Limit

   *****ACCOUNT-STATUS*****
Balance 30 seconds back :  1500
Withdrawal Amount       :  1300
Currnt Balance          :  200

   *****THANK-YOU*****

    B) Incorrect Withdrawal Amount (not multiple of 5)

     *****TERMS-AND-CONDITION*****
 1) Number shuld be greater then ZERO
 2) Number should be divisible by 5
 3) Maximum withydrawal Ammount is 2000
Enter the ammount : 53

Number is greater then ZERO
Number is not divisible by 5

   *****THANK-YOU*****

    C) Insufficient Funds

*****TERMS-AND-CONDITION*****
 1) Number shuld be greater then ZERO
 2) Number should be divisible by 5
 3) Maximum withydrawal Ammount is 2000
Enter the ammount : 1500

Number is greater then ZERO
Number is divisible by 5
Value is under the Limit

   *****ACCOUNT-STATUS*****
Balance 30 seconds back :  1000
Withdrawal Amount       :  1500
Remark                  : Insufficient Balance

   *****THANK-YOU*****
'''
print(" Welcome to GGI bank ")
print(" Type (1) => Withdrawal \n Type (2) => Diposit")
ty = input(" Enter : ")
f = open("ATM.txt", "r")
b = f.read()
b = float(b)
if(ty == str("1")) :
    # Withdrawal
        print("   *****TERMS-AND-CONDITION***** \n 1) Number shuld be greater then ZERO \n 2) Number should be divisible by 5 \n 3) Maximum withydrawal Ammount is 2000 \n 4) Bank Charges is 0.5 US$")
        w = float(input("Enter the ammount : "))  # Withdrawal Amount
        print(" ")
        if (w > 0):
            print("Number is greater then ZERO")
            if (w % 5 == 0):
                print("Number is divisible by 5")
                if (w <= 2000):
                    bkc = 0.5
                    print("Value is under the Limit")
                    print(" ")
                    print("   *****ACCOUNT-STATUS*****")
                    print("Balance 30 seconds back : ", b)
                    print("Withdrawal Amount       : ", w)
                    if (w < b):
                        b = b - w - bkc
                        print("Bank Charges            : ", bkc)
                        print("Currnt Balance          : ", b)
                        f = open("ATM.txt", "w")
                        f.write(str(b))
                    else:
                        print("Remark                  : Insufficient Balance")
                    f.close()
                else:
                    print("Number is greater then 2000")
            else:
                print("Number is not divisible by 5")
        else:
            print("Please Enter the CORRECT number")
        print(" ")
        print("   *****THANK-YOU*****")
elif(ty == str("2")) :
    #Deposit
        print("   *****TERMS-AND-CONDITION***** \n 1) Number shuld be greater then 0 \n 2) Maximum diposit Ammount is 10000 \n ")
        d = float(input("Enter the ammount : "))  # Deposit ammount
        print(" ")
        if ((d > 0) & (d <= 10000)):
            b = b + d
            f = open("ATM.txt", "w")
            f.write(str(b))
            print("   *****ACCOUNT-STATUS*****")
            print("Diposit Amount       : ", d)
            print("Total Balance : ", b)
            print("   *****THANK-YOU*****")
            f.close()
        else:
            print("*****Please enter the correct value*****")
else :
    print("*****Please enter the correct option*****")




