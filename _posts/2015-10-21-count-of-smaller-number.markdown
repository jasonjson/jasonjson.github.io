---
layout: post
title: Count of Smaller Number
date: 2015-10-21 13:32:46.000000000 -04:00
categories:
- Sorting
- Subarray
author: Jason
---
<p><strong><em>Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) and an query list. For each query, give you an integer, return the number of element in the array that are smaller that the given integer.</em></strong></p>

``` java
public class Solution {
   /**
     * @param A: An integer array
     * @return: The number of element in the array that 
     *          are smaller that the given integer
     */
     
    class segmentTreeNode {
        int start, end, count;
        segmentTreeNode left, right;
        segmentTreeNode(int start, int end, int count) {
            this.start = start;
            this.end = end;
            this.count = count;
            this.left = null;
            this.right = null;
        }
    }
    public ArrayList<integer> countOfSmallerNumber(int[] A, int[] queries) {
        // write your code here
        ArrayList<integer> result = new ArrayList<integer>();
        
        segmentTreeNode root = build(0, 10000);
        for (int n : A) {
            update(root, n);
        }
        for (int n : queries) {
            result.add(query(root, 0, n - 1));
        }
        return result;
    }
    
    public segmentTreeNode build(int start, int end) {
        if (start > end) return null;
        if (start == end) return new segmentTreeNode(start, end, 0);//base case
        segmentTreeNode root = new segmentTreeNode(start, end, 0);
        int mid = (start + end) / 2;
        root.left = build(start, mid);
        root.right = build(mid + 1, end);
        root.count = root.left.count + root.right.count;
        return root;
    }
    public int query(segmentTreeNode root, int start, int end) {
        if (start > end) return 0;
        if (root.start == start && root.end == end) return root.count;
        int mid = (root.start + root.end) / 2;
        if (end < mid) {
            return query(root.left, start, end);
        } else if (start > mid) {
            return query(root.right, start, end);
        } else {
            return query(root.left, start, mid) + query(root.right, mid + 1, end);
        }
    }
    public void update(segmentTreeNode root, int val) {
        if (root == null) return;
        if (root.start == val && root.end == val) {
            root.count ++;
            return;
        }
        int mid = (root.start + root.end) / 2;
        if (val <= mid) {
            update(root.left, val);
        } else {
            update(root.right, val);
        }
        root.count = root.left.count + root.right.count;
    }
}
```
``` java
public class Solution {
   /**
     * @param A: An integer array
     * @return: The number of element in the array that 
     *          are smaller that the given integer
     */
    public ArrayList<integer> countOfSmallerNumber(int[] A, int[] queries) {
        ArrayList<integer> result = new ArrayList<integer>();

        Arrays.sort(A);
        for (int i = 0; i < queries.length; i++) {
            result.add(find(A, queries[i]));
        }
        return result;
    }
    
    public int find(int[] A, int val) {
        int lo = 0, hi = A.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (A[mid] == val) {
            //there can be duplicates in the array, find the first index of the val
                while (mid - 1 >= 0 && A[mid - 1] == val) {
                    mid --;
                }
                return mid;
            } else if (A[mid] < val) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
}
```
