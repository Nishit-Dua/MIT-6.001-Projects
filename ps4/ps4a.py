# Problem Set 4A
# Name: Nishit Dua
# Collaborators: None
# Time Spent: Idk man lol

def get_permutations(sequence: str):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    '''
    if sequence.__len__() <= 1:
        # Nested list so i dont have to make a special case for a sing char
        return [[sequence]]

    first = sequence[:1]
    sequence = sequence[1:]

    perm_list = []
    permuted_smaller_seq = get_permutations(sequence)

    for seq in permuted_smaller_seq:
        # print(seq, f'first:  {first}') # Testing
        for x in range(len(seq) + 1):
            tmp = seq[:]
            tmp.insert(x, first)
            perm_list.append(tmp)
    # print(f'perm_list = {perm_list}') # Testing
    return perm_list


def permutations(perm_list):
    return list(set([''.join(c) for c in get_permutations(perm_list)]))


if __name__ == '__main__':
    # EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', permutations(example_input))
    print('-'*50, '\n')  # Indentation

    example_input = 'aabb'
    print('Input:', example_input)
    print('Expected Output:', ['aabb', 'bbaa', 'baab', 'baba', 'abab', 'abba'])
    print('Actual Output:', permutations(example_input))
    print('-'*50, '\n')

    example_input = 'sed'
    print('Input:', example_input)
    print('Expected Output:', ['sed', 'sde', 'dse', 'des', 'esd', 'eds'])
    print('Actual Output:', permutations(example_input))
    print('-'*50, '\n')
