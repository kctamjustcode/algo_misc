'''
num = list(range(10))
a, b = 3, 6

left_dist = max(a, b)
right_dist = max(len(num)-a, len(num)-b)
front = min(a, b)
end = min(len(num)-a, len(num)-b)
joint_dist = front+end

ans = min(min(left_dist, right_dist), joint_dist)
'''

def remove_min_and_max(num):
    a = num.index(max(num))
    b = num.index(min(num))

    left_dist = max(a, b) + 1
    right_dist = max(len(num)-a, len(num)-b)
    front = min(a, b) + 1
    end = min(len(num)-a, len(num)-b)
    joint_dist = front+end

    ans = min(min(left_dist, right_dist), joint_dist)
    return ans

print(remove_min_and_max([2,10,7,5,4,1,8,6]))
print(remove_min_and_max([0,-4,19,1,8,-2,-3,5]))