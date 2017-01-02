---
layout: post
title: Fraction to Recurring Decimal
date: 2015-11-05 12:57:44.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Given two integers representing the numerator and denominator of a fraction, return the fraction in string format. If the fractional part is repeating, enclose the repeating part in parentheses.</em></strong></p>

<hr />
``` java
//for the decimal parts to recur, the remainders should recur. So we need to maintain the remainders we have seen. Once we see a repeated remainder, we know that we have reached the end of the recurring parts and should enclose it with a ). However, we still need to insert the ( to the correct position. So we maintain a mapping from each remainder to the position of the corresponding quotient digit of it in the recurring parts. Then we use this mapping to retrieve the starting position of the recurring parts.
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
