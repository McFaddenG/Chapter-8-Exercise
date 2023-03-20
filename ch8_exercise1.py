#Removes the first and last elements of a list
def chop(fl):
    if len(fl) > 2:
        del fl[0]
        del fl[-1]

#Returns a new list containing all but the first and last elements
def middle(fl):
    if len(fl) > 2:
        return fl[1:-1]
    else:
        return []
        
fl =  [1, 2, 3, 4, 5, 6]
print("Original List: ", fl)

chop(fl)
nl = middle(fl)
print("Modified List: ", nl)
