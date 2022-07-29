"""Print data functions."""


def print_dict(d):
    """Print a dict in a key: value pattern."""
    for key, value in d.items():
        print(key, ' : ', value)


def sort_dict(d):
    """Return a dict sorted by value in reverse order."""
    return sorted(d.items(), key=lambda d: d[1], reverse=True)


def print_tuples(t):
    """Print a list of tuples."""
    for i in t:
        print("  ", i[0], " -> ", i[1])
