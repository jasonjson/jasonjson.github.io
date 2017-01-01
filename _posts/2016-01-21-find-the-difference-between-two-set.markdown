---
layout: post
title: Find the difference between two set
date: 2016-01-21 11:30:59.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468447758;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:2049;}i:1;a:1:{s:2:"id";i:105;}i:2;a:1:{s:2:"id";i:206;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>找出两个数组的差，比如A = [1,1,1,2,2,2], B= [2,2,3]，在A出现在B不出现的集合是[1,1,1,2]， 在B出现在A    不出现的集合是[3]</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public static void main(String[] args) {
        List<integer> A = new ArrayList<>(Arrays.asList(1,1,1,2,2,2));
        List<integer> B = new ArrayList<>(Arrays.asList(2,2,3));
        System.out.println(findSubset(B, A));
        System.out.println(findSubset(A, B));
    }
    public static List<integer> findSubset(List<integer> A, List<integer> B) {
        List<integer> result = new ArrayList<>();
        if (A.size() == 0) return result;
        if (B.size() == 0) {
            result.addAll(A);
            return result;
        }
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : A) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (int num : B) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) - 1);
            }
        }
        for (int num : map.keySet()) {
            for (int i = 0; i < map.get(num); i++) {
                result.add(num);
            }
        }
        return result;
    }
}
</integer></integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
