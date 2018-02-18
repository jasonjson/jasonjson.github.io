---
layout: post
title: 158 - Read N Characters Given Read4 II - Call multiple times
date: 2015-11-05 18:27:33.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**The API: int read4(char *buf) reads 4 characters at a time from a file. The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file. By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file. Note: The read function may be called multiple times.**


``` java
/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    private int buffPtr = 0;
    private int buffCnt = 0;
    private char[] buff = new char[4];
    public int read(char[] buf, int n) {
        int ptr = 0;
        while (ptr < n) {
            if (buffPtr == 0) {
                buffCnt = read4(buff);
            }
            if (buffCnt == 0) break;
            while (ptr < n && buffPtr < buffCnt) {
                buf[ptr++] = buff[buffPtr++];
            }
            if (buffPtr >= buffCnt) buffPtr = 0;
        }
        return ptr;
    }
}
```

``` python
class Solution(object):

    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        while True:
            tmp = [""] * 4
            read4(tmp)
            self.queue.extend(tmp)
            curr = min(len(self.queue), n - index)
            for _ in xrange(curr):
                buf[index] = self.queue.pop(0)
                index += 1
            if curr == 0:
                break
        return index
```
