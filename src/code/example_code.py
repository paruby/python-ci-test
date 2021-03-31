from typing import List, Any


def append_list(input_list: List, elem: Any) -> List:
    input_list.append(elem)
    return input_list


def merge_sort(input: List[int]) -> List[int]:
    if len(input) in [0, 1]:
        return input
    else:
        left = merge_sort(input[0: len(input)//2])
        right = merge_sort(input[len(input)//2:])

        merged = []
        pl, pr = 0, 0
        while pl < len(left) and pr < len(right):
            if left[pl] < right[pr]:
                merged.append(left[pl])
                pl += 1
            else:
                merged.append(right[pr])
                pr += 1
        merged = merged + left[pl:] + right[pr:]
        return merged
