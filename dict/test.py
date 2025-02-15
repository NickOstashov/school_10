def start_test(eng_dict: dict):
    score = 0
    keys = eng_dict.keys()
    for key in keys:
        answ = input(f"Введите перевод слова {key}: ")
        if answ.lower() == eng_dict[key]:
            score += 1

    return score


def main():
    eng_dict = {"hello": "привет"}
    print(start_test(eng_dict))


if __name__ == '__main__':
    main()
