while True:
    N = int(input())
    check_a = check_b = False
    result_a = result_b = 0
    a = N//5
    for i in range(a,0,-1):
        result = N-i*5
        if result%3 == 0:
            if result_a < i+result//3:
                result_a = i+result//3
                check_a = True
                break
            
    b = N//3
    for i in range(b,0,-1):
        result = N-i*3
        if result%5 == 0:
            if result_b < i+result//5:
                result_b = i+result//5
                check_b = True
                break

    if check_a == False and check_b == False:
        print(-1)
    else:
        if result_a != 0 and result_b != 0:    
            if result_a <= result_b:
                print(result_a)
            else:
                print(result_b)
        elif result_a != 0 and result_b == 0:
            print(result_a)
        elif result_a == 0 and result_b != 0:
            print(result_b)
        else:
            print(-1)

        
