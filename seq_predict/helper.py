def sgn(x):
    """ The signum function """
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def iter_pairs(seq, cycle=False):
    """Iterates like all pairs (seq[i], seq[i+1])"""
    it = iter(seq)
    i = next(it)
    for j in it:
        yield (i, j)
        i = j

    if cycle:
        yield (i, seq[0])


def isConstant(seq):
    """ Check if seq is constant """
    first = seq[0]
    for i in seq:
        if i != first:
            return False
    return True


def match_seq(s, seq):
    """try to match the sequences s[i:] to seq[a:b] (b < len(s2))
    return a tuple: (the size of the longest match, seq[b])

    Arguments:
        s: sequence to match
        seq: sequence to be matched with
    """

    match_size, match_b = 0, len(seq) - 1
    for b in range(len(seq) - 2, -1, -1):
        b_, j = b, len(s) - 1
        fail = False

        while b_ != -1 and j != -1:
            if seq[b_] != s[j]:
                fail = True
                break
            b_, j = b_ - 1, j - 1

        if not fail and match_size < b - b_:
            match_size = b - b_
            match_b = b

    if match_size < 3:
        return (0, None)

    return (match_size, seq[match_b + 1])


def complete_match_seq(s, seq):
    """ Try to match sequence s completely inside seq.
    Return first seq index of matching else None."""
    l_s = len(s)
    l_seq = len(seq)
    if l_seq - 1 < l_s:
        return None

    first_index = 0
    for first_index in range(l_seq - l_s + 1):
        fi1 = first_index
        fi2 = fi1 - first_index
        while fi2 < l_s and fi1 < l_seq and s[fi2] == seq[fi1]:
            fi1, fi2 = fi1 + 1, fi2 + 1
        if fi2 == l_s:
            return first_index


def test_match_seq():
    '''
    Tests for match_seq function
    '''
    seq = [1, 4, 9, 16]
    s = [1, 4, 9]
    assert match_seq(s, seq) == (3, 16)

    seq = [1, 4, 9]
    s = [1, 4, 9]
    assert match_seq(s, seq) == (0, None)

    seq = [1, 2, 4, 8, 16, 32, 64, 128]
    s = [1, 2, 4]
    assert match_seq(s, seq) == (3, 8)

    seq = [1, 2, 4, 8, 16, 32, 64, 128]
    s = [2, 2, 4]
    assert match_seq(s, seq) == (0, None)


def test_complete_match_seq():
    seq = [1, 4, 9, 16, 25]
    s = [3, 1, 4, 9]
    assert complete_match_seq(s, seq) == None

    s = [1, 4, 9]
    assert complete_match_seq(s, seq) == 0

    s = [1, 4, 9, 16]
    assert complete_match_seq(s, seq) == 0

    s = [1, 4, 9, 10]
    assert complete_match_seq(s, seq) == None

    s = [4, 9, 16]
    assert complete_match_seq(s, seq) == 1


if __name__ == "__main__":
    # test_match_seq()
    test_complete_match_seq()
