# By : Abdolah Khoshkalam
# Bubble sorting methode
# GitHub: https://github.com/abdolahkh
# -----------------------------------------
def Sort(x, sortingShape):                          # sorting function
    for i in range(len(x)-1):                       # for loop from zero to (length of x) - 1
        for j in range(i, len(x)):                  # mack a hypothetical list
            if x[j] > x[j-1]:                       # compare tow adjancent numbers(if True?)
                x[j], x[j-1] = x[j-1], x[j]         # moving numbers 
    if sortingShape == 'l2g':                       # it is want from persons for shape of sort(if 'less to grate'?)
        return x[::-1]                              # invert the list
    elif sortingShape == 'g2l':                     # if 'less to grate'?
        return x
    return "error: just inter 'l2g' or 'g2l'."      # else part return an error

x = [2, 3, 5, 4, 1]                                 # a list for sorting
sortingShape = 'l2g'                                # shape of sorting
print(Sort(x, sortingShape))                        # use from 'Sort' function
