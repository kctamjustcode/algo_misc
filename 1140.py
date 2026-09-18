import copy, math

piles = [2,7,9,4,4]
piles2 = [1,2,3,4,5,100]

def stone_game_ii(stones, a_stones, b_stones, turn, M):
    if len(stones) == 0:
        return sum(a_stones)
    else:
        if turn%2 == 0:
            max_cnt = -1*math.inf
            for i in range(1, 2*M+1):
                new_stones = copy.deepcopy(stones)
                new_a_stones = copy.deepcopy(a_stones)
                new_a_stones += new_stones[:i]
                new_stones = new_stones[i:]
                M_new = max(M, i)
                max_cnt = max(max_cnt, stone_game_ii(new_stones, new_a_stones, b_stones, turn+1, M_new))
            return max_cnt
        else:
            min_cnt = math.inf
            for i in range(1, 2*M+1):
                new_stones = copy.deepcopy(stones)
                new_b_stones = copy.deepcopy(b_stones)
                new_b_stones += new_stones[:i]
                new_stones = new_stones[i:]
                M_new = max(M, i)
                min_cnt = min(min_cnt, stone_game_ii(new_stones, a_stones, new_b_stones, turn+1, M_new))
            return min_cnt

print(stone_game_ii(piles, [], [], 0, 1))
print(stone_game_ii(piles2, [], [], 0, 1))


