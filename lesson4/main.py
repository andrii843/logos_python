# Task 4

# input_string = input("Enter data: ")
input_string = 'I canT DAnCE i CANt TAlK Hey'
key = 'aaaaabbbbbabbbaabbababbaaababaab'
abc = 'abcdefghijklmnopqrstuvwxyz'

def parse (string) :
	result = ''
	list_key = string_step3.split(' ')
	for s in list_key :
		result += abc[key.find(s)]
	return result

print("\nEncoded text: {}".format(input_string))
string = input_string.replace(' ', '')

string_step2 = ''
i = 0
while i < len(string) // 5:
	string_step2 += string[5*i:5*(i+1)] + ' '
	i += 1
string_step2 = string_step2[:-1]

string_step3 = ''
for s in string_step2 :
	if s == ' ' :
		string_step3 += ' '
	elif s.islower() :
		string_step3 += 'a'
	else :
		string_step3 += 'b'

print('Result: {}\n'.format(parse(string_step3)))

# Additional
def check(string) :
	i = 0
	end = len(string)-1
	for s in string :
		if s != string[end-i] :
			return False
		i += 1
	return True

if check(input("Enter some text to check if it is palindrome: ")) :
	print('Answer: Yes')
else :
	print('Answer: No')