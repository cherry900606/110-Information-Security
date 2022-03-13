
def encryptRailFence(text, key):
 
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix
    # to distinguish filled
    # spaces from blank ones
    rail = [['\n' for i in range(len(text))]
                  for j in range(key)]
     
    # to find the direction
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
         
        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1
         
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))

def railFance(p, k):
    res = ""
    p.upper()

    go_down = False
    row, col = 0, 0

    railList = [['\n' for i in range(len(p))]for j in range(k)]

    for i in range(len(p)):
         
        if (row == 0) or (row == k - 1):
            go_down = not go_down
         
        railList[row][col] = p[i]
        col += 1
         
        if go_down:
            row += 1
        else:
            row -= 1
    
    for i in range(k):
        for j in range(len(p)):
            if railList[i][j] != '\n':
                res = res + railList[i][j]

    return(res)



    




print(railFance("meetmeafterthetogaparty", 2))
