# main.py

def stable_marriage(n, boy_preferences, girl_preferences):
    # Initialize the data structures
    current_partner = [-1] * n
    free_boys = list(range(n))
    next_proposal = [0] * n
    girl_ranking = [[0] * n for _ in range(n)]

    # Build the ranking matrix for girls' preferences
    for g in range(n):
        for rank, b in enumerate(girl_preferences[g]):
            girl_ranking[g][b - 1] = rank
    
    # Perform proposals
    while free_boys:
        b = free_boys.pop(0)
        g = boy_preferences[b][next_proposal[b]] - 1
        next_proposal[b] += 1
        
        if current_partner[g] == -1:
            current_partner[g] = b
        else:
            current_boy = current_partner[g]
            if girl_ranking[g][b] < girl_ranking[g][current_boy]:
                current_partner[g] = b
                free_boys.append(current_boy)
            else:
                free_boys.append(b)
    
    # Prepare the result
    result = []
    for g in range(n):
        result.append((current_partner[g] + 1, g + 1))
    
    return result
