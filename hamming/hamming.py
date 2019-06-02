def distance(a: str, b: str):
    """Returns the number of character differences between two strings.
    """
    if len(a) != len(b):
        raise ValueError('Strands must be same length!')

    return len([1 for n, m in zip(a, b) if n != m])
