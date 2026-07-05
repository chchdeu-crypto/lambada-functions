#mission 1
manager_son_price=lambda price,son_of_m : price*0.8 if son_of_m==True else price*1.17

#mission 2
finel_price=lambda price,discount:price-discount
print(finel_price(150,30))
