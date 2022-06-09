---
layout: post
title: 346 - Moving Average From Data Stream
date: 2022-06-09
tags:
- Leetcode
categories:
- data structure
author: Jason
---
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

* MovingAverage(int size) Initializes the object with the size of the window size.
* double next(int val) Returns the moving average of the last size values of the stream.

```cpp
class MovingAverage {
public:
    queue<int> nums;
    int windowSize;
    double sum;
    MovingAverage(int size) {
        windowSize = size;
        sum = 0;
    }

    double next(int val) {
        if (nums.size() == windowSize) {
            sum -= nums.front();
            nums.pop();
        }
        nums.push(val);
        sum += val;
        return sum / nums.size();
    }
};

```
