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

#mission 6
distance_from_10= lambda num : 10-num if num<=10 else num-10

#mission 7
item_total= lambda item:item["price"]*item["amount"]

#mission 8
shipping_cost=lambda whight,express : 50 if express and whight >5 else 30 if express else 25 if whight>5 else 10
print(shipping_cost(3,True))
print(shipping_cost(8,True))
print(shipping_cost(8,False))
print(shipping_cost(2,False))