---
layout: post
title: Number of Airplanes in the Sky
date: 2015-10-21 14:33:58.000000000 -04:00
tags:
- Algorithm
categories:
- Brain teaser
- Data Structure
author: Jason
---
<p><strong><em>Given an interval list which are flying and landing time of the flight. How many airplanes are on the sky at most?</em></strong></p>


``` java
//wrong, this is answer for how many airplanes are on the sky at least
class Solution {
    public static int count(List<interval> airplanes) {
        if (airplanes == null || airplanes.size() == 0) return 0;

        Collections.sort(airplanes, new Comparator<interval>() {
            public int compare(Interval a, Interval b) {
                return a.start - b.start;
            }
        });
        PriorityQueue<integer> pq = new PriorityQueue<integer>();
        for (Interval interval : airplanes) {
            if (!pq.isEmpty() && interval.start >= pq.peek()) {
                pq.poll();
            }
            pq.offer(interval.end);
        }
        return pq.size();
    }
}
```
``` java
//起飞是(,降落是),最多有多少对正确的括号组合
class Solution {
    /**
     * @param intervals: An interval array
     * @return: Count of airplanes are in the sky.
     */
    public class point {
        int time, flag;
        public point(int time, int flag) {
            this.time = time;
            this.flag = flag;
        }
    }
    public int countOfAirplanes(List<interval> airplanes) { 
        // write your code here
        if (airplanes == null || airplanes.size() == 0) return 0;
        
        List<point> list = new ArrayList<point>();
        for (Interval interval : airplanes) {
            list.add(new point(interval.start, 1)); //flying is 1
            list.add(new point(interval.end, 0)); //landing is 0
        }
        Collections.sort(list, new Comparator<point>() {
            public int compare (point a, point b) {
                return a.x == b.x ? a.flag - b.flag : a.x - b.x;
                //landing happen first
            }
        });
        int result = 0, count = 0;
        for (point p : list) {
            if (p.flag == 1) {
                count ++;
            } else {
                count --;
            }
            result = Math.max(count, result);
        }
        return result;
    }//http://www.cnblogs.com/easonliu/p/4504647.html
}
```
