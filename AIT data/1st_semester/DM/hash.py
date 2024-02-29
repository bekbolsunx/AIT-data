    #Hash function which works with STRING

def hash_function(input):
    hash = 0 
    alpB = ['A', 'B', 'C', 'D', 'E']
    alpS = ['a', 'b', 'c', 'd', 'e']
    for i in input:
        for j , k in enumerate(alpB):
            if i==k or alpS[j]==i:
                hash += (j+1) * 7 - 1
    return hash 

input_string = "AbcE"
result = hash_function(input_string)
print(result)
    