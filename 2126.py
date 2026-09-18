import math, copy

#mass = 10
#asteroids = [3,9,19,5,21]

mass = 5
asteroids = [4,9,23,4]

gained_mass = mass
sorted_asteroids = sorted(asteroids)
destoryable = False
for i in range(len(asteroids)):
    if gained_mass >= sorted_asteroids[i]:
        gained_mass += sorted_asteroids[i]
        if i == len(asteroids)-1:
            destoryable = True

print(destoryable)
