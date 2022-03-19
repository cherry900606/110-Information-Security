import sys
import numpy as np
import math

method = sys.argv[2]
input = sys.argv[4]
key = sys.argv[6]
output = ""

## 1. Caesar
def caesar_encryption(p,k):
  e = ""
  for i in p:
    if i.isupper():
      temp = 65 + ((ord(i) - 65 + k) % 26) 
      e = e + chr(temp)                              
    elif i.islower():
      temp = 97 + ((ord(i) - 97 + k) % 26)
      e = e + chr(temp)
    else:
      e = e + i 
  return e

## 2. Playfair
def findID(l, matrix):
    for i in range (5):
        for j in range(5):
            if l == matrix[i][j]:
                return (i, j)

def playfair_encryption(p, k):
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
    
    
    for i in range(65,91):
        if chr(i) == 'J': 
                continue
        if chr(i) not in duplicate_letter:
            matrix[cnt // 5][cnt % 5] = chr(i)
            cnt += 1
    
    # print(matrix)

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

    return res
######################################################################

## 3. Vernam
def vernam_encryption(p, k):
    res = ""
    p = p.upper()
    k = k.upper()

    pList = []
    kList = []

    ## plaintext to binary ##
    for i in p:
        pList.append(ord(i) - 65)
    
    ## key to binary ##
    tmpK = k
    while len(k) < len(p):
        k += tmpK
    
    for i in k:
        kList.append(ord(i) - 65)

    ## do xor ##
    for i in range(len(p)):
        res = res + chr((pList[i]^kList[i])+65)
    
    return res

## 4. RailFence
def railFence_encryption(p, k):
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

## 5. Row Transformation
def row_trans_encryption(p, k):
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
        # print(id)
        for j in range(height):
            if matrix[j][id] != 0:
                res = res + matrix[j][id]
    
    return res

if method == "caesar":
    output = caesar_encryption(input, int(key))
elif method == "playfair":
    output = playfair_encryption(input, key)
elif method == "vernam":
    output = vernam_encryption(input, key)
elif method == "railfence":
    output = railFence_encryption(input, int(key))
elif method == "row":
    output = row_trans_encryption(input, key)


output = output.upper()
print(output)