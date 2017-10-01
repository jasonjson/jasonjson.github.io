---
layout: post
title: Hash Function
date: 2015-10-21 02:37:58.000000000 -04:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
<p><strong><em>In data structure Hash, hash function is used to convert a string(or any other type) into an integer smaller than hash size and bigger or equal to zero. The objective of designing a hash function is to "hash" the key as unreasonable as possible. A good hash function can avoid collision as less as possible. A widely used hash function algorithm is using a magic number 33, consider any string as a 33 based big integer like follow:</em></strong></p>


``` java
class Solution {
    /**
     * @param key: A String you should hash
     * @param HASH_SIZE: An integer
     * @return an integer
     */
    public int hashCode(char[] key,int HASH_SIZE) {
        // write your code here
        long sum = 0;
        //the hash value can be really large, we need to use long type
        for(int i = 0; i < key.length; i ++){
            sum = sum * 33 + key[i];
            //bug1 : sum += sum * 33 + key[i]
            //the way to doing power!! remember!!
            sum %= HASH_SIZE;
        }
        return (int)sum;
        //don't forget to change the type back to int
    }
};
```
