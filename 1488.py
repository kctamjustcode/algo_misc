rains = [1,2,0,0,2,1,0,0,2,3,0,0,4,5,0,0,2,3]
#rains = [1,2,0,1,2]
#rains = [1,2,3,4]
ans = [-1 if rains[i] > 0 else None for i in range(len(rains))]


def segmenting(rains):
    rains_segment = []
    rain_fragment = []
    for i in range(len(rains)):
        if rains[i] == 0:
            if rain_fragment != []:
                rains_segment += [rain_fragment]
                rain_fragment = []
        elif i == len(rains)-1:
            rain_fragment += [rains[i]]
            rains_segment += [rain_fragment]
        else:
            rain_fragment += [rains[i]]
    return rains_segment

print(segmenting(rains))

def mntc_check(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True


def drying_occupied_schedule():
    occupied = []
    scheduling = []
    rain_segements = segmenting(rains)
    for rain_days in rain_segements:
        if not mntc_check(rain_days):
            return []
    for rain_days in rain_segements:
        occupied_segment = []
        for day in rain_days:
            occupied_segment += [day]
            if not mntc_check(occupied_segment):
                return []
    for i in range(len(rain_segements)-1):
        curr_occpd_segm = []    #
        #coming_occpd_segm = []
        for lake in rain_segements[i]:
            if lake > 0:
                curr_occpd_segm += [lake]   #
                occupied += [lake]
        #for j in range(i+1, len(rain_segements)):
        for lake in rain_segements[i+1]:
            if lake > 0 and lake in occupied:
                scheduling += [lake]
    return scheduling

print(drying_occupied_schedule())

def check_item_mntc(a, lst):
    cnt = 0
    for item in lst:
        if item == a:
            cnt += 1
    return cnt == 1

def drying_lakes_ans():
    schedule = drying_occupied_schedule()
    occupied = []
    #print(schedule)
    for i in range(len(ans)):
        if rains[i] > 0:
            occupied += [rains[i]]
        elif ans[i] is None and schedule[0] in occupied and mntc_check(occupied):
            ans[i] = schedule.pop(0)
            occupied.remove(ans[i])
        if schedule == []:
            return ans
    return ans

print('rain days: ', rains)
print('pre-answer: ',drying_lakes_ans())

def check_vaildity():
    answering = drying_lakes_ans()
    #print('raining:', rains)
    #print('debug: ', answering)
    if len(answering) == 0:
        return False
    else:
        assert len(answering) == len(rains)
        rain_segments = segmenting(rains)
        occupying = []
        #for rains in rain_segments:
        for i in range(len(rains)):
            #print('occp: ', occupying)
            #print('ans:', answering)
            if rains[i] > 0:
                occupying += [rains[i]]
                if not mntc_check(occupying):
                    return False
            if rains[i] == 0:
                if answering[i] in occupying:
                    drying_lake = answering[i]
                    occupying.remove(drying_lake)
        return True

print(check_vaildity())

def final_ans():
    if check_vaildity():
        return drying_lakes_ans()
    else:
        return []
    
print('ans: ', final_ans())
