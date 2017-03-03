---
layout: post
title: Read N Characters Given Read4
date: 2015-11-05 17:42:58.000000000 -05:00
tags: algorithm
categories:
- Brain teaser
author: Jason
---
<p><strong><em>The API: int read4(char *buf) reads 4 characters at a time from a file.</p>

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.</p>
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.</em></strong></p>
``` java
public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    public int read(char[] buf, int n) {//从一个别的file读入char放入buf中
        char[] tmp = new char[4];
        int i = 0, num = 4;
        while(i < n && num == 4){//当上次num != 4说明文件已经读完了
            num = read4(tmp);
            for(int j = 0; j < num && i < n; j++){//最多放n个char进去
                buf[i++] = tmp[j];
            }
        }
        return i;//i starts from 0, so return i though i++ afterwards
    }
}
```
