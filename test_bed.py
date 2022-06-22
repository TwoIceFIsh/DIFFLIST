from difflib import SequenceMatcher

a_list = open('./a_list.txt', 'r', encoding='utf-8').readlines()
b_list = open('./b_list.txt', 'r', encoding='utf-8').readlines()


def compare(a: list, b: list):
    ratio = []
    output = []
    print(len(a))
    print(len(b))

    for i in a:
        a_value = i.strip().replace(' ', '').lower().replace('-', '').replace('.', '').replace(',', '').replace(
            '\n', '')
        print(i.strip())
        for x in b:
            b = x.strip().replace(' ', '').lower().split('|')
            b_value = b[0]

            ratio_value = str(round(float(SequenceMatcher(None, a_value, b_value).ratio()), 2))

            ratio.append(ratio_value + '|' + i.strip() + '|' + x.strip())
            print(x.strip())

        out_data = sorted(ratio, reverse=True)[0].split('|')

        out_data = []
        ratio = []


compare(a=a_list, b=b_list)
