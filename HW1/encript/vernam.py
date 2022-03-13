
def vernam(p, k):
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
    
    #print(pList)
    #print(kList)
    #print(res)
    

#vernam("helo", "xmcl")