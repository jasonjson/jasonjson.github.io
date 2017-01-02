---
layout: post
title: Cosine Similarity
date: 2015-10-21 03:00:50.000000000 -04:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Cosine similarity is a measure of similarity between two vectors of an inner product space that measures the cosine of the angle between them. The cosine of 0° is 1, and it is less than 1 for any other angle.</em></strong></p>


``` java
class Solution {
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: Cosine similarity.
     */
    public double cosineSimilarity(int[] A, int[] B) {
        // write your code here
        if (A == null || B == null || A.length == 0 || B.length == 0) return 2.0;
        if (A.length != B.length) return 2.0;
        
        int i = 0;
        double upper = 0.0, A_abs = 0.0, B_abs = 0.0;
        //double not int
        while (i < A.length) {
            upper += A[i] * B[i];
            i++;
        }
        
        for (int j = 0; j < A.length; j++) {
            A_abs += A[j] * A[j];
        }
        for (int j = 0; j < B.length; j++) {
            B_abs += B[j] * B[j];
        }
        double lower = Math.sqrt(A_abs) * Math.sqrt(B_abs);
        if (lower == 0.0) return 2.0;// bug: error check
        return upper / lower; 
    }
}
```
