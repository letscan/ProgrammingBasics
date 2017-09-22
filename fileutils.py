# coding: utf-8
"""目标：列出指定文件夹下的所有文件
"""
import os

def list_all_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            yield path


def main():
    root_dir = 'C:\\Windows\\System32'
    for file_path in list_all_files(root_dir):
        print(file_path)

if __name__ == '__main__':
    main()
