from json import load


INPUT_FILE = "input.json"


def task() -> float:
    counter = 0
    with open(INPUT_FILE) as input_file:
        json_info = load(input_file)
        for elem in json_info:
            counter += elem["score"] * elem["weight"]
    return round(counter, 3)



print(task())
