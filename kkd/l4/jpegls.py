from methods import methods_map
from math import log2
from collections import Counter


def from_tga(filename):
    with open(filename, 'rb') as f:
        id_len = int.from_bytes(f.read(1), 'little')
        col_map_type = int.from_bytes(f.read(1), 'little')
        img_type = int.from_bytes(f.read(1), 'little')

        # colormap
        first_entr_idx = int.from_bytes(f.read(2), 'little')
        col_map_len = int.from_bytes(f.read(2), 'little')
        col_map_entr_size = int.from_bytes(f.read(1), 'little')

        # img info
        start_x = int.from_bytes(f.read(2), 'little')
        start_y = int.from_bytes(f.read(2), 'little')
        width = int.from_bytes(f.read(2), 'little')
        height = int.from_bytes(f.read(2), 'little')
        pix_depth = int.from_bytes(f.read(1), 'little')
        img_descr = int.from_bytes(f.read(1), 'little')

        attrs_per_prixel = img_descr & 0x00001111
        order = (img_descr & 0x00110000) >> 4
        zero = (img_descr & 0x11000000) >> 6

        if (order & 0x10) != 0:
            vert = range(height)
        else:
            vert = reversed(range(height))

        if (order & 0x01) == 0:
            horiz = range(width)
        else:
            horiz = reversed(range(width))

        bitmap = [0 for _ in range(width*height)]
        for y in vert:
            for x in horiz:
                b = int.from_bytes(f.read(1), 'little')
                g = int.from_bytes(f.read(1), 'little')
                r = int.from_bytes(f.read(1), 'little')
                bitmap[y*width + x] = (r, g, b)
    return (width, height), bitmap


def entropy(frequency, size):
    return -sum([(v/size)*(log2(v)-log2(size))
                 for v in frequency if v > 0])


def print_entropy(triples, header):
    size = len(triples)
    global_entropy = entropy(Counter(triples).values(), size)
    r_entropy = entropy(Counter([r for (r, _, _) in triples]).values(), size)
    g_entropy = entropy(Counter([g for (_, g, _) in triples]).values(), size)
    b_entropy = entropy(Counter([b for (_, _, b) in triples]).values(), size)
    print(header)
    print('---------------------------------------')
    print(f'Global entropy: {global_entropy}')
    print(f'red entropy: {r_entropy}')
    print(f'green entropy: {g_entropy}')
    print(f'blue entropy: {b_entropy}')
    print('---------------------------------------')
    return (header, global_entropy, r_entropy, g_entropy, b_entropy)


def get_neighbours(original, w, h, x, y):
    if x == 0:
        NW = (0, 0, 0)
        W = (0, 0, 0)
        if y == 0:
            N = (0, 0, 0)
        else:
            N = original[(y-1)*w]
    elif y == 0:
        NW = (0, 0, 0)
        N = (0, 0, 0)
        W = original[x-1]
    else:
        N = original[(y-1)*w + x]
        W = original[y*w + x-1]
        NW = original[(y-1)*w + x-1]
    return NW, N, W


def generate_new_img(original, w, h, f):
    new_img = []
    for y in range(h):
        for x in range(w):
            triple = original[y*w + x]
            NW, N, W = get_neighbours(original, w, h, x, y)
            curr = ((triple[0] - f(NW[0], N[0], W[0])) % 256,
                    (triple[1] - f(NW[1], N[1], W[1])) % 256,
                    (triple[2] - f(NW[2], N[2], W[2])) % 256)
            new_img.append(curr)
    return new_img


def compare_entropies(results):
    globals = {val: head for (head, val, _, _, _) in results}
    reds = {val: head for (head, _, val, _, _) in results}
    greens = {val: head for (head, _, _, val, _) in results}
    blues = {val: head for (head, _, _, _, val) in results}
    print('================================')
    print('Best method for global: ', globals[min(globals)])
    print('Best method for red: ', reds[min(reds)])
    print('Best method for green: ', greens[min(greens)])
    print('Best method for blue: ', blues[min(blues)])
    print('================================')


def test_for_methods_map(original, w, h):
    results = []
    for k, f in methods_map.items():
        curr_img = generate_new_img(original, w, h, f)
        results.append(print_entropy(curr_img, f'Method {k}'))
    compare_entropies(results)


def main():
    file = 'tests/example0.tga'
    (w, h), triples = from_tga(file)
    print_entropy(triples, 'Original')
    test_for_methods_map(triples, w, h)


if __name__ == '__main__':
    main()
