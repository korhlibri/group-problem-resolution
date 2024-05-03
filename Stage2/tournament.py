import create_cromosom
import restriccions_function
import restrictions
import random


def tournament(poblation, n_parents):
    restrictions_dict = restrictions.restrictionsGroups()
    cromosom_sort = []

    for i in poblation:
        cromosom_sort.append(restriccions_function.calculate(i, restrictions_dict, True))
        
    cromosom_sort.sort()
    parents = []
    for _ in range(n_parents):
        candidates = []
        for i in range(0,5):
            candidates.append(random.choice(cromosom_sort))
        parent_1 = min(candidates)

        candidates = []
        for i in range(0,5):
            candidates.append(random.choice(cromosom_sort))
        parent_2 = min(candidates)
        
        parents.append((parent_1[1], parent_2[1]))

    return cromosom_sort, parents

