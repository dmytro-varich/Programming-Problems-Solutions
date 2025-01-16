def stable_marriage(men_preferences, women_preferences):
    """
    Implements the Stable Marriage Algorithm (Gale-Shapley Algorithm).
    
    This function finds a stable matching between men and women based on their 
    preference lists. Each man proposes to women in order of his preference until 
    all matches are stable.

    Args:
        men_preferences (list of lists): Preference lists of men, where men_preferences[i]
                                         is a list of women indices in decreasing preference order for man i.
        women_preferences (list of lists): Preference lists of women, where women_preferences[i]
                                           is a list of men indices in decreasing preference order for woman i.

    Returns:
        list of tuples: Pairs of stable matches in the format (man_index, woman_index).
    """
    # Number of men and women
    n_men = len(men_preferences)
    n_women = len(women_preferences)
    
    # Current partners for each woman (-1 indicates no partner)
    women_partners = [-1] * n_women
    
    # List of free men
    free_men = list(range(n_men))
    
    # Rank matrix for women: women_rank[i][j] gives the rank of man j in woman i's preferences
    women_rank = [[-1] * n_men for _ in range(n_women)]
    for i in range(n_women):
        for rank, man in enumerate(women_preferences[i]):
            women_rank[i][man] = rank
    
    # List to track the number of proposals each man has made
    proposals = [0] * n_men
    
    # While there are free men
    while free_men:
        # Pick the first free man
        man = free_men.pop(0)
        
        # If the man has already proposed to all women, skip
        if proposals[man] >= len(men_preferences[man]):
            continue
        
        # Find the next woman to whom the man will propose
        woman = men_preferences[man][proposals[man]]
        proposals[man] += 1
        
        # If the woman is free, she accepts the proposal
        if women_partners[woman] == -1:
            women_partners[woman] = man
        else:
            # If the woman already has a partner, decide if she prefers the new proposal
            current_partner = women_partners[woman]
            if women_rank[woman][man] < women_rank[woman][current_partner]:
                # The woman prefers the new man, so she switches partners
                women_partners[woman] = man
                free_men.append(current_partner)  # The old partner becomes free
            else:
                # The woman rejects the new proposal
                free_men.append(man)
    
    # Generate the result: list of stable matches as (man, woman) pairs
    pairs = [(women_partners[woman], woman) for woman in range(n_women)]
    return pairs


# Example data: preference lists for men and women
men_preferences = [
    [0, 1, 2, 6, 8, 5, 9, 3, 4, 7],
    [0, 1, 2, 6, 7, 8, 9, 3, 4, 5],
    [4, 0, 2, 3, 6, 7, 5, 9, 1, 8],
    [1, 5, 2, 0, 7, 8, 6, 9, 3, 4],
    [0, 1, 5, 3, 7, 9, 8, 2, 4, 6],
    [9, 1, 2, 3, 7, 5, 4, 0, 6, 8],
    [5, 1, 2, 3, 6, 7, 9, 0, 4, 8],
    [4, 5, 2, 3, 6, 9, 1, 0, 7, 8],
    [2, 1, 7, 5, 8, 9, 0, 3, 4, 6],
    [0, 8, 1, 9, 2, 5, 6, 3, 4, 7],
    [2, 1, 5, 6, 3, 8, 0, 4, 7, 9],
    [7, 1, 2, 4, 9, 5, 0, 3, 6, 8],
    [4, 0, 2, 3, 5, 6, 1, 7, 8, 9]
]

