def merge_two_series_by_max(col1, col2):
    col = []
    for i in range(col1.size):
        if col1[i] >= col2[i]:
            col.append(col1[i])
        else:
            col.append(col2[i])
    return col


def reverse_vote_uf(s):
    # fillna perche gli elementi che non corrispondono vengono messi a na e da errore combine

    v1 = s.mask(s == 1, 5)
    v2 = s.mask(s == 2, 4)
    v3 = s.mask(s == 3, 3)
    v4 = s.mask(s == 4, 2)
    v5 = s.mask(s == 5, 1)

    v3 = v3.combine(v1, max)
    v3 = v3.combine(v2, max)
    v3 = v3.combine(v4, max)
    v3 = v3.combine(v5, max)

    return v3


def switch(e):
    switcher = {
        0: 0,
        1: 5,
        2: 4,
        3: 3,
        4: 2,
        5: 1
    }
    return switcher.get(e, lambda: "Invalid")


def reverse_vote_not_uf(s):
    list = []
    for i in range(s.size):
        list.append(switch(s[i]))
    return list
