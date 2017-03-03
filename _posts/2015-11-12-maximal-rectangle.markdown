---
layout: post
title: Maximal Rectangle
date: 2015-11-12 18:23:08.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.</em></strong></p>


<p>If you think this algorithm is not easy to understand, you can try this example:</p>
<p>0 0 0 1 0 0 0</p>
<p>0 0 1 1 1 0 0</p>
<p>0 1 1 1 1 1 0</p>
<p>The vector "left" and "right" from row 0 to row 2 are as follows</p>
<p>row 0:</p>
<p>l: 0 0 0 3 0 0 0</p>
<p>r: 7 7 7 4 7 7 7</p>
<p>row 1:</p>
<p>l: 0 0 2 3 2 0 0</p>
<p>r: 7 7 5 4 5 7 7</p>
<p>row 2:</p>
<p>l: 0 1 2 3 2 1 0</p>
<p>r: 7 6 5 4 5 6 7</p>
<p>The vector "left" is computing the left boundary. Take (i,j)=(1,3) for example. On current row 1, the left boundary is at j=2. However, because matrix[1][3] is 1, you need to consider the left boundary on previous row as well, which is 3. So the real left boundary at (1,3) is 3.</p>
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
        Stack<integer> stack = new Stack<integer>();
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
