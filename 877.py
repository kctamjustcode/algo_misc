import math, copy

piles = [5,3,4,5]

def stone_game(stones, a_stones, b_stones, turn):
    if len(stones) == 0:
        if sum(a_stones) > sum(b_stones):
            print(a_stones, b_stones)
            return True
        else:
            return False
    else:
        if turn%2 == 0:
            for i in [-1, 0]:
                if i == -1:
                    new_a_stones = copy.deepcopy(a_stones)
                    new_a_stones += [stones[-1]]
                    new_stones = copy.deepcopy(stones)
                    new_stones = new_stones[:-1]
                    if stone_game(new_stones, new_a_stones, b_stones, turn+1):
                        return True
                if i == 0:
                    new_a_stones = copy.deepcopy(a_stones)
                    new_a_stones += [stones[0]]
                    new_stones = copy.deepcopy(stones)
                    new_stones = new_stones[1:]
                    if stone_game(new_stones, new_a_stones, b_stones, turn+1):
                        return True
            return False
        else:
            for i in [-1, 0]:
                if i == -1:
                    new_b_stones = copy.deepcopy(b_stones)
                    new_b_stones += [stones[-1]]
                    new_stones = copy.deepcopy(stones)
                    new_stones = new_stones[:-1]
                    if not(stone_game(new_stones, a_stones, new_b_stones, turn+1)):
                        return False

                if i == 0:
                    new_b_stones = copy.deepcopy(b_stones)
                    new_b_stones += [stones[0]]
                    new_stones = copy.deepcopy(stones)
                    new_stones = new_stones[1:]
                    if not(stone_game(new_stones, a_stones, new_b_stones, turn+1)):
                        return False
            return True

print(stone_game(piles, [], [], 0))

piles2 = [3,7,2,3]
print(stone_game(piles2, [], [], 0))