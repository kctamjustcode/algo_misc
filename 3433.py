#numberOfUsers = 2
#events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]

def count_mentions(numberOfUsers, events):

    mentions = [0 for _ in range(numberOfUsers)]

    cnt = 0
    ending = events[-1][1]

    OnlineUser = list(range(numberOfUsers))
    Offline = [None for _ in range(numberOfUsers)]

    event_cnt = 0

    while cnt <= int(events[-1][1]):
        try:
            if int(events[event_cnt][1]) == cnt:
                if events[event_cnt][0] == 'MESSAGE':
                    if events[event_cnt][-1] == 'ALL':
                        for i in range(len(mentions)):
                            mentions[i] += 1
                    elif events[event_cnt][-1] == "HERE":
                        for member in OnlineUser:
                            mentions[member] += 1
                    else:
                        for member in events[event_cnt][-1].split(' '):
                            mentions[int(member[2:])] += 1
                            #print('executed')
                elif events[event_cnt][0] == 'OFFLINE':
                    for member in events[event_cnt][-1]:
                        Offline[int(member)] = cnt
                        OnlineUser.remove(int(member))
                event_cnt += 1
            cnt += 1
        except:
            cnt += 1
        for i in range(len(Offline)):
            if Offline[i] != None and cnt - Offline[i] == 60:
                Offline[i] == None
                OnlineUser += [i]
                #print('Online', i, cnt)
    return mentions

nOU = 2
evnts = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
print(count_mentions(nOU, evnts))

nOU = 2
evnts = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]
print(count_mentions(nOU, evnts))

nOU = 2
evnts = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
print(count_mentions(nOU, evnts))