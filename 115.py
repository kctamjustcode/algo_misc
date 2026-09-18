testing_set = [('rabbbit', 'rabbit'), ('babgbag', 'bag')]

for i in range(2):
    substrings = [[]]

    def generate_substrings(s, sub, t):
        if len(sub) == len(t) and sub == t:
            substrings[0] += [sub]
        elif len(sub) < len(t):
            for i in range(len(s)):
                sub_new = sub
                sub_new += s[i]
                new_s = s[i+1:]
                generate_substrings(new_s, sub_new, t)

    generate_substrings(testing_set[i][0], '', testing_set[i][1])
    print(len(substrings[0]))

    #generate_substrings('babgbag', '', 'bag')
    #print(len(substrings[0]))
