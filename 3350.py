nums = [2,5,7,8,9,2,3,4,3,1]

def get_max_adj_incrsn_subseq_lengt(nums):
    max_length = 0
    freq_dict = {}
    for i in range(len(nums)):
        k = 0
        while nums[i+k] == nums[i]+k:
            k += 1
            if i+k >= len(nums):
                break
        max_length = max(k, max_length)
        if str(k) not in freq_dict.keys():
            freq_dict[str(k)] = 1
        else:
            freq_dict[str(k)] += 1
    return freq_dict

print(get_max_adj_incrsn_subseq_lengt(nums))

