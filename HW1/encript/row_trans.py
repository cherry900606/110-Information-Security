
def row_trans(p, k):
    res = ""
    lp = len(p)
    lk = len(k)
    width = lk
    height = (lp // lk) if (lp % lk == 0) else (lp // lk + 1)
    matrix = [[0 for x in range(width)] for y in range(height)] 

    ## construct matrix ##
    cnt = 0
    for i in p:
        matrix[cnt // width][cnt % width] = i
        cnt += 1

    ## ciphertext ##
    for i in range(1, len(k) + 1):
        id = k.index(str(i))
        print(id)
        for j in range(height):
            if matrix[j][id] != 0:
                res = res + matrix[j][id]
    
    print(res)
    return res


row_trans("attackpostponeduntiltwoamxyz", "4312567")

# attackpostponeduntiltwoamxyz