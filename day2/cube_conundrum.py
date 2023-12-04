import numpy as np

clean_lines = [line.strip().split(":")[1].split(";") for line in open("cube_conundrum.txt").readlines()]

def task_a():
    id_sum = 0
    legal_values = {"red": 12, "green": 13, "blue": 14}
    game_id = 1
    for line in clean_lines:
        legal = True
        split_values = [line.split(",") for line in line]
        for element in split_values:
            values = [value.strip() for value in element]
            for value in values:
                val, key = value.split(" ")
                if int(val) > legal_values.get(key):
                    legal = False
        if legal:
            id_sum += game_id
        game_id += 1
    print(id_sum)


def task_b():
    total = 0
    game_id = 0
    for line in clean_lines:
        game_id += 1
        min_vals = {"red": 0, "green": 0, "blue": 0}
        split_values = [line.split(",") for line in line]
        for element in split_values:
            values = [value.strip() for value in element]
            for value in values:
                val, key = value.split(" ")
                if int(val) > min_vals.get(key):
                    min_vals.update({key: int(val)})
        vals = [int(min_val) for min_val in min_vals.values()]
        product = np.prod(vals)
        total += product
    print(f"Total: {total}")

if __name__ == "__main__":
    task_a()
    task_b()
