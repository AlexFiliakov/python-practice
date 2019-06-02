class SgfTree(object):
    """SGF is a standard format for storing board game files,
    in particular Go (Baduk).
    """

    def __init__(self, properties={}, children=[]):
        self.properties = properties
        self.children = children

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input: str):
    """Parse SGF Tree
    """
    input = input.replace('\t', ' ')
    escapes = {r'\]': '_-esc_right_square_bracket-_'}
    for esc_key, esc_val in escapes.items():
        input = input.replace(esc_key, esc_val)
    empty_tree_error = ValueError('Please provide an SGF Tree')
    if input is None or input == '':
        raise empty_tree_error

    properties = {}
    expect_key = False
    if len(input) < 3:
        raise ValueError('SGF Tree is too short!')
    if input[0] != '(':
        raise ValueError('SGF Tree missing (')
    if input[-1] != ')':
        raise ValueError('SGF Tree missing )')

    node_sep = ';'
    if input[1] != node_sep:
        raise ValueError('SGF Tree missing ' + node_sep)

    input = input[2:-1]

    children = []
    next_key = ''
    next_value = []
    while not len(input) == 0:
        if input[0] == node_sep:
            children.append(parse(f'({input})'))
            return SgfTree(properties, children)
        if input[0] == '(':
            next_child_len = input.find(')')
            child = input[:next_child_len + 1]
            children.append(parse(child))
            input = input[next_child_len + 1:]
            continue

        next_key_len = input.find('[')
        if next_key == '':
            if next_key_len < 0:
                raise ValueError('SGF Tree missing key')
            next_key = input[0:next_key_len]
            if next_key == '' or not next_key.isalpha():
                raise ValueError(f'SGF key missing')
            if not next_key.isupper():
                raise ValueError(f'SGF key not upper case: {next_key}')
        input = input[next_key_len + 1:]
        next_value_len = input.find(']')

        if next_value_len < 0:
            raise ValueError('SGF key missing value')
        next_value.append(input[0:next_value_len])
        input = input[next_value_len + 1:]
        if input == '' or input[0] != '[':
            def unescape(input):
                for esc_key, esc_val in escapes.items():
                    input = input.replace(esc_val, esc_key[1:])
                return input

            next_value = [unescape(item)
                          for item in next_value]

            properties[next_key] = next_value
            next_key, next_value = '', []

    return SgfTree(properties, children)
