---
layout: post
title: Python notes
date: 2017-01-05 10:10
tags:
- Python
categories:
- Reading Notes
author: Jason
---
**Python notes**

### Regular expression
1. Python Compatible Regex Tester
[Link](https://regex101.com/#python)
2. Special characters:
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
    * `\d` When the UNICODE flag is not specified, matches any decimal digit; this is equivalent to the set [0-9]
    * `\D` When the UNICODE flag is not specified, matches any non-digit character; this is equivalent to the set [^0-9]. With UNICODE, it will match anything other than character marked as digits in the Unicode character properties database.
    * `\s` When the UNICODE flag is not specified, it matches any whitespace character.
    * `\S` When the UNICODE flag is not specified, matches any non-whitespace character.
    * `\w` When the LOCALE and UNICODE flags are not specified, matches any alphanumeric character and the underscore.
    * `\W` When the LOCALE and UNICODE flags are not specified, matches any non-alphanumeric character.

### Function caching
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
We can easily uncache the return values as well by using: `fib.cache_clear()`. [Here](https://www.caktusgroup.com/blog/2015/06/08/testing-client-side-applications-django-post-mortem/) is a fine article by Caktus Group in which they caught a bug in Django which occurred due to `lru_cache`

### File handlers
  * `r`   Open text file for reading. The stream is positioned at the beginning of the file.
  * `r+`  Open for reading and writing. The stream is positioned at the beginning of the file.
  * `w`   Truncate file to zero length or create text file for writing. The stream is positioned at the beginning of the file.
  * `w+`  Open for reading and writing. The file is created if it does not exist, otherwise it is truncated.  The stream is positioned at the beginning of the file.
  * `a`   Open for writing. The file is created if it does not exist. The stream is positioned at the end of the file.  Subsequent writes to the file will always end up at the then current end of file, irrespective of any intervening fseek(3) or similar.
  * `a+`  Open for reading and writing. The file is created if it does not exist.  The stream is positioned at the end of the file.  Subsequent writes to the file will always end up at the then current end of file, irrespective of any intervening fseek(3) or similar.'

### \*args and \*\*kwargs
* `*args` is used to send a non-keyworded variable length argument list to the function.
* `**kwargs` allows you to pass keyworded variable length of arguments to a function.

### Decorators
[Read this](http://book.pythontips.com/en/latest/decorators.html)

### Object introspection
* `dir` returns a list of attributes and methods belonging to an object.
* `type` returns the type of an object.
* `id` returns the unique ids of various objects.

### Virtual Environment
* `Virtualenv` is a tool which allows us to make isolated python environments.
[Read this](http://book.pythontips.com/en/latest/virtual_environment.html)

### OS related:
* `os.path.join(path, *paths)` Join one or more path components intelligently. The return value is the concatenation of path and any members of *paths with exactly one directory separator.
* `os.walk(top, topdown=True, onerror=None, followlinks=False)` - Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
* `os.path.isdir` - Return True if path is an existing directory.
* `os.path.abspath` - Return a normalized absolutized version of the pathname path.
* `os.path.basename` - Return the base name of pathname path.
* `os.path.exists` - Return True if path refers to an existing path.
* `os.mkdir` - Create a directory named path with numeric mode mode. The default mode is 0777 (octal).
* `os.makedirs` - Recursive directory creation function.

### Built-in methods
* `filter` - Construct an iterator from those elements of iterable for which function returns true. Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)).
* `chr` - Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a'. This is the inverse of ord().
* `oct` - Convert an integer number to an octal string.
* `hex` - Convert an integer number to a lowercase hexadecimal string prefixed with “0x”
* `ord` - Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
* `id` - Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime.
* `isinstance` - Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof.
* `map` - Return an iterator that applies function to every item of iterable, yielding the results.
* `abs` - Return the absolute value of a number.
* `max` - Return the largest item in an iterable or the largest of two or more arguments.
* `min` - Return the smallest item in an iterable or the smallest of two or more arguments.
* `next` - Retrieve the next item from the iterator by calling its __next__() method.
s is the inverse of ord().
* `pow` - Return x to the power y.
* `property` - Return a property attribute. [read more](https://docs.python.org/3/library/functions.html)
* `reversed` - Return a reverse iterator.
* `sorted` - Return a new sorted list from the items in iterable.
* `sum` - Sums start and the items of an iterable from left to right and returns the total.
* `zip` - Make an iterator that aggregates elements from each of the iterables. Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.
