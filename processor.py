
def generate_matrix(matrix_number=""):
    matrix_size = input(f"Enter size of {matrix_number} matrix: ")
    matrix_size = matrix_size.split(' ')
    n = int(matrix_size[0])
    m = int(matrix_size[1])
    matrix = list()
    print(f"Enter {matrix_number} matrix: ")
    for i in range(0, n):
        row = input().split(' ')
        try:
            converted_list = [int(num) for num in row]
        except ValueError:
            converted_list = [float(num) for num in row]
        matrix.append(converted_list)
    return matrix, n, m


def print_matrix_result(matrix_result):
    print("The result is: ")
    for row in matrix_result:
        print(' '.join(str(num) for num in row))


def add_matrices():
    first_matrix, a_n, a_m = generate_matrix(matrix_number="first")
    second_matrix, b_n, b_m = generate_matrix(matrix_number="second")

    if a_n == b_n and a_m == b_m:
        sum_matrix = list()
        for i in range(0, a_n):
            sum_matrix.append([])
            for j in range(0, a_m):
                sum_matrix[i].append(second_matrix[i][j] + first_matrix[i][j])
        print_matrix_result(sum_matrix)
    else:
        print('ERROR')


def multiply_matrix_by_constant(matrix, scalar):
    product_matrix = list()
    for i in range(len(matrix)):
        product_matrix.append([])
        for j in range(len(matrix[i])):
            product_matrix[i].append(matrix[i][j] * scalar)
    return product_matrix


def shuffle_matrix(matrix_to_shuffle):
    row_len = len(matrix_to_shuffle)
    column_len = len(matrix_to_shuffle[0])
    new_matrix = [[0 for x in range(row_len)] for y in range(column_len)]

    for i in range(len(matrix_to_shuffle)):
        for j in range(len(matrix_to_shuffle[i])):
            new_matrix[j][i] = matrix_to_shuffle[i][j]
    return new_matrix


def multiply_matrices():
    first_matrix, a_n, a_m = generate_matrix(matrix_number="first")
    second_matrix, b_n, b_m = generate_matrix(matrix_number="second")

    if a_m == b_n:
        shuffled_matrix_b = shuffle_matrix(second_matrix)
        product_matrix = []

        for row_matrix in first_matrix:
            outer_row = []
            for row_shuffled in shuffled_matrix_b:
                inner_row = []
                for j in range(len(row_shuffled)):
                    multi = row_matrix[j] * row_shuffled[j]
                    inner_row.append(multi)
                outer_row.append(sum(inner_row))
            product_matrix.append(outer_row)
        print_matrix_result(product_matrix)  # Display result

    else:
        print('ERROR')


def transpose_main_diagonal():
    generated_matrix, n, m = generate_matrix()
    shuffled_matrix = shuffle_matrix(generated_matrix)
    print_matrix_result(shuffled_matrix)


def transpose_side_diagonal():
    generated_matrix, n, m = generate_matrix()
    generated_matrix.reverse()
    for row in generated_matrix:
        row.reverse()
    shuffled_matrix = shuffle_matrix(generated_matrix)
    print_matrix_result(shuffled_matrix)


def transpose_vertical_line():
    generated_matrix, n, m = generate_matrix()
    for row in generated_matrix:
        row.reverse()
    print_matrix_result(generated_matrix)


def transpose_horizontal_line():
    generated_matrix, n, m = generate_matrix()
    generated_matrix.reverse()
    print_matrix_result(generated_matrix)


def find_determinant(matrix):

    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        not_row = 0
        determinant = 0
        # Main for
        for not_column in range(len(matrix)):
            sub_matrix = []
            for i in range(len(matrix)):
                new_row = []
                for j in range(len(matrix[i])):
                    if i != not_row and j != not_column:
                        new_row.append(matrix[i][j])
                if len(new_row) != 0:
                    sub_matrix.append(new_row)
            determinant += (matrix[not_row][not_column]
                            * (-1) ** ((not_row + 1) + (not_column + 1))) * find_determinant(sub_matrix)
        return determinant


def get_adjacent_matrix(matrix):
    row_len = len(matrix)
    column_len = len(matrix[0])
    new_matrix = [[0 for x in range(row_len)] for y in range(column_len)]
    for not_row in range(len(matrix)):
        for not_column in range(len(matrix)):
            sub_matrix = []
            for i in range(len(matrix)):
                new_row = []
                for j in range(len(matrix[i])):
                    if i != not_row and j != not_column:
                        new_row.append(matrix[i][j])
                if len(new_row) != 0:
                    sub_matrix.append(new_row)
            new_matrix[not_row][not_column] = ((-1) ** ((not_row + 1) + (not_column + 1))) * find_determinant(sub_matrix)
    new_matrix = shuffle_matrix(new_matrix)
    return new_matrix


def generate_inverse_matrix(matrix):
    determinant = find_determinant(matrix)
    adjacent_matrix = get_adjacent_matrix(matrix)
    inverse_matrix = multiply_matrix_by_constant(adjacent_matrix,  (1 / determinant))
    print_matrix_result(inverse_matrix)


def find_determinant_menu():
    generated_matrix, n, m = generate_matrix()
    result = find_determinant(generated_matrix)
    print("The result is:")
    print(result)


def print_main_menu():
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')


def print_transpose_menu():
    print('1. Main diagonal')
    print('2. Side diagonal')
    print('3. Vertical line')
    print('4. Horizontal line')


def execute_choice(ce):
    if ce == '1':
        add_matrices()
        print()
    elif ce == '2':
        generated_matrix, n, m = generate_matrix()
        multiplier = float(input("Enter constant: "))
        product = multiply_matrix_by_constant(generated_matrix, multiplier)
        print_matrix_result(product)
        print()
    elif ce == '3':
        multiply_matrices()
        print()
    elif ce == '4':
        print_transpose_menu()
        ce_input = input()
        if ce_input == '1':
            transpose_main_diagonal()
            print()
        elif ce_input == '2':
            transpose_side_diagonal()
            print()
        elif ce_input == '3':
            transpose_vertical_line()
            print()
        elif ce_input == '4':
            transpose_horizontal_line()
            print()
    elif ce == '5':
        find_determinant_menu()
        print()
    elif ce == '6':
        generated_matrix, n, m = generate_matrix()
        generate_inverse_matrix(generated_matrix)
        print()
    elif ce == '0':
        pass


choice = ''
while choice != '0':
    print_main_menu()
    choice = input()
    execute_choice(choice)


