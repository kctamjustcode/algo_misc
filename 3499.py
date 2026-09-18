import copy

#s = "0100"
#aug_s = '1'+s+'1'

def find_zero_blocks(s):
    aug_s = '1'+s+'1'
    zero_blocks = []
    for i in range(1,len(aug_s)-2):
        if aug_s[i-1] == '1' and aug_s[i] == '0':
            for j in range(i, len(aug_s)):
                if aug_s[j] == '0':
                    continue
                if aug_s[j] == '1':
                    zero_blocks += [(i, j-1)]
                    break
    return zero_blocks

def find_one_blocks(s):
    one_blocks = []
    zero_found = False
    for i in range(len(s)):
        if s[i] == 0:
            zero_found = True
    if zero_found:
        for i in range(1,len(aug_s)-2):
            if aug_s[i-1] == '0' and aug_s[i] == '1':
                for j in range(i, len(aug_s)):
                    if aug_s[j] == '1':
                        continue
                    if aug_s[j] == '0':
                        one_blocks += [(i, j-1)]
                        break
        return one_blocks
    else:
        return [(0, len(s)-1)]


s_exmp = "1000100"
aug_s = '1'+s_exmp+'1'
one_blocks = find_one_blocks(s_exmp)

max_cnt = 0
for one_block in one_blocks:
    new_aug_s = ""
    for i in range(len(aug_s)):
        if i in range(one_block[0], one_block[1]+1):
            new_aug_s += '0'
        else:
            new_aug_s += aug_s[i]

    new_zero_blocks = find_zero_blocks(new_aug_s[1:-1])

    for zero_block in new_zero_blocks:
        new_aug_s_1 = ""
        for i in range(len(aug_s)):
            if i in range(zero_block[0], zero_block[1]+1):
                new_aug_s_1 += '1'
            else:
                new_aug_s_1 += new_aug_s[i]

        new_one_blocks = find_one_blocks(new_aug_s_1)
        new_one_block_lens = [item[1]-item[0]+1 for item in new_one_blocks]

        print(new_aug_s, new_aug_s_1)

        max_cnt = max(max_cnt, max(new_one_block_lens)-2)

print(max_cnt)

