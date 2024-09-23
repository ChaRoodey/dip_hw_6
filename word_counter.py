def counter(s: str) -> {str: int}:
    rez = {}

    for word in s:
        rez[word] = rez.get(word, 0) + 1

    return rez


if __name__ == '__main__':
    print(counter('Hello world! world!'))