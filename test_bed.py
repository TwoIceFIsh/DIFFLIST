import asyncio
import re
from difflib import SequenceMatcher

a_list = open('./a_list.txt', 'r', encoding='utf-8').readlines()
b_list = open('./b_list.txt', 'r', encoding='utf-8').readlines()


async def compare(a: list, b: list):
    line_list = []
    # print(len(a))
    for i in range(0, len(a)):
        for x in range(0, len(b)):
            a_list_value = re.sub(r'[^a-zA-Z]+', '',
                                  a_list[i].strip().lower())
            b_list_value = re.sub(r'[^a-zA-Z]+', '',
                                  b_list[x].strip().lower()).split('|')[0]
            a_name = a_list[i].strip()
            b_name = b_list[x].strip().split('|')[0]
            b_code = b_list[x].strip().split('|')[1]

            # 유사도 값
            diff_ratio = round(SequenceMatcher(None, a_list_value, b_list_value).ratio(), 2)

            # 유사도 값 9.0 이상 등록
            if diff_ratio == 1.0:
                line_list.append(
                    f'{str(diff_ratio)}|{a_name}|{b_name}|{b_code}|Matched|{str(diff_ratio)}|{a_name}|{b_name}')
                continue

            # 교집합
            if a_name in b_name or b_name in a_name:
                line_list.append(
                    f'{str(diff_ratio)}|{a_name}|{b_name}|{b_code}|Included|{str(diff_ratio)}|{a_name}|{b_name}')
                continue

            # 유사도 값 9.0 미만 등록
            if 0.9 < diff_ratio < 1.0:
                line_list.append(
                    f'{str(diff_ratio)}|{a_name}|{b_name}|{b_code}|Considerable|{str(diff_ratio)}|{a_name}|{b_name}')

            # 유사도 값 9.0 미만 등록
            if diff_ratio < 0.9:
                line_list.append(f'{str(diff_ratio)}|{a_name}|N/A|N/A|Not Matched|{str(diff_ratio)}|{a_name}|{b_name}')

        datas = sorted(line_list, reverse=True)[0].split('|')

        print(f'{i + 1}|{datas[1]}|{datas[2]}|{datas[3]}|{datas[4]}|{datas[5]}|{datas[6]}|{datas[7]}')

        line_list = []


async def start():
    await asyncio.gather(
        compare(a=a_list, b=b_list)
    )


asyncio.run(start())
