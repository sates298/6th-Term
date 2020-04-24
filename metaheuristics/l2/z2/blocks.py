import random


class Matrix():
    def __init__(self, w, h, k):
        self.f_width = w
        self.f_height = h
        self.k = k
        self.matrix = []
        self.changed = False

    def swap_2_blocks(self):
        self.changed = False
        i, n = random.sample(range(len(self.matrix)), k=2)
        j = random.choice(range(len(self.matrix[i])))
        m = random.choice(range(len(self.matrix[n])))
        iter = 0
        while not self.matrix[i][j] == self.matrix[n][m] and iter < 10:
            iter += 1
            i, n = random.sample(range(len(self.matrix)), k=2)
            j = random.choice(range(len(self.matrix[i])))
            m = random.choice(range(len(self.matrix[n])))

        if iter < 10:
            self.changed = True
            block1 = self.matrix[i][j]
            block2 = self.matrix[n][m]
            block1.x, block2.x = block2.x, block1.x
            block1.y, block2.y = block2.y, block1.y
            self.matrix[i][j], self.matrix[n][m] = \
                self.matrix[n][m], self.matrix[i][j]

    def change_one_color(self, colors):
        self.changed = False
        block = random.choice(random.choice(self.matrix))
        old_c = block.color
        block.color = random.choice(colors)
        while block.color == old_c:
            block.color = random.choice(colors)
        self.changed = True

    def stretch_one(self):
        self.changed = False
        i = random.choice(range(len(self.matrix)))
        j = random.choice(range(len(self.matrix[i])))
        block = self.matrix[i][j]
        iter = 0
        while block.h == self.k and block.w == self.k:
            i = random.choice(range(len(self.matrix)))
            j = random.choice(range(len(self.matrix[i])))
            block = self.matrix[i][j]
            iter += 1
            if iter > 10:
                self.changed = False
                return None
        if block.h > self.k and random.random() > 0.33:
            if i > 0:
                upper = self.matrix[i-1][j]
                if upper.x == block.x and upper.w == block.w:
                    upper.h += 1
                    block.h -= 1
                    block.y += 1
                    self.changed = True
            else:
                lesser = self.matrix[i+1][j]
                if lesser.x == block.x and lesser.w == block.w:
                    lesser.h += 1
                    block.h -= 1
                    lesser.y -= 1
                    self.changed = True
        if block.w > self.k and random.random() > 0.33:
            if j > 0:
                left = self.matrix[i][j-1]
                if left.y == block.y and left.h == block.h:
                    left.w += 1
                    block.w -= 1
                    block.x += 1
                    self.changed = True
            else:
                right = self.matrix[i][j+1]
                if right.y == block.y and right.h == block.h:
                    right.w += 1
                    block.w -= 1
                    lesser.x -= 1
                    self.changed = True

    def generate_start(self, colors):
        mod_h = self.f_height % self.k
        mod_w = self.f_width % self.k
        blocks_w = self.f_width // self.k
        blocks_h = self.f_height // self.k

        for i in range(blocks_h):
            row = []
            for j in range(blocks_w):
                row.append(Block(j*self.k, i*self.k, self.k,
                                 self.k, random.choice(colors)))
            self.matrix.append(row)
        for i in range(blocks_h):
            self.matrix[i][-1].w += mod_w
        for i in range(blocks_w):
            self.matrix[-1][i].w += mod_h
        return self


    def to_matrix(self):
        matrix = [[0 for _ in range(self.f_width)]
                  for _ in range(self.f_height)]
        for row in self.matrix:
            for block in row:
                for i in range(block.x, block.x + block.w):
                    for j in range(block.y, block.y + block.h):
                        print(i, ' ', j)
                        # matrix[j][i] = block.color
        return matrix


class Block():
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def __eq__(self, other):
        return self.w == other.w and self.h == other.h
