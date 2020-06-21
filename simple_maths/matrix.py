import copy
from operator import add, mul


class Matrix2D:
    def __init__(self, shape, init=0, data=None):
        assert len(shape) == 2
        self.shape = shape
        if data is None:
            self.data = [[init] * shape[1] for _ in range(shape[0])]
        else:
            self.data = data

    def copy(self):
        return Matrix2D(self.shape, data=copy.deepcopy(self.data))

    def __repr__(self):
        return '\n'.join(' '.join(map(str, self.data[i])) for i in range(self.shape[0]))

    def _elementwise_op_inplace(self, m, op):
        if type(m) == Matrix2D:
            assert self.shape == m.shape
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.data[i][j] = op(self.data[i][j], m.data[i][j])
        else:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.data[i][j] = op(self.data[i][j], m)

    def _elementwise_op(self, m, op):
        result = self.copy()
        result._elementwise_op_inplace(m, op)
        return result

    def __add__(self, other):
        return self._elementwise_op(other, add)

    def __mul__(self, other):
        return self._elementwise_op(other, mul)

    def __matmul__(self, other):
        r1, c1 = self.shape
        r2, c2 = other.shape
        if c1 != r2:
            raise ValueError('Incompatible matrices')

        data = []
        for i in range(r1):
            row = []
            for j in range(c2):
                row.append(sum(self.data[i][k] * other.data[k][j] for k in range(c1)))
            data.append(row)
        return Matrix2D(shape=(r1, c2), data=data)

    def transpose(self, ttype=1):
        if ttype == 1:
            shape = (self.shape[1], self.shape[0])
            m = Matrix2D(shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    m.data[j][i] = self.data[i][j]
            return m
        elif ttype == 2:
            shape = (self.shape[1], self.shape[0])
            m = Matrix2D(shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    m.data[self.shape[1] - j - 1][self.shape[0] - i - 1] = self.data[i][j]
            return m
        elif ttype == 3:
            shape = self.shape
            m = Matrix2D(shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    m.data[i][self.shape[1] - j - 1] = self.data[i][j]
            return m
        elif ttype == 4:
            shape = self.shape
            m = Matrix2D(shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    m.data[self.shape[0] - i - 1][j] = self.data[i][j]
            return m
        return None

    def minor(self, i, j) -> float:
        minor_shape = (self.shape[0] - 1, self.shape[1] - 1)
        minor_data = []
        for r in range(self.shape[0]):
            if r == i - 1:
                continue
            row = self.data[r]
            minor_data.append(row[:j-1] + row[j:])
        return Matrix2D(shape=minor_shape, data=minor_data).det

    def cofactor(self, i, j) -> float:
        return (-1)**(i+j) * self.minor(i, j)

    @property
    def det(self) -> float:
        if self.shape == (1, 1):
            return self.data[0][0]

        if self.shape == (2, 2):
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

        det_ = 0
        for j in range(self.shape[1]):
            det_ += self.data[0][j] * self.cofactor(1, j+1)
        return det_

    @staticmethod
    def from_input(name=''):
        name = name + ' ' if name else ' '
        shape = tuple(map(int, input(f'Enter size of {name}matrix: ').split()))
        print(f'Enter {name}matrix: ')
        data = []
        for i in range(shape[0]):
            row = list(map(float, input().split()))
            if len(row) != shape[1]:
                raise ValueError('Unexpected row size')
            data.append(row)
        return Matrix2D(shape, data=data)


def main():
    while True:
        choice = input("1. Add matrices\n"
                       "2. Multiply matrix by a constant\n"
                       "3. Multiply matrices\n"
                       "4. Transpose matrix\n"
                       "4. Transpose matrix\n"
                       "5. Calculate a determinant\n"
                       "0. Exit\n"
                       "Your choice: ")

        try:
            if choice == '1':
                m1 = Matrix2D.from_input('first')
                m2 = Matrix2D.from_input('second')
                print('The result is:')
                print(m1 + m2)
            elif choice == '2':
                m = Matrix2D.from_input()
                n = float(input('Enter constant: '))
                print('The result is:')
                print(m * n)
            elif choice == '3':
                m1 = Matrix2D.from_input('first')
                m2 = Matrix2D.from_input('second')
                print('The result is:')
                print(m1 @ m2)
            elif choice == '4':
                ttype = input("1. Main diagonal\n"
                              "2. Side diagonal\n"
                              "3. Vertical line\n"
                              "4. Horizontal line\n"
                              "Your choice: ")

                m = Matrix2D.from_input()
                print('The result is:')
                print(m.transpose(int(ttype)))
            elif choice == '5':
                m = Matrix2D.from_input()
                print('The result is:')
                print(m.det)
            else:
                break
        except ValueError:
            print('The operation cannot be performed.')


if __name__ == "__main__":
    main()
