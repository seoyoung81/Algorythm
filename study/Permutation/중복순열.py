def generate_permutations(lst):
    """
    Recursively generates all permutations of a list.
    """
    if len(lst) == 0:
        return [[]]

    permutations = []

    for i in range(len(lst)):
        # Get the current element
        elem = lst[i]

        # Get all permutations of the remaining elements
        remaining = lst[:i] + lst[i + 1:]
        remaining_perms = generate_permutations(remaining)

        # Combine the current element with each permutation of the remaining elements
        for perm in remaining_perms:
            # remove duplicate permutations
            new_perm = [elem] + perm
            if new_perm not in permutations:
                permutations.append(new_perm)

    return permutations

lst = [0, 0, 1, 1]
perms = generate_permutations(lst)
print(perms)