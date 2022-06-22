from difflib import SequenceMatcher

a_list = open('./a_list.txt', 'r', encoding='utf-8').readlines()

b_list = open('./b_list.txt', 'r', encoding='utf-8').readlines()


def compare(a: list, b: list):
    ratio = []
    output = []
    for i in enumerate(a):
        a_value = i[1].strip().replace(' ', '').lower().replace('-', '').replace('.', '').replace(',', '').replace(
            '\n', '')
        for x in enumerate(b):
            b = x[1].strip().replace(' ', '').lower().split('|')
            b_value = b[0]
            try:
                b_id = b[1].strip()
            except:
                print(x)
            ratio_value = str(round(float(SequenceMatcher(None, a_value, b_value).ratio()), 2))
            ratio.append(ratio_value + '|' + i[1].strip() + '|' + x[1].strip())
        out_data = sorted(ratio, reverse=True)[0].split('|')
        print(f'{out_data[0]} [{out_data[1]}] vs [{out_data[2]}/{out_data[3]}]')
        ratio = []


compare(a=a_list, b=b_list)
