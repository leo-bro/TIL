def solution(lines):
    nlines = []
    overlay = 0
    for line in lines:
        nlines.append([f + 0.5 for f in range(line[0], line[1])])
    minl = min([line[0] for line in lines])
    maxl = max([line[-1] for line in lines])
    print(minl, maxl)
    for n in range(minl, maxl + 1, 1):
        cnt = len([1 for nline in nlines if (n + 0.5) in nline])
        if cnt >= 2:
            overlay += 1
    return overlay


def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


print(solution([[0, 2], [-3, -1], [-2, 1]]))
