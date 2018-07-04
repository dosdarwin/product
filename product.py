product =[]
while True:
	name = input('please type the product you buy:')
	if name == 'q':
		break
	p = []
	price = input('please type the price of the product you buy:') 
	product.append([name, price])
for p in product:
	print(p[0], 'cost is', p[1])