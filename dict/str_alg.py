def function(input_str: str) -> str:
    dict_by_symbol = dict()
    for symbol in input_str:
        if not symbol in dict_by_symbol:
            dict_by_symbol[symbol] = 1
        else:
            dict_by_symbol[symbol] += 1

    sorted_symbol = sorted(dict_by_symbol.keys())
    res = ''
    for symbol in sorted_symbol:
        res += symbol * dict_by_symbol[symbol]

    return res

def main():
    input_str = input("Введите строку: ")
    print('Ответ: ', function(input_str))

if __name__ == "__main__":
    main()