#!/usr/bin/env python3
from itertools import pairwise

def main():
    safe = 0
    safe_with_damper = 0

    with open('inputs/d2.txt') as f:
        for line in f:
            nums = [int(x) for x in line.split()]
            if is_safe(nums):
                safe += 1
            if is_safe_with_damper(nums):
                safe_with_damper += 1
    print(safe)
    print(safe_with_damper)

def test_is_safe():
    assert is_safe([1, 2, 3]) is True
    assert is_safe([5, 2, 0]) is True
    assert is_safe([1, 0, 4]) is False
    assert is_safe([19, 17, 16, 17]) is False
    assert is_safe([1, 1]) is False

    assert is_safe_with_damper([7, 6, 4, 2, 1]) is True
    assert is_safe_with_damper([1, 2, 7, 8, 9]) is False
    assert is_safe_with_damper([9, 7, 6, 2, 1]) is False
    assert is_safe_with_damper([1, 3, 2, 4, 5]) is True
    assert is_safe_with_damper([8, 6, 4, 4, 1]) is True
    assert is_safe_with_damper([1, 3, 6, 7, 9]) is True


def is_safe(nums):
    direction = 0
    removed = False
    for l, r in pairwise(nums):
        if l == r:
            return False
        if not direction:
            direction = 1 if l < r else -1

        if not validate_direction(direction, l, r):
            return False

    return True


def is_safe_with_damper(nums):
    to_skip = 0

    if is_safe(nums):
        return True

    while to_skip < len(nums):
        if is_safe([x for i, x in enumerate(nums) if i != to_skip]):
            return True
        to_skip += 1

    return False

def validate_direction(direction, l, r):
    if direction == 1:
        lo, hi = l, r
    elif direction == -1:
        lo, hi = r, l

    return lo < hi and hi - lo >= 1 and hi - lo <= 3
   

test_is_safe()
main()
