import math, copy

triangle =  [[2],[3, 7],[8, 5, 6],[6, 1, 9, 3]]

def min_sum_path(tri, lyr, indx, min_sum):
    if lyr == len(triangle):
        return min_sum
    else:
        if lyr == 0:
            return min_sum_path(tri, 1, 0, tri[0][0])
        else:
            min_sum_proc = math.inf
            for ind in [indx, indx+1]:
                min_sum_cp = min_sum + tri[lyr][ind]
                min_sum_proc = min(min_sum_proc, min_sum_path(tri, lyr+1, ind, min_sum_cp))
            return min_sum_proc
    
print(min_sum_path(triangle, 0, 0, 0))
