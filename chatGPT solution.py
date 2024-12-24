import random
import unittest

#from dinamic.Alon import brute_force_maximal_rectangle

#gpt1
def findMaxMatrix(matrix):
    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0])
    height = [0] * (n + 1)
    ans = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                height[j] += 1
            else:
                height[j] = 0

        stack = [-1]
        for j in range(n + 1):
            while height[j] < height[stack[-1]]:
                h = height[stack.pop()]
                w = j - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(j)

    return ans




def findMaxMatrix1(matrix):
    m, n = len(matrix), len(matrix[0])
    max_area = 0

    # initialize the bit array
    heights = [0] * n

    # iterate over each row
    for i in range(m):
        # update the bit array
        for j in range(n):
            if matrix[i][j] == 0:
                heights[j] = 0
            else:
                heights[j] += 1

        # calculate the area of the largest sub-rectangle that ends at this row
        area = get_max_area(heights)
        max_area = max(max_area, area)

        # stop searching if we've found the largest sub-rectangle possible
        if max_area == m * n:
            break

    return max_area

def get_max_area(heights):
    heights.append(0)
    stack = [-1]
    max_area = 0

    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    heights.pop()
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

    def test_random_rectangle(self):
        rows = random.randint(1, 100)
        cols = random.randint(1, 100)
        rect_rows = random.randint(1, rows)
        rect_cols = random.randint(1, cols)
        rect_row = random.randint(0, rows - rect_rows)
        rect_col = random.randint(0, cols - rect_cols)
        matrix = [[1 if rect_row <= i < rect_row + rect_rows and rect_col <= j < rect_col + rect_cols else random.randint(0, 1) for j in range(cols)] for i in range(rows)]
        #matrix = [[0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        print(matrix)
        expected_area = rect_rows * rect_cols
        #expected_area = 14
        self.assertEqual(findMaxMatrix(matrix), expected_area)






