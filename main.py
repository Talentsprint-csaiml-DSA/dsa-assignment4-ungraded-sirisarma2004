def stable_marriage(n, boy_preferences, girl_preferences):
    free_boys = list(range(n))
    girl_engaged_to = [-1] * n
    boy_engaged_to = [-1] * n
    girl_ranking = [[0] * n for _ in range(n)]
    for g in range(n):
        for rank, b in enumerate(girl_preferences[g]):
            girl_ranking[g][b - 1] = rank
    boy_proposals = [0] * n
    while free_boys:
        boy = free_boys.pop(0)
        next_girl = boy_preferences[boy][boy_proposals[boy]] - 1
        boy_proposals[boy] += 1
        if girl_engaged_to[next_girl] == -1:
            girl_engaged_to[next_girl] = boy
            boy_engaged_to[boy] = next_girl
        else:
            current_boy = girl_engaged_to[next_girl]
            if girl_ranking[next_girl][boy] < girl_ranking[next_girl][current_boy]:
                girl_engaged_to[next_girl] = boy
                boy_engaged_to[boy] = next_girl
                free_boys.append(current_boy)
                boy_engaged_to[current_boy] = -1
            else:
                free_boys.append(boy)
    return [(boy + 1, girl + 1) for boy, girl in enumerate(boy_engaged_to)]

if __name__ == "__main__":
    n = 3
    boy_preferences = [[1, 2, 3], [2, 1, 3], [1, 2, 3]]
    girl_preferences = [[2, 1, 3], [1, 3, 2], [3, 1, 2]]
    result = stable_marriage(n, boy_preferences, girl_preferences)
    print("Stable marriages:", result)
