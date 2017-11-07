# coding: utf-8
"""一些有用的工具函数
"""
from collections import defaultdict


def group_by(iterable, key=None):
    get_key = key or (lambda e: e)
    groups = defaultdict(list)
    for item in iterable:
        try:
            key = get_key(item)
        except Exception:
            pass
        else:
            groups[key].append(item)
    return groups


def main():
    import sys
    print(sys.path[0])

if __name__ == '__main__':
    main()
