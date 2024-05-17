def read_numbers(file_path: str) -> list:
    with open(file_path) as file:
        nums = [int(line.strip()) for line in file]
    return nums


def get_total_moves(nums: list) -> None:
    nums.sort()
    total_moves = 0
    median = nums[len(nums) // 2]
    for num in nums:
        total_moves += abs(num - median)
    print(total_moves)


def main(numbers_path: str) -> None:
    nums = read_numbers(
        file_path=numbers_path
    )
    get_total_moves(
        nums=nums
    )


if __name__ == '__main__':
    print('Введите путь к файлу c целыми числами (пример: numbers.txt)')
    numbers_txt_path = input()
    main(
        numbers_path=numbers_txt_path
    )
