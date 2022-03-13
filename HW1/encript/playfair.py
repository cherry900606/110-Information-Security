

def findID(l, matrix):
    for i in range (5):
        for j in range(5):
            if l == matrix[i][j]:
                return (i, j)

def playfair(p, k):
    matrix = [[0 for x in range(5)] for y in range(5)] 
    res = ""
    cnt = 0

    p = p.upper()
    k = k.upper()

    ## create key matrix ##
    duplicate_letter = []
    for i in k:
        if i not in duplicate_letter:
            duplicate_letter.append(i)
            matrix[cnt // 5][cnt % 5] = i
            cnt += 1
        else:
            continue
    
    
    for i in range(65,90):
        if chr(i) == 'J': 
                continue
        if chr(i) not in duplicate_letter:
            matrix[cnt // 5][cnt % 5] = chr(i)
            cnt += 1

    ## plaintext preprocess ##
    p = p.replace(' ', '')

    cnt = 0
    while (cnt < len(p)):
        l1 = p[cnt]
        if cnt == len(p) - 1:
            p = p + 'X'
            cnt += 2
            continue
        l2 = p[cnt+1]
        if l1 == l2:
            p = p[:cnt + 1] + "X" + p[cnt + 1:]
        cnt += 2

    ## encode ##
    for (l1, l2) in zip(p[0::2], p[1::2]):
        row1, col1 = findID(l1, matrix)
        row2, col2 = findID(l2, matrix)
        if row1 == row2:
            res += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1==col2:# Rule 3, the letters are in the same column
            res += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else: #Rule 4, the letters are in a different row and column
            res += matrix[row1][col2] + matrix[row2][col1] 

    print(res)

playfair("Hello", "abcd")
 