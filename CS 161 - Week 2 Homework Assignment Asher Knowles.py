#Part 1

#1

#set variable
x=31
#print bin and hex

print(x, bin(x), hex(x))

#2

#set variable
#x=1.825
#Issue with 1.825: A decimal number is a float and cannot be an int and only ints can be converted to bin or hex

x=18
#attempt print
print(x, bin(x), hex(x))

#3

#set variables
y=0b1011
z=0xA3
#print
print(y,z)

#4

#set variable
w=y+z+x
#print
print("The sum of x,y,and z is", w)


#Part 2 Compression

#set variables

original_size = 240
dictionary_size = 25
compressed_text_size = 148
#make formulas

percent_of_compression_float = 1-((compressed_text_size+dictionary_size)/original_size)
percent_of_compression_percent=percent_of_compression_float*100
percent_of_compression_percent_string=f"{percent_of_compression_percent:.2f}%"

total_size=dictionary_size+compressed_text_size

#print
print(' 	Compressed text size:', str(compressed_text_size), 'characters')
print(' 	Dictionary size:', str(dictionary_size), 'characters')
print(' 	Tottal size:', str(total_size), 'characters')
print(' 	Original text size:', str(original_size), 'characters')
print(' 	Compression:', percent_of_compression_percent_string)

