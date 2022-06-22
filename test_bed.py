a_list = open('./a_list.txt', 'r', encoding='utf-8').readlines()
b_list = open('./b_list.txt', 'r', encoding='utf-8').readlines()


def compare(a: list, b: list):
    ratio = []

    for i in range(0, len(a) - 1):
        for x in range(0, len(b) - 1):
            import re
            a_list_value = re.sub(r'', a_list[i].strip().replace(' ', '').replace('-', '').replace('.', '').lower())
            b_list_value = b_list[x].strip().replace(' ', '').replace('-', '').replace('.', '').lower()
            print(a_list_value + '  ' + b_list_value)


compare(a=a_list, b=b_list)
