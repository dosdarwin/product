
def input_product():
	product = []
	while True:
		name = input('please type the product you buy:')
		if name == 'q':
			break
		p = []
		price = input('please type the price of the product you buy:') 
		product.append([name, price])
	return product

def print_product(product):
	for p in product:
		print(p[0], 'cost is', p[1])

def open_file(filename,product):
	with open(filename, 'w') as f:
		f.write('商品,價格\n')
		for p in product: 
			f.write(p[0] + ',' + p[1] + '\n')
			return product
			return filename

def read_file(filename):
	import os
	pro2=[]
	if os.path.isfile(filename):
		print('yeah!, find the file!')
		with open(filename, 'r') as r:
			for d in r:
				if '商品,價格' in d:
					continue
				name,price = d.strip().split(',')
				pro2.append([name,price])
	else:
		print('cannot find the file......')
	print(pro2)
	return pro2

product = input_product()
print_product(product)
open_file('product.csv', product)
read_file('product.csv')