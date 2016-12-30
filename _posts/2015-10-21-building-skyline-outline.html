---
layout: post
title: Building skyline Outline
date: 2015-10-21 14:47:55.000000000 -04:00
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
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1467334677;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:609;}i:1;a:1:{s:2:"id";i:499;}i:2;a:1:{s:2:"id";i:936;}}}}
  _inbound_impressions_count: '0'
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given N buildings in a x-axis，each building is a rectangle and can be represented by a triple (start, end, height)，where start is the start position on x-axis, end is the end position on x-axis and height is the height of the building. Buildings may overlap if you see them from far away，find the outline of them. An outline can be represented by a triple, (start, end, height), where start is the start position on x-axis of the outline, end is the end position on x-axis and height is the height of the outline.</em></strong></p>
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
    public ArrayList<ArrayList<integer>> buildingOutline(int[][] buildings) {
        ArrayList<ArrayList<integer>> result = new ArrayList<ArrayList<integer>>();
        if (buildings == null || buildings.length == 0) return result;        
        ArrayList<height> heights = new ArrayList<height>();
        for (int[] building : buildings) {
            heights.add(new Height(building[0], -building[2]));
            heights.add(new Height(building[1], building[2]));
        }
        Collections.sort(heights, new Comparator<height>() {
            public int compare(Height h1, Height h2) {
                return h1.index != h2.index ? h1.index - h2.index : h1.height - h2.height; 
            }
        });
        PriorityQueue<integer> heap = new PriorityQueue<integer>(10, Collections.reverseOrder());
        heap.add(0);
        int prev_height = 0, prev_index = 0;
        for (Height h : heights) {
            if (h.height < 0) {
                heap.add(-h.height);
            } else {
                heap.remove(h.height);
            }
            int curr = heap.peek();
            if (curr != prev_height) {
                if (prev_height != 0) {
                    ArrayList<integer> list = new ArrayList<integer>();
                    list.add(prev_index);
                    list.add(h.index);
                    list.add(prev_height);
                    result.add(list);
                }
                prev_index = h.index;
                prev_height = curr;
            }
        }
        return result;
    }
}//http://www.lintcode.com/en/problem/building-outline/#
</integer></integer></integer></integer></height></height></height></integer></integer></integer></pre>
<p>[/expand]</p>
