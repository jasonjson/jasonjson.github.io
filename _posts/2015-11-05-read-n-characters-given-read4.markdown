---
layout: post
title: 157 - Read N Characters Given Read4
date: 2015-11-05 17:42:58.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**The API: int read4(char *buf) reads 4 characters at a time from a file. The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file. By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.**


``` java
public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    public int read(char[] buf, int n) {
        char[] tmp = new char[4];
        int i = 0, num = 4;
        while(i < n && num == 4){
            num = read4(tmp);
            for(int j = 0; j < num && i < n; j++){
                buf[i++] = tmp[j];
            }
        }
        return i;
    }
}
```

``` python
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        index = 0
        tmp = [""] * 4
        while True:
            new_read = read4(tmp)
            curr = min(new_read, n - index)
            for i in xrange(curr):
                buf[index] = tmp[i]
                index += 1
            if curr == 0:
                break
        return index
```
