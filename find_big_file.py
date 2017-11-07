# coding: utf-8
"""目标：找出指定文件夹中最大的一个文件
"""
from os.path import getsize as get_file_size

from fileutils import list_all_files


def find_biggest_file(file_paths):
    file_path = max(file_paths, key=get_file_size)
    return file_path


def main():
    dir_path = r'C:\Windows\System32'
    all_files = list_all_files(dir_path)
    big_file_path = find_biggest_file(all_files)
    big_file_size = get_file_size(big_file_path)
    print(big_file_path, big_file_size)

if __name__ == '__main__':
    main()
