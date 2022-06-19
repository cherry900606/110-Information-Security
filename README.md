# 110-Information-Security
## HW1
Implement:
* Caesar
* Playfair
* Vernam (autokey)
* Rail fence
* Row transposition

一人加密，一人解密

Format:
```
encrypt.o/decrypt.o –m [method] –i [input] –k [key]
\\ Method: caesar/playfair/vernam/railfence/row
\\ Ex: encrypt.o –m caesar –i implaintext –k 4
\\ Plaintext 全為英文小寫 Ciphertext 全為英文大寫
```

## HW2
Implement DES
* Block size: 64 bits
* Key size: 64 bits

一人加密，一人解密

Format:
```
encrypt.o/decrypt.o –i [input] –k [key]
python3 encrypt.py/decrypt.py –i [input] –k [key]
\\ Ex: encrypt.o –i 0x456 –k 0x123
\\ Ex: python3 encrypt.py –i 0x456 –k 0x123
\\ 輸入測資都是 Hex，前面有”0x”；輸出一樣最前面有”0x”，後面若有英文請大寫
```

## HW4
Implement RSA:
* 產生金鑰(產生 p, q, N, phi(N), e, d)
```
python3 RSA.py –i
```
* 加密(輸入任意 msg, N, e, 輸出 cipher text)
```
python3 RSA.py –e [msg] [N] [e]
// 輸出 base64 code
```
* 解密(輸入任意 cipher text, N, d, 輸出 msg)
```
python3 RSA.py –d [ciphertext] [N] [d]
```
* CRT 加速(輸入任意 cipher text, p, q, d, 輸出 msg)
```
python3 RSA.py –CRT [ciphertext] [p] [q] [d]
```

Key size: 1024 bits

一個人完成加密 + 解密

