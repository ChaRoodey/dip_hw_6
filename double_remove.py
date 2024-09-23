def sdr(s: str):
    if not s:
        return s

    rez = [s[0]]

    for i in s[1:]:
        if i != rez[-1]:
            rez.append(i)

    return ''.join(rez)



if __name__ == '__main__':
    print(sdr('aabbccaa'))