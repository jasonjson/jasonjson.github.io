---
layout: post
title: The Skyline Problem
date: 2015-10-21 14:47:31.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466796055;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:611;}i:1;a:1:{s:2:"id";i:1652;}i:2;a:1:{s:2:"id";i:107;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    class Height {
        int index, height;
        Height (int index, int height) {
            this.index = index;
            this.height = height;
        }
    }
    public List<int[]> getSkyline(int[][] buildings) {
        List<int[]> result = new ArrayList<int[]>();
        if (buildings == null || buildings.length == 0) return result;        
        ArrayList<height> heights = new ArrayList<height>();
        for (int[] building : buildings) {
            heights.add(new Height(building[0], - building[2]));
            heights.add(new Height(building[1], building[2]));
        }
        Collections.sort(heights, new Comparator<height>() {
            public int compare(Height a, Height b) {
                return a.index == b.index ? a.height - b.height : a.index - b.index;
            }
        });
        PriorityQueue<integer> heap = new PriorityQueue<integer>(10, Collections.reverseOrder());
        heap.offer(0);
        int prev = 0;
        for (Height h : heights) {
            if (h.height < 0) {
                heap.offer(-h.height);
            } else {
                heap.remove(h.height);
            }
            int curr = heap.peek();
            if (curr != prev) {//merge same height points
                result.add(new int[] {h.index, curr});
                prev = curr;
            }
        }
        return result;
    }
}//http://codechen.blogspot.com/2015/06/leetcode-skyline-problem.html
</integer></integer></height></height></height></pre>
<p>[/expand]</p>
