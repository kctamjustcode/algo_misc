import math, copy

stones = [5,1,2,4,3]

def stone_game_ix(stone_row, removed, turn):
    if sum(removed) % 3 == 0 and len(removed) != 0:
        if turn%2 == 0:
            return True
        else:
            return False
    if len(stone_row) == 0 and sum(removed)%3 != 0:
        return False
    else:
        if turn%2 == 0:
            for stone in stone_row:
                #if sum(removed) + stone % 3 == 0:
                #    return False
                #else:
                new_stone_row = copy.deepcopy(stone_row)
                new_stone_row.remove(stone)
                new_removed = copy.deepcopy(removed)
                new_removed.append(stone)
                if stone_game_ix(new_stone_row, new_removed, turn+1):
                    return True
            return False
        else:
            for stone in stone_row:
                #if sum(removed) + stone % 3 == 0:
                #    return True
                #else:
                new_stone_row = copy.deepcopy(stone_row)
                new_stone_row.remove(stone)
                new_removed = copy.deepcopy(removed)
                new_removed.append(stone)
                if not stone_game_ix(new_stone_row, new_removed, turn+1):
                    return False
            return True

print(stone_game_ix(stones, [], 0))
print(stone_game_ix([2, 1], [], 0))
print(stone_game_ix([2], [], 0))