def task_a():
    with open("./aoc1.txt") as f:
        lines = f.readlines()
        clean_lines = [line.strip() for line in lines]
        answer = 0
        for line in clean_lines:
            cat_num = ""
            for letter in line:
                if letter.isnumeric():
                    cat_num = letter
                    break
            for letter in line[::-1]:
                if letter.isnumeric():
                    new_num = cat_num + letter
                    break
            answer += int(new_num)
        print(f"Answer for task a: {answer}")

def task_b():
    with open("./aoc1.txt") as f:
        lines = f.readlines()
        clean_lines = [line.strip() for line in lines]
        numbers_s = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        answer = 0
        for line in clean_lines:
            result = ""
            for i in range(1, len(line) + 1):
                if any(char.isnumeric() for char in line[:i]):
                    result += line[i - 1]
                    break
                elif any(ext in line[:i] for ext in numbers_s):
                    for j in range(len(line[:i]) + 1):
                        if line[i - j : i] in numbers_s:
                            result += str(numbers_s.index(line[i - j : i]) + 1)
                            break
                    break
            for j in range(len(line) - 1, -1, -1):
                if any(char.isnumeric() for char in line[j:]):
                    result += line[j]
                    break
                elif any(ext in line[j:] for ext in numbers_s):
                    for k in range(len(line[j:]) + 1):
                        if line[j : j + k] in numbers_s:
                            result += str(numbers_s.index(line[j : j + k]) + 1)
                            break
                    break
            answer += int(result)
    print(f"Answer for task b: {answer}")


if __name__ == "__main__":
    task_a()
    task_b()
