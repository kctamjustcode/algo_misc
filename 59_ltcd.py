n = 4


n_matrix = [[] for _ in range(n)]

cnt = 0
parity_cnt = 0
top_occur = 0
right_occur = 0
bottum_occur = 0
left_occur = 0

direction = 0

last_num = 1

while last_num < n*n+1:
    if direction % 4 == 0:
        n_matrix[top_occur].insert(left_occur+cnt,last_num)
        cnt += 1
        last_num += 1
        if left_occur + right_occur + cnt == n:
            cnt = 0
            top_occur += 1
            direction += 1
    elif direction % 4 == 1:
        n_matrix[top_occur + cnt].insert(len(n_matrix[top_occur + cnt])-right_occur, last_num)
        cnt += 1
        last_num += 1
        if top_occur + cnt + bottum_occur == n:
            cnt = 0
            right_occur += 1
            direction += 1
    elif direction % 4 == 2:
        n_matrix[n-1 - bottum_occur].insert(right_occur-1, last_num)
        cnt += 1
        last_num += 1
        if right_occur + cnt + left_occur == n:
            cnt = 0
            bottum_occur += 1
            direction += 1
    elif direction % 4 == 3:
        n_matrix[n-1 - bottum_occur - cnt].insert(left_occur, last_num)
        cnt += 1
        last_num += 1
        if top_occur + bottum_occur + cnt == n:
            cnt = 0
            left_occur += 1
            direction += 1
