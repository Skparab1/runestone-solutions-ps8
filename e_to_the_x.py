import math

def eToX(x):
    i = 1
    s = 1
    term = 1
    while term > (1.0e-12):
        term = term * (x/i)
        s = s + term
        print('n:',i,'\t\tterm:',term,'\t\tsum:',(s))
        i += 1
        
    return s

def main():
    print(eToX(2))

if __name__ == "__main__":
    main()

