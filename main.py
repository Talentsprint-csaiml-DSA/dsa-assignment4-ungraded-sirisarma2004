def stable_marriage(n, boy_preferences, girl_preferences):
    # Initialize free boys and proposals count
    free_boys = list(range(n))  # Boys are indexed from 0 to n-1
    next_proposal = [0] * n  # Track the next girl to propose to for each boy
    girl_partner = [-1] * n  # Track the current partner of each girl (-1 means free)

    # Create a rank list for girls for faster comparison
    girl_rank = [[0] * n for _ in range(n)]
    for girl in range(n):
        for rank, boy in enumerate(girl_preferences[girl]):
            girl_rank[girl][boy - 1] = rank  # Store the rank of each boy for the girl

    while free_boys:
        # Get the first free boy
        boy = free_boys.pop(0)
        # Get the next girl to propose to
        girl_index = next_proposal[boy]
        girl = boy_preferences[boy][girl_index] - 1  # Convert to 0-indexed

        # Propose to the girl
        if girl_partner[girl] == -1:  # If the girl is free
            girl_partner[girl] = boy  # Engage the boy and girl
        else:
            current_partner = girl_partner[girl]
            # Check if the girl prefers the new boy over her current partner
            if girl_rank[girl][boy] < girl_rank[girl][current_partner]:
                # She prefers the new boy
                girl_partner[girl] = boy  # Engage the new boy
                free_boys.append(current_partner)  # The current partner becomes free
            else:
                # She prefers her current partner, so the boy remains free
                free_boys.append(boy)

        # Move to the next girl for the boy
        next_proposal[boy] += 1

    # Prepare the result in the required format
    result = [(boy + 1, girl + 1) for girl, boy in enumerate(girl_partner)]
    return result
