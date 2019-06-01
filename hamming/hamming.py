def distance(strand_a, strand_b):
    """Exercism solution to the Distance challenge.

    Arguments:
        strand_a {int} -- parm...
        strand_b {int} -- parm...
    """
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be same length!')

    return len([1 for a, b in zip(strand_a, strand_b) if a != b])
