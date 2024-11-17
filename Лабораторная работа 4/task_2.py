# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:

    with open(INPUT_FILENAME) as f:
        lines = [csv_line for csv_line in csv.DictReader(f)]


    with open(OUTPUT_FILENAME, 'w') as sf:
        json.dump(lines, sf, indent=4)

if __name__ == '__main__':

    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
