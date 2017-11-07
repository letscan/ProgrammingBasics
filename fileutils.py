# coding: utf-8
"""目标：列出指定文件夹下的所有文件
"""
import os
import hashlib


def raise_(e):
    raise e

def list_all_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, onerror=raise_):
        for filename in filenames:
            full_path = os.path.realpath(os.path.join(dirpath, filename))
            yield full_path

def list_dir_children(root_dir):
    for path in os.listdir(root_dir):
        full_path = os.path.realpath(os.path.join(root_dir, path))
        yield full_path

def get_dir_size(dirpath):
    file_paths = list_all_files(dirpath)
    size = sum(os.path.getsize(p) for p in file_paths)
    return size

def read_text(path, encoding='utf-8'):
    with open(path, 'r') as fp:
        text = fp.read()
    return text

def read_bytes(path):
    with open(path, 'rb') as fp:
        bs = fp.read()
    return bs

def get_hash(path):
    content = read_bytes(path)
    hasher = hashlib.sha256()
    hasher.update(content)
    return hasher.hexdigest()


def main():
    root_dir = 'C:\\Windows\\System32'
    for path in list_dir_children(root_dir):
        print(path, get_dir_size(path))

if __name__ == '__main__':
    main()
