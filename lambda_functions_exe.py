#mission 1
manager_son_price=lambda price,son_of_m : price*0.8 if son_of_m==True else price*1.17

#mission 2
finel_price=lambda price,discount:price-discount

#mission 3
full_name= lambda f_name,l_name: f"{f_name} {l_name}"

#mission 4
grade_status= lambda grade : "pass" if grade>=55 else "fail"

#mission 5
large= lambda n1,n2 : n1 if n1>n2 or n1==n2 else n2
print(large(4,4))
print(large(5,4))
print(large(1,4))