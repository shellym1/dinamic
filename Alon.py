import random
import unittest

#gpt3
def findMaxMatrix(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        stack = [-1]
        for j in range(cols):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[j]:
                h = heights[stack.pop()]
                w = j - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(j)

        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = cols - stack[-1] - 1
            max_area = max(max_area, h * w)

    return max_area






def brute_force_maximal_rectangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                k = j
                while k < cols and matrix[i][k] == 1:
                    k += 1
                l = i
                while l < rows and matrix[l][j] == 1:
                    l += 1
                area = (k - j) * (l - i)
                if area > max_area:
                    max_area = area
    return max_area


class MaximumSizeRectangleBinarySubmatrixTests(unittest.TestCase):
    def setUp(self):
        self.small_matrix = [[0, 1], [1, 0]]
        self.large_matrix = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]
        self.all_zeros = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.all_ones = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    def test_small_matrix(self):
        self.assertEqual(findMaxMatrix(self.small_matrix), 1)

    def test_large_matrix(self):
        self.assertEqual(findMaxMatrix(self.large_matrix), 8)

    def test_all_zeros(self):
        self.assertEqual(findMaxMatrix(self.all_zeros), 0)

    def test_all_ones(self):
        self.assertEqual(findMaxMatrix(self.all_ones), 9)
    #
    # def test_random_inputs(self):
    #     for i in range(10):
    #         rows = random.randint(1, 100)
    #         cols = random.randint(1, 100)
    #         matrix = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
    #         expected_area = brute_force_maximal_rectangle(matrix)
    #         self.assertEqual(findMaxMatrix(matrix), expected_area)

    def test_random_rectangle(self):
        rows = random.randint(1, 100)
        cols = random.randint(1, 100)
        rect_rows = random.randint(1, rows)
        rect_cols = random.randint(1, cols)
        rect_row = random.randint(0, rows - rect_rows)
        rect_col = random.randint(0, cols - rect_cols)
        #matrix = [[1 if rect_row <= i < rect_row + rect_rows and rect_col <= j < rect_col + rect_cols else random.randint(0, 1) for j in range(cols)] for i in range(rows)]
        matrix = [[0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        print(matrix)
        #expected_area = rect_rows * rect_cols
        expected_area = 14
        self.assertEqual(findMaxMatrix(matrix), expected_area)




