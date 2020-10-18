import hashlib


def my_range(file_text):
    with open(file_text) as fp:
        lines = fp.readlines()
    for item in lines:
        yield item


if __name__ == '__main__':
    for i in my_range('text.txt'):
        hash_object = hashlib.md5(i.encode())
        print(hash_object.hexdigest())
