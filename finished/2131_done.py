def longest(words):
    cache = dict()
    char_count = 0
    middle_word = False
    middle_dict = dict()
    for word in words:
        fc = word[0]
        sc = word[1]
        if fc == sc:
            if word in middle_dict:
                middle_dict[word] += 1
            else:
                middle_dict[word] = 1
        else:
            opposite_word = sc + fc
            if opposite_word in cache and cache[opposite_word] > 0:
                char_count += 4
                cache[opposite_word] -= 1
                #print(word, opposite_word, char_count)
            else:
                if word not in cache:
                    cache[word] = 1
                else:
                    cache[word] += 1
        #print(cache)

    for word, count in middle_dict.items():
        if count % 2 == 1 and not middle_word:
            middle_word = True
            char_count += (count * 2)
            #print("odd", word, char_count)
        else:
            char_count += (int(count / 2) * 4)
            #print("even", word, char_count)
    return char_count


words_list = [["ab", "ty", "yt", "lc", "cl", "ab"], ["lc", "cl", "gg"], ["cc", "ll", "xx"],
              ["qo", "fo", "fq", "qf", "fo", "ff", "qq", "qf", "of", "of", "oo", "of", "of", "qf", "qf", "of"],
              ["bb", "lb", "ll", "bx", "xx", "lx", "xx", "lx", "ll", "xb", "bx", "lb", "bb", "lb", "bl", "bb", "bx",
               "xl", "lb", "xx"]]

for i in range(len(words_list)):
    print(longest(words_list[i]))
    print()

dictq = dict()
for pair in words_list[3]:
    if pair in dictq:
        dictq[pair] += 1
    else:
        dictq[pair] = 1

print(dictq)
