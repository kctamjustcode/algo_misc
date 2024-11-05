from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    sc = [candidate for candidate in candidates if candidate <= target]
    alsub = [[]]
    for cand in sc:
        new = []
        for sub in alsub:
            new.append(sub+[cand])
        alsub += new
    ans = []
    for sub in alsub:
        if sum(sub) == target:
            if sorted(sub) not in ans:
                ans.append(sorted(sub))
    return ans

candidates = [10,1,2,7,6,1,5]
print(combinationSum2(candidates, 8))