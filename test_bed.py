from difflib import SequenceMatcher

a_list = ['Tomato mosaic virus',
          'Tomato ringspot virus',
          'Tomato spotted wilt virus']

b_list = ['Tobamovirus tomato mosaic virus',
          'Nepovirus tomato ringspot virus',
          'Tospovirus tomato spotted wilt virus']


def compare(a: list, b: list):
    ratio = []
    output = []
    for i in enumerate(a):
        a_value = i[1].strip().replace(' ', '').lower().replace('-', '').replace('.', '').replace(',', '')
        for x in enumerate(b):
            b_value = x[1].strip().replace(' ', '').lower()
            ratio_value = str(round(float(SequenceMatcher(None, a_value, b_value).ratio()), 2))
            # print(f'a {i} b {x} {ratio_value}')
            ratio.append(ratio_value + '|' + i[1] + '|' + x[1])
        out_data = sorted(ratio, reverse=True)[0].split('|')
        print(f'{out_data[0]} [{out_data[1]}] vs [{out_data[2]}]')
        ratio = []


compare(a=a_list, b=b_list)
