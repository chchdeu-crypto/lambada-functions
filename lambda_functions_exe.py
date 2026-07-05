#mission 1
manager_son_price=lambda price,son_of_m : price*0.8 if son_of_m==True else price*1.17

#mission 2
finel_price=lambda price,discount:price-discount

#mission 3
full_name= lambda f_name,l_name: f"{f_name} {l_name}"

#mission 4
grade_status= lambda grade : "pass" if grade>=55 else "fail"
print(grade_status(80))
print(grade_status(40))