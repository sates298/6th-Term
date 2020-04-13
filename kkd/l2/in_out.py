def read_file_by_bytes(file):
    chars = []
    with open(file, "rb") as f:
        while byte:= f.read(1):
            chars.append(byte)
    return chars


def read_file_by_chars(file):
    text = ''
    with open(file, "r") as f:
        text = f.read()
    return text


def write_to_file_chars(file, code):
    with open(file, 'w') as f:
        f.write(code)


def write_to_file_bytes(file, code):
    with open(file, 'wb') as f:
        f.write(code)
