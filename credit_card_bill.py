
def creditCardBill(rate, balance, payment):
    month = 0
    while balance > payment:
        month += 1
        balance = balance * (1+(rate/100))
        balance = balance - payment
        paymentsum = payment*month
        print('Month:',month,'\tbalance:',round(balance,10),'\ttotal payments:',paymentsum)
    
    month += 1
    
    balance = balance*(1+(rate/100))
    
    paymentsum = paymentsum + balance
    balance = 0
    print('Month:',month,'\tbalance:',round(balance,1),'\ttotal payments:',paymentsum)
    
def main():
    creditCardBill(1.5, 1000.0, 100.0)

if __name__ == "__main__":
    main()

