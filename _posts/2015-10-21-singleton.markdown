---
layout: post
title: Singleton
date: 2015-10-21 03:34:23.000000000 -04:00
type: post
published: true
status: publish
categories:
- OOD
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466665193;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1919;}i:1;a:1:{s:2:"id";i:1396;}i:2;a:1:{s:2:"id";i:442;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Singleton is a most widely used design pattern. If a class has and only has one instance at every moment, we call this design as singleton. For example, for class Mouse (not a animal mouse), we should design it in singleton. You job is to implement a getInstance method for given class, return the same instance of this class every time you call this method.</em></strong></p>
<p><a href="http://www.programmerinterview.com/index.php/design-pattern-questions/design-pattern-interview-question-part-2/">Read More</a><br />
[expand title="code"]</p>
<pre>
class Solution {
    /**
     * @return: The same instance of this class every time
     */
    
    private static volatile Solution instance = null;
    //Declaring a volatile Java variable means: The value of this variable will never be cached thread-locally: all reads and writes will go straight to "main memory"; Access to the variable acts as though it is enclosed in a synchronized block, synchronized on itself.
    private Solution() {
        
    }
    public static Solution getInstance() {
        // The whole point of this is to save resources by instantiating the Singleton only when it’s actually needed. This technique is commonly known as lazy loading, or deferred initialization.
        if (instance == null) {
            //Suppose there are two threads T1 and T2. Both comes to create instance and execute “instance==null”, now both threads have identified instance variable to null thus assume they must create an instance. They sequentially goes to synchronized block and create the instances. At the end, we have two instances in our application. This error can be solved using double-checked locking. This principle tells us to recheck the instance variable again in synchronized block in given below way:
            synchronized (Solution.class) {
                if (instance == null) {
                    instance = new Solution();
                }
            }
        }
        return instance;
    }
};
</pre>
<p>[/expand]</p>
