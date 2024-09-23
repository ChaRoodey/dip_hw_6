def counter(s: str) -> {str: int}:
    rez = {}

    for word in s.split(' '):
        if word in rez:
            rez[word] += 1
        else:
            rez[word] = 1

    return rez


if __name__ == '__main__':
    print(counter('Hello world! world!'))