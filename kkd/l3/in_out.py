import bitarray


def read_file_by_bytes(file):
    chars = []
    with open(file, "rb") as f:
        while byte:= f.read(1):
            chars.append(byte)
    return chars


def read_file_by_bytes_to_bits(file):
    ba = bitarray.bitarray()
    with open(file, 'rb') as f:
        bytes_ = f.read()
        ba.frombytes(bytes_)
        bits = ba.to01()
    return bits


def read_file_by_chars(file):
    text = ''
    with open(file, "r") as f:
        text = f.read()
    return text


def write_to_file_chars(file, code):
    with open(file, 'w') as f:
        f.write(code)


def write_to_file_bytes_string(file, data, is_omega=False):
    ba = bitarray.bitarray()
    ba.extend(''.join(data))

    if is_omega:
        while len(ba) % 8 != 0:
            ba.append(True)

    pad = len(ba) * 8

    with open(file, 'wb') as f:
        ba.tofile(f)

    return ba.tobytes()


def write_to_file_bytes(file, code):
    with open(file, 'wb') as f:
        f.write(code)
