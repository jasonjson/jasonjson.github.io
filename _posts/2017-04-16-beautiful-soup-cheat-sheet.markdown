---
layout: post
title: Beautiful Soup Cheat Sheet
date: 2017-04-16
tags:
- Python
categories:
- Reading Notes
author: Jason
---
**Beautiful Soup Cheat Sheet**

### Navigating using tag name
* `.tag` - The simplest way to navigate the parse tree is to say the name of the tag you want. However, using a tag name as an attribute will give you only the first tag by that name.
* `.contents` - Gives a tag's children as a list. The BeautifulSoup object itself has one child <html> tag.
* `.children` - Gives a generator to iterate over a tag's children.
* `.descendants` - Lets you iterate over all of a tag’s children, recursively: its direct children, the children of its direct children, and so on.
* `.string` - If a tag has only one child, and that child is a NavigableString, the child is made available as .string. If a tag’s only child is another tag, and that tag has a .string, then the parent tag is considered to have the same .string as its child. f a tag contains more than one thing, then it’s not clear what .string should refer to, so .string is defined to be *None*.
* `.strings` - If there’s more than one thing inside a tag, you can still look at just the strings using this generator.
* `.stipped_strings` - Use this generator to remove extra white spaces.
* `.parent` - Access an element’s parent.
* `.parents` - Iterate over all of an element's parents
* `.next_sibling` and `.previous_sibling` - Navigate between page elements that are on the same level of the parse tree.
* `.next_siblings` and `.previous_siblings` - Iterate over a tag’s siblings.
* `.next_element` and `.previous_elements` - points to whatever was parsed immediately afterwards or before.

### Searching the tree
* Kinds of filters
    1. **string** Pass a string to a search method and Beautiful Soup will perform a match against that exact string.
    2. **regular expression** If you pass in a regular expression object, Beautiful Soup will filter against that regular expression using its match() method.
    3. **list** If you pass in a list, Beautiful Soup will allow a string match against any item in that list.
    4. **True** The value True matches everything it can.
    5. **function** Define a function that takes an element as its only argument. The function should return True if the argument matches, and False otherwise.
* `find_all` - The method looks through a tag’s descendants and retrieves all descendants that match your filters.
    1. **name** Pass in a value for name and you’ll tell Beautiful Soup to only consider tags with certain names.
    2. **keyword** Any argument that’s not recognized will be turned into a filter on one of a tag’s attributes.
    3. **class_** You can search by CSS class using the this keyword as argument.
    4. **string** You can search for strings instead of tags.
    5. **limit** If you don’t need all the results, you can pass in a number for limit.
    6. **recursive** If you only want Beautiful Soup to consider direct children, you can pass in recursive=False.
* `find` - Rather than passing in limit=1 every time you call find_all, you can use the find() method. The only difference is that find_all() returns a list containing the single result, and find() just returns the result. If find_all() can’t find anything, it returns an empty list. If find() can’t find anything, it returns None.
* `find_parents` and `find_parent` - These methods work their way up the tree, looking at a tag’s (or a string’s) parents.
* `find_next_siblings` and `find_next_sibling` - These methods use .next_siblings to iterate over the rest of an element’s siblings in the tree. The find_next_siblings() method returns all the siblings that match, and find_next_sibling() only returns the first one.
* `find_previous_siblings` and `find_previous_sibling` - These methods use .previous_siblings to iterate over an element’s siblings that precede it in the tree. The find_previous_siblings() method returns all the siblings that match, and find_previous_sibling() only returns the first one.

### Output
* `prettify` - turns a Beautiful Soup parse tree into a nicely formatted Unicode string, with each HTML/XML tag on its own line.
* `get_text()` - returns all the text in a document or beneath a tag, as a single Unicode string.

### Parsing only part of a document
* `SoupStrainer` - allows you to choose which parts of an incoming document are parsed. You just create a SoupStrainer and pass it in to the BeautifulSoup constructor as the parse_only argument.
