from csv import DictReader
from json import dumps



INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as input_file:
        csv_info = [_ for _ in DictReader(input_file)]
    # TODO Сериализовать в файл с отступами равными 4
        with open(OUTPUT_FILENAME, "w") as output_file:
            output_file.write(dumps(csv_info, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
