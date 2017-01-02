---
layout: post
title: Read N Characters Given Read4 II - Call multiple times
date: 2015-11-05 18:27:33.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>The API: int read4(char *buf) reads 4 characters at a time from a file.</p>

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.</p>
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.</p>
Note:</p>
The read function may be called multiple times.</em></strong></p>
``` java
/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    //use buffer pointer (buffPtr) and buffer Counter (buffCnt) to store the data received in previous calls. In the while loop, if buffPtr reaches current buffCnt, it will be set as zero to be ready to read new data.
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
