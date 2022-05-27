# By : Abdolah Khoshkalam
# this program recives number of rows and made a triangle with stars.
# GitHub: https://github.com/abdolahkh
# -----------------------------------------
n = int(input("nuber of rows : "))     # number of rows
c = n                                  # counter of spaces

for i in range(n+1):
	for j in range(i):
		print('*',end = ' ')
	x = ' ' * c
	c -= 1
	print('\n',x, end = '')