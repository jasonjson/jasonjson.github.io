---
layout: post
title: Gas Station
date: 2015-10-21 14:14:07.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>There are N gas stations along a circular route, where the amount of gas at station i is gas[i]. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations. Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.</em></strong></p>


``` java
//Whenever the sum is negative, reset it and let the car start from next point.
//In the mean time, add up all of the left gas to total. If it's negative finally, return -1 since //it's impossible to finish.
//If it's non-negative, return the last point saved in res;
public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0, sum = 0, index = 0;
        for (int i = 0; i < gas.length; i ++) {
            sum += gas[i] - cost[i];
            if (sum < 0) {
                total += sum;
                sum = 0;
                index = i + 1;
            }
        }
        total += sum;
        if (total < 0) {
            return -1;
        } else {
            return index;
        }
    }
}
```

``` java
public class Solution {
    /**
     * @param gas: an array of integers
     * @param cost: an array of integers
     * @return: an integer
     */
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // write your code here
        if (gas.length == 0 || cost.length == 0) return -1;
        
        for (int i = 0; i < gas.length; i++) {
            int left_gas = 0, k = 0;;
            for (; k < gas.length; k++) {
                int index = (k + i) % gas.length;
                left_gas += gas[index] - cost[index];
                if (left_gas < 0) break; // 可以等于0，走到加油站正好加油
            }
            if (k == gas.length) return i;
            i += k;
        }
        return -1;
    }
}
```
