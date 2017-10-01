---
layout: post
title: Subarray Sum K
date: 2015-10-21 02:17:46.000000000 -04:00
tags:
- Leetcode
categories:
- Integer
author: Jason
---
<p><strong><em>Given an nonnegative integer array, find a subarray where the sum of numbers is k. Your code should return the index of the first number and the index of the last number.</em></strong></p>


``` java
public class solution {
    public static void main(String[] args) {
        int[] a = {1, 4, 0, 0, 3, 10, 5};;
        ArrayList<Integer> list = findSum(a,7);
        for(int n : list){
            System.out.println(n);
        }
    }

    public static ArrayList<Integer> findSum(int[] arr, int val){
        if(arr == null) return null;
        HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
        ArrayList<Integer> result = new ArrayList<Integer>();
        int sum = 0;
        for(int i = 0; i < arr.length; i++){
            sum += arr[i];
            if(sum == val){
                result.add(0);
                result.add(i);
                break;
            }else if(map.containsKey(sum-val)){
                result.add(map.get(sum-val) + 1);
                result.add(i);
                break;
            }else {
                map.put(sum,i);
            }
        }
        return result;
    }
}
```
