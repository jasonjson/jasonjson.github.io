---
layout: post
title: Largest Rectangle in Histogram
date: 2015-10-26 22:24:05.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Dynamic Programming
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463105500;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1482;}i:1;a:1:{s:2:"id";i:587;}i:2;a:1:{s:2:"id";i:589;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.</em></strong></p>
<p><a href="http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html">See detailed explanation</a><br />
<a href="http://www.geeksforgeeks.org/largest-rectangle-under-histogram/">Read more</a><br />
[expand title="O(n^2)"]</p>
<pre>
public class Solution {
    /**
     * @param height: A list of integer
     * @return: The area of largest rectangle in the histogram
     */
    public int largestRectangleArea(int[] height) {
        // write your code here
        if (height == null || height.length == 0) return 0;
        
        int n = height.length, max = 0;
        for (int i = 0; i < n; i++) {
            if(i > 0 && height[i] <= height[i-1]) {//优化剪枝
                continue;
            }
            int min = height[i];
            for (int j = i; j < n; j++) {//往右边边遍历,求区间[i,j]内的最大值
                min = Math.min(min, height[j]);
                max = Math.max(max, min * (j - i + 1));//以j为界当前最短的高度*长度，min * (i - j + 1) 相当于local_max，必须包括height[j]在内
            }
        }
        return max;
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title ="O(n)"]</p>
<p>&lt;</p>
<p>pre><br />
public class Solution {<br />
    public int largestRectangleArea(int[] height) {<br />
        if (height == null || height.length == 0) return 0;</p>
<pre><code>    int area = 0, n = height.length;
    Stack&lt;Integer&gt; stack = new Stack&lt;Integer&gt;();
    for (int i = 0; i &lt; n; i++) {
        while (!stack.isEmpty() &amp;&amp; height[i] &lt; height[stack.peek()]) {
            area = Math.max(area, height[stack.pop()] * (stack.isEmpty() ? i : i - stack.peek() - 1));
        }
        stack.push(i);
    }
    while (!stack.isEmpty()) {
        area = Math.max(area, height[stack.pop()] * (stack.isEmpty() ? n : n - stack.peek() - 1));
    }
    return area;
}
</code></pre>
<p>}/pre></p>
<p>[/expand]</p>
