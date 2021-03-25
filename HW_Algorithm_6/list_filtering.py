# in this kata you will create a function that takes a list of non-negative integers and
# strings and returns a new list with the strings filtered out.

# ex : filter_list([1,2,'a','b']) == [1,2] , filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l):
    # option-1
    new_list = []
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list
    
    # option-2
    # return [x for x in l if type(x) is not str]

print(filter_list([1,2,'aasf','1','123',123]))