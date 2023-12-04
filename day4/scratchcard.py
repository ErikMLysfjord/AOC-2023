import time

lines = [line.split(":")[1].strip().split("|") for line in open("day4.txt").readlines()]
correct_nums = []
actual_nums = []


def task_a():
    answer = 0
    for line in lines:
        point = 0
        correct_nums = [num for num in line[0].strip().split(" ") if num]
        actual_nums = [num for num in line[1].strip().split(" ") if num]
        for num in actual_nums:
            if num in correct_nums:
                if point < 2:
                    point += 1
                else:
                    point *= 2
        answer += point
    print(answer)


def task_b():
    amounts = [1 for i in range(len(lines))]
    for i in range(len(lines)):
        points = 0
        for num in actual_nums:
            if num in correct_nums:
                points += 1
        for j in range(points):
            old_val = amounts[i + j + 1]
            amounts[i + j + 1] = old_val + 1 * amounts[i]
    print(sum(amounts))


if __name__ == "__main__":
    start = time.time()
    task_a()
    task_b()
    end = time.time()
    print(f"Runtime: {end - start}")
