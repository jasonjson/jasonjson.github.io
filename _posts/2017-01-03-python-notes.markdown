---
layout: post
title: Github notes
date: 2017-01-05 10:10
categories:
- notes
author: Jason
---

# Python Notes

## Regular expression

## Function caching

In Python 3.2+ there is an `lru_cache` decorator which allows us to quickly cache and uncache the return values of a function.

``` python
from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2) 

>>> print([fib(n) for n in range(10)])
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

The `maxsize` argument tells `lru_cache` about how many recent return values to cache.

We can easily uncache the return values as well by using:

``` python
fib.cache_clear()
```
[Here](https://www.caktusgroup.com/blog/2015/06/08/testing-client-side-applications-django-post-mortem/) is a fine article by Caktus Group in which they caught a bug in Django which occurred due to `lru_cache`

## File handlers

  * **r**   Open text file for reading. The stream is positioned at the beginning of the file.

  * **r+**  Open for reading and writing. The stream is positioned at the beginning of the file.

  * **w**   Truncate file to zero length or create text file for writing. The stream is positioned at the beginning of the file.

  * **w+**  Open for reading and writing. The file is created if it does not exist, otherwise it is truncated.  The stream is positioned at the beginning of the file.

  * **a**   Open for writing. The file is created if it does not exist. The stream is positioned at the end of the file.  Subsequent writes to the file will always end up at the then current end of file, irrespective of any intervening fseek(3) or similar.

  * **a+**  Open for reading and writing. The file is created if it does not exist.  The stream is positioned at the end of the file.  Subsequent writes to the file will always end up at the then current end of file, irrespective of any intervening fseek(3) or similar.'
