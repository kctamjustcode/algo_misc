n = 1000

cnt = n

#def get_cnt_dict(cnt):
verf = False
while not verf:
    cnt += 1
    str_cnt = str(cnt)
    nbn_verf_dict = {}
    for alphabet in str_cnt:
        if alphabet not in nbn_verf_dict.keys():
            nbn_verf_dict[alphabet] = 1
        else:
            nbn_verf_dict[alphabet] += 1
    verf = True
    for alphabet in str_cnt:
        if nbn_verf_dict[alphabet] != int(alphabet):
            verf = False
print(cnt)
