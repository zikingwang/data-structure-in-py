# -*- coding: utf-8 -*-


def index_of_min(lyst):
    """
    Returns the index of the minnum item.
    搜索列表的最小值
    O(n)
    :param lyst:
    :return:
    """
    min_index = 0
    current_index = 1
    while current_index < len(lyst):
        if lyst[current_index] < lyst[min_index]:
            min_index = current_index
        current_index += 1
    return min_index


def sequential_search(target, lyst):
    """
    Returns the position of the target itrm if found, or -1 otherwise.
    顺序搜索,如果找到返回目标索引,如果没找到,返回-1
    O(n)
    :param target:
    :param lyst:
    :return:
    """
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1


def binary_search(target, sorted_lyst):
    """
    Binary search need sourted list
    二分查找算法
    O(log2n)
    :param target:
    :param sorted_lyst:
    :return:
    """
    left = 0
    right = len(sorted_lyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sorted_lyst[midpoint]:
            return midpoint
        elif target < sorted_lyst[midpoint]:
            right = midpoint - 1
        elif target > sorted_lyst[midpoint]:
            left = midpoint + 1
    return -1
