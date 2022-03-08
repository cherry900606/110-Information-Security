import sys
import numpy as np
import math

method = sys.argv[2]
input = sys.argv[4]
key = sys.argv[6]

def caeser_decrypt(ciphertext, key):
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            plaintext += chr((ord(c) - ord('A') - key) % 26 + ord('A'))
        else:
            plaintext += c
    return plaintext.lower()

def vernam_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(key)):
        if ciphertext[i].isalpha():
            plaintext += chr(((ord(ciphertext[i])-ord('A'))^(ord(key[i])-ord('A'))) + ord('A'))
        else:
            plaintext += ciphertext[i]
    return plaintext.lower()

def rail_fence_decrypt(ciphertext, key):
    plaintext = ""

    matrix = np.ones(shape=(key, len(ciphertext)), dtype=str)

    # 先在 matrix 中標注有字的位置
    x = 0
    y = 0
    isDown = False # 初始化

    while y != len(ciphertext):
        matrix[x][y] = '*'

        if x == key - 1 or x == 0:
            isDown = not isDown
        if isDown:
            x += 1
        else:
            x -= 1
        y += 1

    # 把 ciphertext 填上去
    flag = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if matrix[i][j] == '*':
                matrix[i][j] = ciphertext[flag]
                flag += 1

    # 照著 w 的方向讀字
    x = 0
    y = 0
    isDown = False # 初始化

    while y != len(ciphertext):
        plaintext += matrix[x][y]

        if x == key - 1 or x == 0:
            isDown = not isDown
        if isDown:
            x += 1
        else:
            x -= 1
        y += 1
    return plaintext.lower()

def row_transposition_decrypt(ciphertext, key):
    plaintext = ""

    # 得知長寬、初始化矩陣並將有字的地方標為1
    width = len(str(key))
    height = math.ceil(len(ciphertext) / width)
    matrix = np.ones(shape=(height* width), dtype=str)
    matrix[:len(ciphertext)] = '0'
    matrix = matrix.reshape(height, width)

    # 建立 key 與 matrix column 的對應關係
    m = dict(enumerate(str(key)))
    inv_map = {int(v): k for k, v in m.items()}

    # 填矩陣
    minus = 0
    for i in range(width):
        col = int(str(key)[i])
        start = (col - 1) * height

        for j in range(height):
            if matrix[j][inv_map[col]] != '1':
                matrix[j][inv_map[col]] = ciphertext[start + j - minus]
            else:
                minus += 1

    # 還原原始字串
    for i in range(height):
        for j in range(width):
            if matrix[i][j] != '1':
                plaintext += matrix[i][j]
    return plaintext.lower()

def playfair_decrypt(ciphertext, key):
    plaintext = ""

    # key 填入 matrix
    matrix = np.ones(shape=(25), dtype=str)
    for index, c in enumerate(key):
        if c not in matrix:
            matrix[index] = c
    matrix = matrix.reshape(5,5)

    # 填完剩下的 matrix
    flag = 0
    for i in range(5):
        for j in range(5):
            while flag == 9 or chr(ord('A') + flag) in matrix:
                flag += 1
            if matrix[i][j] == '1':
                matrix[i][j] = chr(ord('A') + flag)
                flag += 1

    #print(matrix)

    # 開始解密
    while len(ciphertext):
        # 倆倆切割
        if len(ciphertext) < 2: # 長度不足補 X
            ciphertext += 'X'
        c1 = ciphertext[0]
        c2 = ciphertext[1]
        ciphertext = ciphertext[2:]
        if c1 == c2: # 兩個相同要拆開
            ciphertext = c2 + ciphertext
            c2 = 'X'
        # 拿到兩個字元的位置
        x1 = np.where(matrix==c1)[0][0]
        y1 = np.where(matrix==c1)[1][0]
        x2 = np.where(matrix==c2)[0][0]
        y2 = np.where(matrix==c2)[1][0]

        if x1 == x2: # same row
            plaintext += matrix[x1][(y1 - 1) % 5] + matrix[x1][(y2 - 1) % 5]
        elif y1 == y2: # same column
            plaintext += matrix[(x1 - 1) % 5][y1] + matrix[(x2 - 1) % 5][y2]
        else:
            plaintext += matrix[x1][y2] + matrix[x2][y1]
    return plaintext.lower()

if method == "caesar":
    output = caeser_decrypt(input, int(key))
elif method == "playfair":
    output = playfair_decrypt(input, key)
elif method == "vernam":
    output = vernam_decrypt(input, key)
elif method == "railfence":
    output = rail_fence_decrypt(input, int(key))
elif method == "row":
    output = row_transposition_decrypt(input, key)

print(output)