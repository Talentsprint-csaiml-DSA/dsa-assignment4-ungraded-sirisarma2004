def stable_marriage(n, boy_preferences, girl_preferences):
    # Initialize all boys and girls as free
    free_boys = list(range(n))
    girl_engaged_to = [-1] * n  # This will store the boy each girl is engaged to
    boy_engaged_to = [-1] * n  # This will store the girl each boy is engaged to

    # Create a rank table for girls to quickly check preferences
    girl_ranking = [[0] * n for _ in range(n)]
    for g in range(n):
        for rank, b in enumerate(girl_preferences[g]):
            girl_ranking[g][b - 1] = rank  # -1 for 0-indexing

    # Create a list of proposals made by each boy
    boy_proposals = [0] * n  # boy_proposals[i] is the index of the next girl boy i will propose to
    
    while free_boys:
        boy = free_boys.pop(0)  # Get the first free boy
        next_girl = boy_preferences[boy][boy_proposals[boy]] - 1  # Get the next girl to propose to (convert to 0-index)

        # Boy proposes to the next girl
        boy_proposals[boy] += 1

        # Check if the girl is free
        if girl_engaged_to[next_girl] == -1:
            # Girl is free, accept the proposal
            girl_engaged_to[next_girl] = boy
            boy_engaged_to[boy] = next_girl
        else:
            # Girl is already engaged, check if she prefers this boy
            current_boy = girl_engaged_to[next_girl]
            if girl_ranking[next_girl][boy] < girl_ranking[next_girl][current_boy]:
                # She prefers the new boy, so swap
                girl_engaged_to[next_girl] = boy
                boy_engaged_to[boy] = next_girl
                # The rejected boy becomes free
                free_boys.append(current_boy)
                boy_engaged_to[current_boy] = -1
            else:
                # She prefers her current engagement, reject the proposal
                free_boys.append(boy)  # The boy remains free and can propose again

    # The result is the boy-girl engagement list
    result = [(boy + 1, girl + 1) for boy, girl in enumerate(boy_engaged_to)]
    return result

# Example input
n = 3
boy_preferences = [[1, 2, 3], [2, 1, 3], [1, 2, 3]]
girl_preferences = [[2, 1, 3], [1, 3, 2], [3, 1, 2]]

# Output the stable marriage matching
result = stable_marriage(n, boy_preferences, girl_preferences)
print(result)
