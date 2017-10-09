---
layout: post
title: 166 - Fraction to Recurring Decimal
date: 2015-11-05 12:57:44.000000000 -05:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
**Given two integers representing the numerator and denominator of a fraction, return the fraction in string format. If the fractional part is repeating, enclose the repeating part in parentheses.**


``` java
public class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (denominator == 0) return "";
        StringBuilder sb = new StringBuilder();
        HashMap<Long, Integer> map = new HashMap<Long, Integer>();
        if (numerator < 0 && denominator > 0 || (numerator > 0 && denominator < 0))  sb.append("-");
        long nume = Math.abs((long) numerator);//必须用long, 两个数可能是Integer.MIN_VALUE
        long deno = Math.abs((long) denominator);
        long digit = nume / deno;
        sb.append("" + digit);
        nume %= deno;
        if (nume == 0) {
            return sb.toString();
        } else {
            sb.append(".");
        }
        int index = 1;//把“.”的位置想象成0，后面的数字起始index为1
        while (nume != 0) {
            nume *= 10;//2 / 5, num = 2, 左移成20再除5等于4
            digit = nume / deno;
            if (!map.containsKey(nume)) {
                sb.append("" + digit);
                map.put(nume, index ++);
            } else {
                int firstIndex = map.get(nume) + sb.indexOf(".");
                sb.insert(firstIndex, "(");
                sb.append(")");
                break;
            }
            nume %= deno;//这个必须放在最后，不然我们就提前更新了nume的值，无法用于map搜索
        }
        return sb.toString();
    }
}
```

``` python
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if not denominator:
            return ""
        if not numerator:
            return "0"

        ret = []
        nume, deno = abs(numerator), abs(denominator)

        #integral part
        if (numerator > 0) == (denominator < 0):
            ret.append("-")
        ret.append(str(nume / deno))
        nume %= deno
        if nume == 0:
            return "".join(ret)
        #fractional part
        ret.append(".")
        repeating_map = {nume : len(ret)}
        while nume:
            nume *= 10
            ret.append(str(nume / deno))
            nume %= deno
            if nume not in repeating_map:
                repeating_map[nume] = len(ret)
            else:
                ret.insert(repeating_map[nume], "(")
                ret.append(")")
                break
        return "".join(ret)
```
