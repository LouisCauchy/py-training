def process(lst):
	dct = {}
	for i in lst:
		if i in dct:
			dct[i] += 1
		else:
			dct[i] = 1
	return dct

def main():
	lst = input("Enter values:").split(',')
	print(process(lst))
	
main()