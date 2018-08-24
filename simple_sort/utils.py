# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 09:26
# @Author  : wangzijun
# @File    : utils.py


def swap(lyst, i, j):
    """
    Exchanges the items at positions i and j.
    交换算法
    :param lyst:
    :param i:
    :param j:
    :return:
    """
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
