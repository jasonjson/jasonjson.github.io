---
layout: post
title: Recover Rotated Sorted Array
date: 2015-10-21 02:19:02.000000000 -04:00
tags:
- Algorithm
categories:
- Sorting
author: Jason
---
<p><strong><em>Given a rotated sorted array, recover it to sorted array in-place.</em></strong></p>


``` java
public class Solution {
    /**
     * @param nums: The rotated sorted array
     * @return: void
     */
    public void recoverRotatedSortedArray(ArrayList<integer> nums) {
        // write your code
        int len = nums.size();
        int index = 0;
        while(index < len-1 && nums.get(index) <= nums.get(index+1)){
        //the element can be the same, so <= is important
            index++;
        }
        reverseUtil(nums,0,index);
        reverseUtil(nums,index+1,len-1);
        reverseUtil(nums,0,len-1);
    }
    //reverse an arraylist
    public void reverseUtil(ArrayList<integer> nums, int lo, int hi){
        if(lo > hi) return;
        for(int i = lo; i <= hi; i++){
            nums.add(i,nums.remove(hi));
        }
    }
}
```
