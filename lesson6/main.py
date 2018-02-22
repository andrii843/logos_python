# Task 6
import sys, os

directory_in = 'doil'
filename = sys.argv[1]
directory_out = 'result'

words_res = {}
with open(directory_in + '/' + filename, 'r', encoding='utf-8') as f :
	lines = f.readlines()
	for line in lines :
		if line.isspace() :
			continue
		words = line.strip().split(' ')		
		for word in words :
			if word in words_res :
				words_res[word] += 1
			else :
				words_res[word] = 1

char_count = 0
word_count = 0
chars_unique = set()

str_res = ''
for key, value in words_res.items() :
	char_count += len(key) * value
	word_count += value
	str_res += '{} - {}\n'.format(key, value)
	for char in key :
		chars_unique.add(char)

str_res_start = 'Count of words - {}\n'.format(word_count)
str_res_start += 'Count of chars - {}\n'.format(char_count)
str_res_start += 'Unique words - {}\n'.format(len(words_res.keys()))
str_res_start += 'Unique chars - {}\n\n'.format(len(chars_unique))

if not os.path.exists(directory_out):
    os.makedirs(directory_out)
with open(directory_out + '/' + filename, 'w', encoding='utf-8') as f :
	f.write(str_res_start + str_res)