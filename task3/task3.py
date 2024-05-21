import sys
import json


def read_data(file_path: str) -> dict:
    with open(file_path) as data_file:
        data = json.load(data_file)
        return data


def update_test_values(tests: list[dict], values: list[dict]) -> None:
    for test in tests:
        for value in values:
            if test['id'] == value['id']:
                test['value'] = value['value']
        if 'values' in test:
            update_test_values(test['values'], values)


def write_report(new_tests_data: dict, file_path: str) -> None:
    with open(file_path, 'w') as report_file:
        json.dump(new_tests_data, report_file, indent=4)


def main(tests_path: str, values_path: str, report_path: str) -> None:
    tests_data = read_data(
        file_path=tests_path
    )
    values_data = read_data(
        file_path=values_path
    )
    update_test_values(
        tests=tests_data['tests'],
        values=values_data['values']
    )
    write_report(
        new_tests_data=tests_data,
        file_path=report_path
    )


if __name__ == '__main__':
    main(
        tests_path=sys.argv[1],
        values_path=sys.argv[2],
        report_path=sys.argv[3]
    )
