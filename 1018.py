def convert_to_int_1018(ans):
    num = 0
    for i in range(len(ans)):
        num += 2**(len(ans)-i-1)*ans[i]
    return num

# print(convert_to_int_1018([1,0,1]))
num = [1,0,1]

#for i in range(len(num)):
anws = [convert_to_int_1018(num[:i+1])%5 == 0 for i in range(len(num))]
print(anws)

num = [0,1,1]
anws = [convert_to_int_1018(num[:i+1])%5 == 0 for i in range(len(num))]
print(anws)