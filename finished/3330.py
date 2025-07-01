words = ["abbcccc", "abcd", "aaaa"]

for word in words:
    lt = []
    last_ch = ''
    for i, ch in enumerate(word):
        if not lt:
            lt.append(ch)
        elif ch == last_ch:
            new_w = lt[-1] + ch
            lt.append(new_w)
        else:
            lt[-1] += ch

        last_ch = ch

    print(len(lt))
