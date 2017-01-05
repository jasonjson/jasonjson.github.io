---
layout: post
title: Python notes
date: 2017-01-05 10:10
categories:
- notes
author: Jason
---

# Python Notes

## Regular expression
### Python Compatible Regex Tester

[Link](https://regex101.com/#python)

### Special characters:
* `.` (Dot.) In the default mode, this matches any character except a newline. If the DOTALL flag has been specified, this matches any character including a newline.

* `^` (Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.

* `$` Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline. foo matches both ‘foo’ and ‘foobar’, while the regular expression foo$ matches only ‘foo’. More interestingly, searching for foo.$ in 'foo1\nfoo2\n' matches ‘foo2’ normally, but ‘foo1’ in MULTILINE mode; searching for a single $ in 'foo\n' will find two (empty) matches: one just before the newline, and one at the end of the string.

* `*` Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible. ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.

* `+` Causes the resulting RE to match 1 or more repetitions of the preceding RE. ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.

* `?` Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.

* `\\` Either escapes special characters (permitting you to match characters like '*', '?', and so forth), or signals a special sequence

* `[]` Used to indicate a set of characters.

* `(?:...)` A non-capturing version of regular parentheses

* `(?P<name>...)` Similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name name.

* `\\d` When the UNICODE flag is not specified, matches any decimal digit; this is equivalent to the set [0-9]

* `\\D` When the UNICODE flag is not specified, matches any non-digit character; this is equivalent to the set [^0-9]. With UNICODE, it will match anything other than character marked as digits in the Unicode character properties database.

* `\\s` When the UNICODE flag is not specified, it matches any whitespace character.

* `\\S` When the UNICODE flag is not specified, matches any non-whitespace character.

* `\\w` When the LOCALE and UNICODE flags are not specified, matches any alphanumeric character and the underscore.

* `\\W` When the LOCALE and UNICODE flags are not specified, matches any non-alphanumeric character.

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

## \*args and \*\*kwargs

\*args is used to send a non-keyworded variable length argument list to the function.
\*\*kwargs allows you to pass keyworded variable length of arguments to a function.

## Decorators

[Read this](http://book.pythontips.com/en/latest/decorators.html)

## Object introspection

`dir` returns a list of attributes and methods belonging to an object.
`type` returns the type of an object.
`id` returns the unique ids of various objects.

## Virtual Environment

`Virtualenv` is a tool which allows us to make isolated python environments.
[Read this](http://book.pythontips.com/en/latest/virtual_environment.html)
