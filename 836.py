def if_overlap(rec1, rec2):
    case1 = (rec1[0] in range(rec2[0]+1, rec2[2])) and (rec1[1] in range(rec2[1]+1, rec2[3]))
    case2 = (rec1[2] in range(rec2[0]+1, rec2[2])) and (rec1[3] in range(rec2[1]+1, rec2[3]))
    case3 = (rec1[0] in range(rec2[0]+1, rec2[2])) and (rec1[3] in range(rec2[1]+1, rec2[3]))
    case4 = (rec1[2] in range(rec2[0]+1, rec2[2])) and (rec1[1] in range(rec2[1]+1, rec2[3]))
    return case1 or case2 or case3 or case4

exmp1 = [0,0,2,2]
exmp2 = [1,1,3,3]

print(if_overlap(exmp1,exmp2))

exmp1 = [0,0,1,1]
exmp2 = [1,0,2,1]
print(if_overlap(exmp1,exmp2))

exmp1 = [0,0,1,1]
exmp2 = [2,2,3,3]
print(if_overlap(exmp1,exmp2))