---
layout: post
title: Top k elements with most occurrences
date: 2016-01-19 17:16:33.000000000 -05:00
tags: algorithm
categories:
- Data Structure
author: Jason
---
<p><strong><em>Find k elements within a array with most occurrences.</em></strong></p>


``` java
public class Solution {
    public static void main(String[] args) {
        int[] nums = {1,1,2,2,3,3,3,4,5,6,6,6,6,6,7,7,7,8,8,8,8,9,10,11,12,13,14,15,15};
        System.out.println(get(nums, 3));
    }
    public static List<integer> get(int[] nums, int k) {
        List<integer> result = new ArrayList<>();
        if (nums == null || nums.length == 0 || k == 0) return result;


        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        System.out.println(map);
        PriorityQueue<integer> pq = new PriorityQueue<>(k, new Comparator<integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return map.get(o1) - map.get(o2);//不用造class来储存值和次数
            }
        });
        for (int key : map.keySet()) {
            if (pq.size() == k) {
                if (map.get(pq.peek()) < map.get(key)) {
                    pq.poll();
                    pq.offer(key);
                }
            } else {
                pq.offer(key);
            }
        }
        while (!pq.isEmpty()) {
            result.add(pq.poll());
        }
        return result;
    }
}
```
