import os
from src.option import Option


def parse_num(s: str) -> Option:
    try:
        num = int(s)
        return Option.some(num)
    except ValueError:
        return Option.none()


nums = []
fail = False

while True:

    os.system("clear")
    if fail:
        print("Invalid integer")
        fail = False
    print(f"list = {nums}")

    user_input = input("number or \"done\": ")
    n = parse_num(user_input)

    if user_input == "done":
        break

    if n.is_none():
        fail = True
        continue

    nums += [n.unwrap()]


os.system("clear")
print(f"original = {nums}")

restart = False

while True:
    for n in range(len(nums) - 1):
        if nums[n] > nums[n + 1]:
            nums[n], nums[n + 1] = nums[n + 1], nums[n]
            restart = True
            break

    if restart:
        restart = False
        continue

    break

print(f"sorted = {nums}")
