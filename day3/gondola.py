import re

def task_a():
    finds = dict()
    pattern = r'\d+'
    patt = r'\W'
    answer = 0
    pass
    """ with open("day3.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        sym_indexes = []
        num_indexes = []
        nums = []
        for i in range(len(lines)):
            finds = re.findall(pattern, lines[i])
            symbols = re.findall(patt, lines[i])
            symbols = [symbol for symbol in symbols if symbol != '.']
            symbol_indexes = []
            for y in range(len(lines[i])):
                if len(symbols) == 0: 
                    continue
                elif lines[i][y] == symbols[0]:
                    symbol_indexes.append(y)
                    symbols.remove(lines[i][y])
            indexes = [lines[i].find(tmp) for tmp in finds]
            sym_indexes.append(symbol_indexes)
            num_indexes.append(indexes)
            nums.append(finds)

        for j in range(len(sym_indexes)):
            for index in sym_indexes[j]:
                if int(index) == int(num_indexes[j]) - 1 or int(index) == int(num_indexes[j]) + len(nums[j]) + 1:
                    print(index, sym_indexes[j]) """


def task_b():
    pass

if __name__ == "__main__":
    task_a()
    task_b()