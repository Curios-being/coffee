class Matrices:

    def matrix(self, rows):
        rows = int(rows)
        # let's hope there won't be wrong column input
        return [[float(j) for j in input().split()] for i in range(rows)]

    def multiply_by_const(self):
        rows, columns = input('Enter size of matrix: ').split()
        print('Enter matrix:')
        matr = self.matrix(rows)
        multip = int(input('Enter constant: '))
        prod = []
        for row in range(int(rows)):
            prod.append([matr[row][column] * multip for column in range(int(columns))])
        print('The result is:\n')
        for _ in prod:
            print(*_)

    def muliply_matr(self):
        rows_1, columns_1 = input('Enter size of first matrix: ').split()
        print('Enter first matrix:')
        matr_1 = self.matrix(rows_1)
        rows_2, columns_2 = input('Enter size of second matrix: ').split()
        print('Enter second matrix:')
        matr_2 = self.matrix(rows_2)
        if int(columns_1) != int(rows_2):
            print('The operation cannot be performed.\n')
            return 0
        prod = [[0 for j in range(int(columns_2))] for i in range(int(rows_1))]
        # iterate through rows of matr_1
        for i in range(len(matr_1)):
            # iterate through columns of matr_2
            for j in range(len(matr_2[0])):
                # iterate through rows of matr_2
                for k in range(len(matr_2)):
                    prod[i][j] += matr_1[i][k] * matr_2[k][j]
        for _ in prod:
            print(*_)

    def add_matrices(self):
        rows_1, columns_1 = input('Enter size of first matrix: ').split()
        print('Enter first matrix:')
        matr_1 = self.matrix(rows_1)
        rows_2, columns_2 = input('Enter size of second matrix: ').split()
        print('Enter second matrix:')
        matr_2 = self.matrix(rows_2)
        if rows_2 != rows_1 or columns_2 != columns_1:
            print('The operation cannot be performed.\n')
            return 0

        summ = []
        for row in range(int(rows_1)):
            summ.append([matr_1[row][column] + matr_2[row][column] for column in range(int(columns_1))])
        print('The result is:\n')
        for _ in summ:
            print(*_)

    def transpose(self, choice):
        rows, columns = input('Enter size of matrix: ').split()
        print('Enter matrix:')
        matr = self.matrix(rows)
        if choice == '1':
            matr = self.main_diagonal(matr)
        elif choice == '2':
            matr = self.side_diagonal(matr)
        elif choice == '3':
            matr = self.vertical_line(matr)
        elif choice == '4':
            matr = self.horizontal_line(matr)
        else:
            print('Sorry, no such operation')
            return 0
        print('The result is:')
        for _ in matr:
            print(*_)

    # on main diagonal
    # def transposeMatrix(m):
    #     return map(list, zip(*m))

    def main_diagonal(self, matrix):
        # result = []
        # # iterate through rows
        # for i in range(len(X)):
        #     # iterate through columns
        #     for j in range(len(X[0])):
        #         result[j][i] = X[i][j]

        return [[matrix[column][row] for column in range(len(matrix[0]))] for row in range(len(matrix))]

    def side_diagonal(self, matrix):
        # reverse and then same as main diagonal and then again reverse
        matrix = [[matrix[row][-column] for column in range(1, len(matrix[0]) + 1)] for row in range(len(matrix))]
        matrix = [[matrix[column][row] for column in range(len(matrix[0]))] for row in range(len(matrix))]
        return [[matrix[row][-column] for column in range(1, len(matrix[0]) + 1)] for row in range(len(matrix))]
    def vertical_line(self, matrix):
        return [[matrix[row][-column] for column in range(1, len(matrix[0]) + 1)] for row in range(len(matrix))]

    def horizontal_line(self, matrix):
        return [[matrix[-row][column] for column in range(len(matrix[0]))] for row in range(1, len(matrix) + 1)]

    def determinant_recursive(self, matrix, total=0):
        # Section 1: store indices in list for row referencing
        indices = list(range(len(matrix)))
        if len(matrix) == 1:
            return matrix[0][0]
        # Section 2: when at 2x2 submatrices recursive calls end
        if len(matrix) == 2 and len(matrix[0]) == 2:
            val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return val

        # Section 3: define submatrix for focus column and
        #      call this function
        for fc in indices:  # A) for each focus column, ...
            # find the submatrix ...
            copy_matrix = matrix[:]  # B) make a copy, and ...
            copy_matrix = copy_matrix[1:]  # ... C) remove the first row
            height = len(copy_matrix)  # D)

            for i in range(height):
                # E) for each remaining row of submatrix ...
                #     remove the focus column elements
                copy_matrix[i] = copy_matrix[i][0:fc] + copy_matrix[i][fc + 1:]

            sign = (-1) ** (fc % 2)  # F)
            # G) pass submatrix recursively
            sub_det = self.determinant_recursive(copy_matrix)
            # H) total all returns from recursion
            total += sign * matrix[0][fc] * sub_det

        return total

    # and yeah, this doesn't cover 1 1 case
    # not gonna lie, didn't quite get it, but i'll just save, so i could use it in future
    # def determinant_fast(self, matrix):
    #     # Section 1: Establish n parameter and copy A
    #     n = len(matrix)
    #     copy = matrix[:]
    #
    #     # Section 2: Row ops on A to get in upper triangle form
    #     for fd in range(n):  # A) fd stands for focus diagonal
    #         for i in range(fd + 1, n):  # B) only use rows below fd row
    #             if copy[fd][fd] == 0:  # C) if diagonal is zero ...
    #                 copy[fd][fd] == 1.0e-18  # change to ~zero
    #             # D) cr stands for "current row"
    #             crScaler = copy[i][fd] / copy[fd][fd]
    #             # E) cr - crScaler * fdRow, one element at a time
    #             for j in range(n):
    #                 copy[i][j] = copy[i][j] - crScaler * copy[fd][j]
    #
    #     # Section 3: Once copy is in upper triangle form ...
    #     product = 1.0
    #     for i in range(n):
    #         # ... product of diagonals is determinant
    #         product *= copy[i][i]
    #
    #     return product


    # i geuss cheating, but, whatever, it would take too much time to invent the bike, when i could just analyse it
    def getMatrixMinor(self, m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def getMatrixDeternminant(self, m):
        # base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * self.getMatrixDeternminant(self.getMatrixMinor(m, 0, c))
        return determinant

    def getMatrixInverse(self, m):
        determinant = self.getMatrixDeternminant(m)
        # special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]

        # find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = self.getMatrixMinor(m, r, c)
                cofactorRow.append(((-1) ** (r + c)) * self.getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = self.main_diagonal(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant

        for i in cofactors:
            print(*i)

    def menu(self):
        while True:
            choice = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: """)
            if choice == '1':
                self.add_matrices()
            elif choice == '2':
                self.multiply_by_const()
            elif choice == '3':
                self.muliply_matr()
            elif choice == '4':
                choice = input("""\n1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: """)
                self.transpose(choice)
            elif choice == '5':
                rows, columns = input('Enter size of matrix: ').split()
                print('Enter matrix:')
                matr = self.matrix(rows)
                print('The result is:', self.determinant_recursive(matr), sep='\n')
            elif choice == '6':
                rows, columns = input('Enter size of matrix: ').split()
                print('Enter matrix:')
                matr = self.matrix(rows)
                self.getMatrixInverse(matr)
            elif choice == '0':
                break
            else:
                print('Sorry, no such choice\n')

Matrices().menu()