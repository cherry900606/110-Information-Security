
def caesar_encryption(p,k):
  e = ''
  for i in p:
    if i.isupper():
      temp = 65 + ((ord(i) - 65 + k) % 26) 
      e = e + chr(temp)                              
    elif i.islower():
      temp = 97 + ((ord(i) - 97 + k) % 26)
      e = e + chr(temp)
    else:
      e = e + i  
    
 
  # print cipher
  print(e)
 