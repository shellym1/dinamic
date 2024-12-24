def maximal_rectangle(matrix):
    rows = len(matrix)
    if rows == 0:
        return 0

    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in range(rows):
        # Update the heights of each column based on the current row
        for col in range(cols):
            if matrix[row][col] == 1:
                heights[col] += 1
            else:
                heights[col] = 0

        # Use a stack to find the maximum area rectangle for the current row
        stack = []
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        # Pop remaining elements from stack to calculate their areas
        while stack:
            h = heights[stack.pop()]
            w = cols if not stack else cols - stack[-1] - 1
            max_area = max(max_area, h * w)

    return max_area