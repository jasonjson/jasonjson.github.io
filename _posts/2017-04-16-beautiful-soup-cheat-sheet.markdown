---
layout: post
title: Beautiful Soup Cheat Sheet
date: 2017-04-16
tags:
- Python
categories:
- A note
author: Jason
---
**Beautiful Soup Cheat Sheet**

# Navigating using tag name
* `.tag` - The simplest way to navigate the parse tree is to say the name of the tag you want. However, using a tag name as an attribute will give you only the first tag by that name.
* `.contents` - Gives a tag's children as a list. The BeautifulSoup object itself has one child `<html>` tag.
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

# Searching the tree
