def unic(a, b) -> [str]:
    set1, set2 = set(a), set(b)

    return (set1 - set2) | (set2 - set1)

if __name__ == '__main__':
    print(unic(['a', 'b', 'c'], ['b', 'c', 'aa']))