#wizards_time = [0 for _ in range(len(skill)+1)]

def check_wizards_available(wiz_tim, expt_tim):
    #assert len(wiz_tim) == len(expt_tim),[ wiz_tim,  expt_tim]
    vaildties = [0 if expt_tim[i]>=wiz_tim[i] else 1 for i in range(len(wiz_tim))]
    return sum(vaildties) == 0

print(check_wizards_available([0,1,2,3],[2,2,2,3]))
def brew_potion_time(skill, mana):
    wizards_time = [0 for _ in range(len(skill)+1)]
    for item in mana:
        cnt = 0
        #for w in range(len(wizards_time)):
        expected_time_indv = [skill[i]*item for i in range(len(skill))]
        #print('mana: ', expected_time_indv)
        expected_time_group = [sum(expected_time_indv[0:i])+cnt for i in range(len(skill)+1)]
        #print('time: ',wizards_time, expected_time_group)
        min_indv_wizards_time = [wizards_time[i] + expected_time_indv[i-1] for i in range(1, len(wizards_time))]
            #wizards_time[i] += expected_time_indv[i-1]
        #print('min_indv: ',min_indv_wizards_time)
        while not check_wizards_available(min_indv_wizards_time, expected_time_group[1:]):
            #cnt += 1
            for i in range(len(expected_time_group)):
                expected_time_group[i] += 1
            #expected_time_group = [sum(expected_time_indv[:i])+cnt for i in range(len(skill)+1)]
        #print('result: ',expected_time_group, cnt)
        wizards_time = expected_time_group #[expected_time_group[i] + wizards_time[i] for i in range(len(wizards_time))]
    return wizards_time
    #print(wizards_time)

s1 = [1, 5, 2, 4]
m1 = [5, 1, 4, 2]

print(brew_potion_time(s1, m1))

s2 = [1,1,1]
m2 = [1,1,1]

print(brew_potion_time(s2, m2))