def valid_date(d: str) -> bool:
    day, month, year = d.split('.')

    if day > 0 and month > 0 and year > 0 and day <= 31 and month <= 12 and year <= 9999:
        return True
    else:
        return False


if __name__ == '__main__':
    print(valid_date('11.11.2001'))