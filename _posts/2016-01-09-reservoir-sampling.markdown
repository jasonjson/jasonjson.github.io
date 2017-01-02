---
layout: post
title: Reservoir Sampling
date: 2016-01-09 10:29:27.000000000 -05:00
categories:
- Brain teaser
- Data Structure
author: Jason
---
<p><strong><em>Reservoir sampling is a family of randomized algorithms for randomly choosing k samples from a list of n items, where n is either a very large or unknown number.</em></strong></p>


<p><a href="http://www.geeksforgeeks.org/reservoir-sampling/">read more</a></p>

``` java
public class Solution {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7,8,9,10};
        randamPick(arr,4);
        randamPick(arr,4);
        randamPick(arr,4);
        randamPick(arr,4);
        randamPick(arr,4);
    }

    public static int[] randamPick(int[] arr, int k) {
        int[] result = new int[k];
        int i = 0;
        for (; i < k; i++) {
            result[i] = arr[i];
        }
        Random rand = new Random();
        for (; i < arr.length; i++) {            
            int j = rand.nextInt(i + 1);
            if (j < k) {
                result[j] = arr[i];
            }
        }
        for (int num : result) {
            System.out.print(num + ",");
        }
        System.out.println();
        return result;
    }
}
```
``` java
import java.util.Random;

/**
 * Returns a pseudo-random number between min and max, inclusive.
 * The difference between min and max can be at most
 * <code>MARKDOWN_HASH3f3ef32e712257154e7e45593a71c6bcMARKDOWN_HASH</code>.
 *
 * @param min Minimum value
 * @param max Maximum value.  Must be greater than min.
 * @return Integer between min and max, inclusive.
 * @see java.util.Random#nextInt(int)
 */
public static int randInt(int min, int max) {

    // NOTE: This will (intentionally) not run as written so that folks
    // copy-pasting have to think about how to initialize their
    // Random instance.  Initialization of the Random instance is outside
    // the main scope of the question, but some decent options are to have
    // a field that is initialized once and then re-used as needed or to
    // use ThreadLocalRandom (if using at least Java 1.7).
    Random rand = new Random();

    // nextInt is normally exclusive of the top value,
    // so add 1 to make it inclusive
    int randomNum = rand.nextInt((max - min) + 1) + min;

    return randomNum;
}
```
