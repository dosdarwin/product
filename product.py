product =[]
while True:
	name = input('please type the product you buy:')
	if name == 'q':
		break
	p = []
	price = input('please type the price of the product you buy:') 
	p.append(name)
	p.append(price)
	product.append(p)
print(product)