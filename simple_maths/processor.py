from simple_maths.matrix import Matrix2D


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
