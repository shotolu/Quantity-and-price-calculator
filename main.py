product_price_1=input('what is the price of product 1')
quantity_product_1=input('what is the quantity of product 1')
product_price_2=input('what is the price of product 2')
quantity_product_2=input('what is the quantity of product 1')
product_price_3=input('what is the price of product 3')
quantity_product_3=input('what is the quantity of product 3')

result_product_1=float(product_price_1)*float(quantity_product_1)
result_product_2=float(product_price_2)*float(quantity_product_2)
result_product_3=float(product_price_3)*float(quantity_product_3)

total_price=result_product_1+result_product_2+result_product_3

print('Your total price is ' + str(total_price))