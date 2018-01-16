---
layout: post
title: 85 - Maximal Rectangle
date: 2015-11-12 18:23:08.000000000 -05:00
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.**


``` java
public class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0) return 0;

        int row = matrix.length, col = matrix[0].length, max = 0;
        int[] left = new int[col], right = new int[col], height = new int[col];
        Arrays.fill(right, col);//!!fill the right array

        for (int i = 0; i < row; i++) {
            int curr_left = 0, curr_right = col - 1;
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == '1') {
                    height[j] ++;
                } else {
                    height[j] = 0;
                }
            }

            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == '1') {
                    left[j] = Math.max(left[j], curr_left);
                } else {
                    left[j] = 0;
                    curr_left = j + 1;
                }
            }

            for (int j = col - 1; j >= 0; j--) {
                if (matrix[i][j] == '1') {
                    right[j] = Math.min(right[j], curr_right);
                } else {
                    right[j] = col - 1;
                    curr_right = j - 1;
                }
            }

            for (int j = 0; j < col; j++) {
                max = Math.max(max, height[j] * (right[j] - left[j] + 1));
            }
        }
        return max;
    }
}
```

``` java
public class Solution {
    //We can apply the maximum in histogram in each row of the 2D matrix.
    //What we need is to maintain an int array for each row, which represent
    //for the height of the histogram.
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0) return 0;

        int row = matrix.length, col = matrix[0].length, max = 0;
        int[] height = new int[col];
        for (int j = 0; j < col; j++) {
            if (matrix[0][j] == '1') {
                height[j] = 1;
            }
        }
        max = getArea(height);
        for (int i = 1; i < row; i++) {
            reset(matrix, height, i);
            max = Math.max(max, getArea(height));
        }
        return max;
    }

    public void reset(char[][] matrix, int[] height, int row) {
        for (int j = 0; j < height.length; j ++) {
            if (matrix[row][j] == '1') {
                height[j] += 1;
            } else {
                height[j] = 0;
            }
        }
    }

    public int getArea(int[] height) {
        Stack<Integer> stack = new Stack<Integer>();
        int area = 0;
        for (int i = 0; i < height.length; i++) {
            while (!stack.isEmpty() && height[i] < height[stack.peek()]) {
                area = Math.max(area, height[stack.pop()] * (i - (stack.isEmpty() ? 0 : stack.peek() + 1)));
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            area = Math.max(area, height[stack.pop()] * (height.length - (stack.isEmpty() ? 0 : stack.peek() + 1)));
        }
        return area;
    }
}
```
