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
with open('product.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in product: 
		f.write(p[0] + ',' + p[1] + '\n')

pro2=[]
with open('product.csv', 'r') as r:
	for d in r:
		if '商品,價格' in d:
			continue
		name,price = d.strip().split(',')
		pro2.append([name,price])
print(pro2)