women_preferences = [
    [1, 0, 2, 3, 4, 8, 6, 7, 11, 10, 5, 9, 12],
    [5, 10, 2, 3, 8, 0, 7, 9, 6, 12, 1, 4, 11],
    [0, 1, 3, 6, 9, 7, 11, 10, 2, 4, 5, 8, 12],
    [0, 3, 2, 8, 6, 11, 9, 4, 10, 1, 5, 7, 12],
    [6, 3, 2, 4, 5, 7, 0, 1, 10, 8, 9, 11, 12],
    [0, 11, 2, 3, 10, 1, 7, 8, 9, 6, 4, 5, 12],
    [0, 9, 2, 11, 10, 5, 6, 7, 1, 3, 4, 8, 12],
    [0, 11, 3, 4, 6, 7, 8, 1, 12, 2, 5, 9, 10],
    [0, 7, 11, 3, 6, 5, 4, 9, 12, 1, 2, 8, 10],
    [0, 11, 10, 1, 7, 5, 3, 4, 9, 2, 6, 8, 12]
]

# Solve the stable marriage problem
pairs = stable_marriage(men_preferences, women_preferences)
print(pairs)


def generate_cnf(men_prefs, women_prefs):
    n_men = len(men_prefs)
    n_women = len(women_prefs)

    # Create priority-based indices for all pairs
    ranked_pairs = []
    for m, prefs in enumerate(men_prefs):
        for rank, w in enumerate(prefs):
            ranked_pairs.append((m, w, rank))

    # Sort pairs by priority (rank)
    ranked_pairs.sort(key=lambda x: (x[0], x[2]))  # Sort by man, then by rank

    # Assign unique indices based on priority
    priority_index = { (m, w): i + 1 for i, (m, w, _) in enumerate(ranked_pairs) }

    def var_index(m, w):
        return priority_index[(m, w)]

    clauses = []

    # 1. Each man can be matched with at most one woman
    for m in range(n_men):
        for w1 in range(n_women):
            for w2 in range(w1 + 1, n_women):
                clauses.append([-var_index(m, w1), -var_index(m, w2)])

    # 2. Each woman must be matched with exactly one man
    for w in range(n_women):
        clauses.append([var_index(m, w) for m in range(n_men)])  # At least one
        for m1 in range(n_men):
            for m2 in range(m1 + 1, n_men):
                clauses.append([-var_index(m1, w), -var_index(m2, w)])  # At most one

    # 3. Stability constraints:
    for m in range(n_men):
        for w in range(n_women):
            # Current pair (m,w)
            for m_prime in range(n_men):
                if m_prime == m:
                    continue
                for w_prime in range(n_women):
                    if w_prime == w:
                        continue
                    # Check if (m,w_prime) and (m_prime,w) form a blocking pair
                    if (men_prefs[m].index(w_prime) < men_prefs[m].index(w) and 
                        women_prefs[w_prime].index(m) < women_prefs[w_prime].index(m_prime)):
                        clauses.append([-var_index(m, w), -var_index(m_prime, w_prime)])
      
    return clauses

def cnf_to_string(clauses, n_men, n_women):
    num_vars = n_men * n_women
    num_clauses = len(clauses)
    result = [f"p cnf {num_vars} {num_clauses}"]
    for clause in clauses:
        result.append(" ".join(map(str, clause)) + " 0")
    return "\n".join(result)


men_preferences = [
    [0, 1, 2, 6, 8, 5, 9, 3, 4, 7],
    [0, 1, 2, 6, 7, 8, 9, 3, 4, 5],
    [4, 0, 2, 3, 6, 7, 5, 9, 1, 8],
    [1, 5, 2, 0, 7, 8, 6, 9, 3, 4],
    [0, 1, 5, 3, 7, 9, 8, 2, 4, 6],
    [9, 1, 2, 3, 7, 5, 4, 0, 6, 8],
    [5, 1, 2, 3, 6, 7, 9, 0, 4, 8],
    [4, 5, 2, 3, 6, 9, 1, 0, 7, 8],
    [2, 1, 7, 5, 8, 9, 0, 3, 4, 6],
    [0, 8, 1, 9, 2, 5, 6, 3, 4, 7],
    [2, 1, 5, 6, 3, 8, 0, 4, 7, 9],
    [7, 1, 2, 4, 9, 5, 0, 3, 6, 8],
    [4, 0, 2, 3, 5, 6, 1, 7, 8, 9]
]

