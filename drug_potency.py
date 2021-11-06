def drugPotency(loss, expire):
    potency = 100
    oldpotency = 100
    months = 0
    while oldpotency >= expire:
        oldpotency = potency
        print('Month:',months,'\teffectiveness:',potency)
        potency = potency - ((loss/100)*potency)
        months += 1
    
def main():
    drugPotency(4.0, 50.0)

if __name__ == "__main__":
    main()

