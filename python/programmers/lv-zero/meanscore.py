def solution(score):
    answer = []
    # Calculate the mean score for each student
    mean_score = [sum(sc) / len(sc) for sc in score]

    # Sort the mean scores in descending order and assign ranks
    sorted_mean_score = sorted(mean_score, reverse=True)
    rank_map = {}
    rank = 1

    for i, s in enumerate(sorted_mean_score):
        if s not in rank_map:  # Only assign rank to unique scores
            rank_map[s] = rank
        rank += 1

    # Assign ranks to the original mean scores
    for m in mean_score:
        answer.append(rank_map[m])

    return answer


def solution(score):
    a = sorted([sum(i) for i in score], reverse=True)
    return [a.index(sum(i)) + 1 for i in score]


print(
    solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])
)  # [1, 2]
print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))  # [3]
