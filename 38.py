def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    i = 0
    str_n = str(n)
    if len(str_n) == 1:
        return "1"+str_n[0]
    while str_n[i] == str_n[i+1]:
        i += 1
        if i == len(str_n)-1:
            break
    if i == len(str_n)-1:
        return str(i+1)+str_n[i]
    else:
        cont = str((i+1))+str_n[i]
        return cont + countAndSay(int(str_n[i+1:]))

print(countAndSay(1122211444))

def countAndSay_II(n):
    if n == 1:
        return "1"
    elif n == 2:
        return countAndSay(n-1)
    else:
        return countAndSay(int(countAndSay_II(n-1)))

print(countAndSay_II(4))