#Task 5

# 1
def get_unique(arr) :
	unique = []
	for val in arr :
		flag = True
		for val_un in unique :
			if val == val_un and type(val) == type(val_un) :
				flag = False
		if flag :
			unique.append(val)

	return unique

vals = [1, 3, 3.0, '3', 3.0, '3', '3.0', 1]
print("Input:  {}\nUnique: {}\n".format(vals, get_unique(vals)))

# 2
def getCountDigits(a, b) :
	count = 0
	for digit in str(b) :
		if str(a).find(digit) != -1 :
			count += 1

	return count

a = int(input("Enter a: "))
b = int(input("Enter b: "))
count = getCountDigits(a, b)
print("a = {}\nb = {}\nCount = {}".format(a, b, count))