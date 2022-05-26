# By : Abdolah Khoshkalam
# this program recive a text and a string from you and search that in the text.
# GitHub: https://github.com/abdolahkh
# -----------------------------------------
def Search(y, x):                                           # Search function
    l = len(x)                                              # length of search string
    for i in range(len(y)):                                 # for loop from zero to length of text
        c = 0                                               # count variable
        emp = []                                            # an empty list for text parsing
        while c < len(y) - len(x) + 1:                      # use from while loop
            s = y[c: c + len(x)]                            # macking string's from text
            emp.append(s)                                   # adding string to rmpty list
            c += 1                                          # adding one to count
    if x in emp:                                            # searching part(search in the list of strings)
        return emp, True                                    # return the results
    return False                                            # else
# -----------------------------------------
def Position(y, x):                                         # findding position of string in the text
    print("You are intered : ", y)                          # print reciving text
    strs, res = Search(y, x)                                # use from Search function
    if res == True:                                         # cheching result of searching
        c = 0                                               # count variable
        num = 0                                             # number of search counter
        for i in strs:                                      # search string in list of strings
            c += 1                                          # adding one to counter
            if i == x:                                      # cheching result with reciving string
                num += 1                                    # adding one to counter
                print(f"{num} : ", end = '')                # print output part
                print(f"from {c} to {c + len(x) - 1}")

#input part
y = input("inter the text here: ")                          
x = input("what you need to shearch it in the text? ")

#shaow results
print(Search(y, x)[1])
Position(y, x)