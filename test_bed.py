import re
from difflib import SequenceMatcher

a_list = open('./a_list.txt', 'r', encoding='utf-8').readlines()
b_list = open('./b_list.txt', 'r', encoding='utf-8').readlines()


def compare(a: list, b: list):
    line_list = []
    # print(len(a))
    for i in range(0, len(a)):
        for x in range(0, len(b)):
            a_list_value = re.sub(r'[^a-zA-Z]+', '',
                                  a_list[i].strip().lower())
            b_list_value = re.sub(r'[^a-zA-Z]+', '',
                                  b_list[x].strip().lower()).split('|')[0]
            diff_ratio = round(SequenceMatcher(None, a_list_value, b_list_value).ratio(), 2)

            line_list.append(f'{str(diff_ratio)}|{a_list[i].strip()}|{b_list[x].strip()}')

        datas = sorted(line_list, reverse=True)[0].split('|')
        print(f'{datas[0]} {datas[1]} / {datas[2]} {datas[3]}')

        line_list = []


compare(a=a_list, b=b_list)
