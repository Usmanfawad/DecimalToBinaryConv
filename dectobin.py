user= int(input("Enter dec:    "))
rem_lst=[]
while user!=0:
    inte=user//2
    user=inte
    rem=user%2
    rem_lst.append(str(rem))

x= ''.join(rem_lst)
print(x)
    

    
