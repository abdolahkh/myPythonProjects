# By : Abdolah Khoshkalam
# this program recives your name or text and writes it with stars(*).
# GitHub: https://github.com/abdolahkh
# -----------------------------------------
# Difination of letters with stars
a = ["       **", "      ****", "     **  **", "    **    **", "   ** *  * **", "  **        **", " **          **"]
b = [" * * *", " **   **", " **    **", " ** * *", " **    **", " **     **", " ** *  **"]
c = [" *********", " **      *", " **       ", " **       ", " **       ",  " *********"]
d = [" *******", " **     **", " **     **", " **     **" , " **     **", " *******"]
e = ["        ", " *******", " **", " *******", " **"," *******"]
f = [" *******", " **    *"," **", " *******"," **"," **",]
g = [" *******", " **", " **"," **   ***"," **     *"," *******"]
h = [" **    **", " **    **", " ********"," **    **"," **    **"," **    **"]
i = [" ******", "   **", "   **","   **","   **"," ******"]
j = [" ****", "   **", "   **","   **","   **"," ***"]
k = [" **   **", " **  **", " *****"," **  **"," **   **"," **   ***"]
l = [" **", " **", " **"," **"," **"," ********"]
m = [" **          **", " ****      ****", " ** **    ** **"," **  **  **  **"," **   ****   **"," **    **    **"]
n = [" **    **", " ****  **", " ** ** **"," **  ****"," **   ***"," **    **"]
o = ["  ******", " **    **", " **    **"," **    **"," **    **","  ******"]
p = [" *******", " **    **", " **    **"," *******"," **"," **"]
q = ["  ********", " **      **", " **      **"," **   *****"," **      **"," ******** ***"]
r = [" *******", " **    **", " **    **"," *******"," **    **"," **    ***"]
s = ["", "  ******", " **","  *****","      **"," ******"]
t = [" ********", "    **", "    **","    **","    **","    **"]
u = [" **     **", " **     **", " **     **"," **     **"," **     **","  *******"]
v = [" ***         ***", "   **       **", "    **     **","     **   **","      ** **","       ***"]
w = ["", "  **       **       **", "   **     ****     **","    **   **  **   **","     ** **    ** **","      ***      ***"]
x = ["  **    **", "   **  **", "    ****","   **  **","  **    **", " **      **"]
y = [" **      **", "  **    **", "    ****","     **","     **","     **"]
z = ["", " ********", "      **","    **","  **"," ********"]

# -----------------------------------------
x = input("your name or text:").lower()     # This part recives your name or text.
y = ""                                      # Defination an empty string
for term in x:                              # Adding a space to letters for splitting stering
    y += term + ' '
z = y.split()
# -----------------------------------------
# output part
for term in z:                              
    for j in eval(term):                    # use eval for give meaning to letters.
        print(j)
    print()