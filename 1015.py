def gen_ones(n):
    return int('1'*n)

def smlst_lngth_divisibility(k):
    lngth = 1
    while gen_ones(lngth) % k != 0:
        lngth += 1
        if lngth > 4300:
            return -1
    return lngth, gen_ones(lngth)

for i in range(10+10):
    print(smlst_lngth_divisibility(i+1))