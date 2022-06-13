
def while_check(data):
    i = 0
    while data:
        print(i,"번")
        if data[i] == 1:
            return data[i]
        else:
            i += 1
        
data = [4,5,1,6,7]
print(while_check(data))
