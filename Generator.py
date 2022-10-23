from RandomWordGenerator import RandomWord
from multiprocessing import Process
from typing import List
import random
import multiprocessing
import os


def generator(n, path):
    rw = RandomWord(max_word_size=10, constant_word_size=False)
    with open(path, 'a') as file:
        for i in range(n):
            file.write(rw.generate() + "\n")


def minmax(line, len_max, len_min):
    line_len: int = len(line)
    if line_len > len_max:
        len_max = line_len
    if line_len < len_min:
        len_min = line_len
    return len_max, len_min


def count_vowels_consonants(line, total_v, total_c):
    vowels: list = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for i in line:
        if i in vowels:
            total_v += 1
        else:
            total_c += 1
    return total_v, total_c


def get_lengths(length: int, dict_lengths: dict):
    if dict_lengths.get(length, None):
        dict_lengths[length] += 1
    else:
        dict_lengths[length] = 1
    return dict_lengths


def analyze(path):
    with open(path, 'r') as file:
        sum: int = 0
        count: int = 0
        len_max: int = 0
        len_min: int = 1
        total_v: int = 0
        total_c: int = 0
        dict_lengths = {}
        for line in file:
            sum = sum + len(line)
            len_max, len_min = minmax(line, len_max, len_min)
            count += 1
            total_v, total_c = count_vowels_consonants(line, total_v, total_c)
            dict_lengths = get_lengths(len(line), dict_lengths)
        result = f"""
**********************************************
Аналитика для файла {path}
**********************************************
1. Всего символов --> {sum}
2. Максимальная длина слова --> {len_max}
3. Минимальная длина слова --> {len_min}
4. Средняя длина слова --> {int(sum / count)}
5. Количество гласных --> {total_v}
6. Количество согласных --> {total_c}
7. Количество повторений слов с одинаковой длиной:"""
        print(result)
        for key, value in dict_lengths.items():
            print(f"    {key} сим. - {value} повтор")


def process_file(n):
    path: str = f"/Users/shipelkin/Desktop/PythonProjects/text/{os.getpid()}_{n}.txt"
    generator(n, path)
    analyze(path)


if __name__ == "__main__":
    list_process: List[Process] = []
    for i in range(multiprocessing.cpu_count() - 1):
        p = Process(target=process_file, args=(random.randint(100000, 5000000),))
        p.start()
        list_process.append(p)
    for i in list_process:
        i.join()
