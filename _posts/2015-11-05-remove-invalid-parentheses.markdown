---
layout: post
title: 301 - Remove Invalid Parentheses
date: 2015-11-05 11:13:54.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results. Note: The input string may contain letters other than the parentheses ( and ).**


``` java
public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> result = new ArrayList<String>();
        if (s == null) return result;//s.length() == 0 is also a valid result

        Set<String> visited = new HashSet<String>();
        Queue<String> q = new LinkedList<String>();
        q.offer(s);
        visited.add(s);
        boolean found = false;
        while (!q.isEmpty()) {
            String curr = q.poll();
            if (isValid(curr)) {
                result.add(curr);
                found = true;
            }
            if (!found) {
                for (int i = 0; i < curr.length(); i++) {
                    if (curr.charAt(i) == '(' || curr.charAt(i) == ')') {
                        String newS = curr.substring(0, i) + curr.substring(i + 1);
                        if (!visited.contains(newS)) {
                            q.offer(newS);
                            visited.add(newS);
                        }
                    }
                }
            }
        }
        return result;
    }

    public boolean isValid(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                count ++;
            }
            if (c == ')' && count -- == 0) {
                return false;
            }
        }
        return count == 0;
    }
}
```

``` python
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        visited = set([s])
        #cannot write set(s), if s = "ab", set(s) = set("a", "b")
        stack = collections.deque([s])
        #have to use queue, we need to stop once is valid one is found
        ret = []
        found = False
        while stack:
            curr = stack.popleft()
            if self.is_valid(curr):
                ret.append(curr)
                found = True
            if not found:
                for i, char in enumerate(curr):
                    if char == "(" or char == ")":
                        new_s = curr[:i] + curr[i+1:]
                        if new_s not in visited:
                            stack.append(new_s)
                            visited.add(new_s)
        return ret or [""]

    def is_valid(self, s):
        count = 0
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
                if count < 0:
                    return False
        return count == 0
```