women_preferences = [
    [1, 0, 2, 3, 4, 8, 6, 7, 11, 10, 5, 9, 12],
    [5, 10, 2, 3, 8, 0, 7, 9, 6, 12, 1, 4, 11],
    [0, 1, 3, 6, 9, 7, 11, 10, 2, 4, 5, 8, 12],
    [0, 3, 2, 8, 6, 11, 9, 4, 10, 1, 5, 7, 12],
    [6, 3, 2, 4, 5, 7, 0, 1, 10, 8, 9, 11, 12],
    [0, 11, 2, 3, 10, 1, 7, 8, 9, 6, 4, 5, 12],
    [0, 9, 2, 11, 10, 5, 6, 7, 1, 3, 4, 8, 12],
    [0, 11, 3, 4, 6, 7, 8, 1, 12, 2, 5, 9, 10],
    [0, 7, 11, 3, 6, 5, 4, 9, 12, 1, 2, 8, 10],
    [0, 11, 10, 1, 7, 5, 3, 4, 9, 2, 6, 8, 12]
]

clauses = generate_cnf(men_preferences, women_preferences)
cnf_str = cnf_to_string(clauses, len(men_preferences), len(women_preferences))
print(cnf_str)

def generate_index_mapping(men_preferences, women_preferences):
    """
    Generate index mapping for variables.
    Each variable x_m,w is mapped to an index starting from 1.
    """
    n_men = len(men_preferences)
    n_women = len(women_preferences)
    
    index_map = {}
    counter = 1
    
    for i, m in enumerate(men_preferences):
        for w in m:
            index_map[(i, w)] = counter
            counter += 1
    
    return index_map

# Test with given input data
men_preferences = [
    [0, 1, 2, 6, 8, 5, 9, 3, 4, 7],
    [0, 1, 2, 6, 7, 8, 9, 3, 4, 5],
    [4, 0, 2, 3, 6, 7, 5, 9, 1, 8],
    [1, 5, 2, 0, 7, 8, 6, 9, 3, 4],
    [0, 1, 5, 3, 7, 9, 8, 2, 4, 6],
    [9, 1, 2, 3, 7, 5, 4, 0, 6, 8],
    [5, 1, 2, 3, 6, 7, 9, 0, 4, 8],
    [4, 5, 2, 3, 6, 9, 1, 0, 7, 8],
    [2, 1, 7, 5, 8, 9, 0, 3, 4, 6],
    [0, 8, 1, 9, 2, 5, 6, 3, 4, 7],
    [2, 1, 5, 6, 3, 8, 0, 4, 7, 9],
    [7, 1, 2, 4, 9, 5, 0, 3, 6, 8],
    [4, 0, 2, 3, 5, 6, 1, 7, 8, 9]
]

women_preferences = [
    [1, 0, 2, 3, 4, 8, 6, 7, 11, 10, 5, 9, 12],
    [5, 10, 2, 3, 8, 0, 7, 9, 6, 12, 1, 4, 11],
    [0, 1, 3, 6, 9, 7, 11, 10, 2, 4, 5, 8, 12],
    [0, 3, 2, 8, 6, 11, 9, 4, 10, 1, 5, 7, 12],
    [6, 3, 2, 4, 5, 7, 0, 1, 10, 8, 9, 11, 12],
    [0, 11, 2, 3, 10, 1, 7, 8, 9, 6, 4, 5, 12],
    [0, 9, 2, 11, 10, 5, 6, 7, 1, 3, 4, 8, 12],
    [0, 11, 3, 4, 6, 7, 8, 1, 12, 2, 5, 9, 10], 
    [0, 7, 11, 3, 6, 5, 4, 9, 12, 1, 2, 8, 10],
    [0, 11, 10, 1, 7, 5, 3, 4, 9, 2, 6, 8, 12]
]

index_mapping = generate_index_mapping(men_preferences, women_preferences)

# Print the mapping
for pair, index in index_mapping.items():
    print(f"x{pair} -> {index}")