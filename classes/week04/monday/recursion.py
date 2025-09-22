def myPrint(n):
    
    print("hello", n)   
    if n == 5: return 'done'    
    myPrint(n + 1)

print(myPrint(1))

#prints sum of numbers from 1 to n; 5 + 5, 5 + 5-1, 5+4-1, and so on
def recur_sum(n):
    if n == 0: 
        return 0 
    else:
        return n + recur_sum(n - 1)

print(recur_sum(5))


    
    

    