from audioop import mul


while True:
    a, b = list(map(int, input().split()))
    factor_chk = False
    multiple_chk = False
    if a < b:
        if b%a == 0:
            factor_chk = True
    elif a > b:
        if a%b == 0:
            multiple_chk = True
    if a == 0 and b == 0:
        break
    if factor_chk == False and multiple_chk == False:
        print("neither")
    elif factor_chk == True:
        print("factor")
    elif multiple_chk == True:
        print("multiple")
    