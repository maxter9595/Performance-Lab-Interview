import math


def read_coordinates(file_path: str) -> list:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [tuple(map(float, line.strip().split())) for line in lines]


def main(circle_path: str, points_path: str) -> None:
    circle_center, circle_radius = read_coordinates(circle_path)
    points = read_coordinates(points_path)

    for point in points:
        x, y = point
        distance = math.sqrt(
            (x - circle_center[0]) ** 2 + (y - circle_center[1]) ** 2
        )

        if math.isclose(distance, circle_radius[0]):
            print(0)
        elif distance < circle_radius[0]:
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    print('Введите путь к файлу с координатами и радиусом окружности',
          '(пример: circle.txt)')
    circle_txt_path = input()
    print('Введите путь к файлу с координатами точек',
          '(пример: dot.txt)')
    points_txt_path = input()
    main(
        circle_path=circle_txt_path,
        points_path=points_txt_path
    )
