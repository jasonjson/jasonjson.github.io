---
layout: post
title: Find best container
date: 2015-12-12 13:02:39.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Two Pointers
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468314774;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:73;}i:1;a:1:{s:2:"id";i:587;}i:2;a:1:{s:2:"id";i:141;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>現在給某個容量(double capacity), 還有一個array(double[] weights), 和int numOfContainers 主要是要在array中選出兩個weights總和小於等於capacity但最接近capacity.然後指定到一個Container object並且return</em></strong></p>
<p>[expand title="code"]</p>
<pre>
class Solution {
    public static void main(String[] args) {
        double[] weights = {0.1, 2.3784, 3.2541, 9.2589, 5.3451, 6.79322, 5.3478};
        Container c = findOptimalWeight(weights, 15.0);
        System.out.println(c.first + "," + c.second);
    }
    static class Container {
        double first, second;
        public Container(int first, int second){
            this.first = first;
            this.second = second;
        }
    }
    public static Container findOptimalWeight(double[] weights, double target) {
        Container result = new Container(0, 0);
        if (weights == null || weights.length < 2) return result;

        Arrays.sort(weights);
        int lo = 0, hi = weights.length - 1, first = lo, second = hi;
        while (lo < hi) {
            if (weights[lo] + weights[hi] == target) {
                first = lo;
                second = hi;
                break;
            } else if (weights[lo] + weights[hi] > target) {
                hi --;
            } else {
                if (target < weights[first] + weights[second] || target - (weights[first] + weights[second]) > target - (weights[lo] + weights[hi])) {
                    first = lo;
                    second = hi;
                }
                lo ++;
            }
        }
        result.first = weights[first];
        result.second = weights[second];
        return result;
    }
}
</pre>
<p>[/expand]</p>
