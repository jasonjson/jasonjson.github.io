---
layout: post
title: Summary for leetcode, zz from peking2
date: 2015-10-25 10:20:07.000000000 -04:00
tags: algorithm
categories:
- Reading Notes
author: Jason
---
<p>首先声明一下，这里的面试题主要所指数据结构和算法的题目，题目的分析集中在Leetcode上面的题目上。</p>
<p>我认为一道面试题由以下几个方面组成的</p>
<p>Question</p>
<p>Data structure in question</p>
<p>Data structure in solution</p>
<p>Algorithm in solution</p>
<p>Coding</p>
<p>题目：非常关键，一个题目通常有一些相应的变形题目，同一个题目可能有不同的要求。比如时间复杂度，空间复杂度的要求，比如recursive,</p>
iterative的要求。而根据题目的变形与要求，可能会极大的影响到你能够采取的数据结构和算法。</p>
<p>问题中的数据机构：问题中有可能带数据结构，有可能没有数据结构，有可能是可以自定义数据结构</p>
<p>解决方案中的数据结构：可以是in-place的，也就是利用已有的数据结构，也可能是创建新的数据结构。新的数据结构跟已有的数据结构没有必然的联系，而很多问题都是一题多解，可能采取不同的数据结构。</p>
<p>算法：一般来说，当解决方案中的数据结构确定以后，算法也就确定了。同样，一旦解决方案的算法确定，相应的数据结构也就确定了。这两个没有先后的关系，但解决方案中的数据结构和算法具有非常紧密的联系。</p>
<p>代码：非常关键。代码就是解决方案的数据结构和算法的实现了。目前来看，题目，数据结构和算法在面试中出现的类型比较固定，因此代码的好坏则是拉开面试者水平的一个有效手段。这也是为什么F，G如此看中代码的质量了。我发现上面几点比较容易突击，但是写代码的功力还是需要实打实的积累的。</p>
<p>总结面试题目的关键就是要把面试题目进行分类之后分析。由于面试题目由以上几个部分组成并且混杂在一起，因此怎样合理的分类就变得非常的困难。其实Careercup150的分类就比较好，它是这样进行分类的。</p>
<p>数据结构：Arrays and Strings, Linked Lists, Stacks and Queues, Trees and</p>
Graphs</p>
<p>算法：Bit Manipulation, Mathematics and Probability, Recursion and</p>
Dynamic Programming, Sorting and Searching</p>
<p>但是我感觉这样分类比较适合初级阶段学习，并不适合系统地对面试题目进行分析。我其实目前也没有什么特别好的idea，想跟着感觉先来，可能慢慢就能悟出更多了。</p>
<ol>
<li>首先算法要简洁，算法不简洁代码好不了，这是根本。</li>
<li>对惯用的代码要形成习惯和模式，基本上大家都这么写</p>
比如一个array倒置[1,2,3]变为[3,2,1]，基本上都会用while, 而我以前由于没有练习过，当场用的for，就很难看。</li>
<li>每一句代码都是必要的。有些代码虽说放在那里无关大局，但是完全可以删掉，就显得冗余难看</li>
<li>代码要模块化，如果一段代码会重复使用要写子函数。或者一部分功能自成一体，最好也写子函数
<p>简称two pointers吧。大概把分类粗略的搞了一遍（http://leetcode.cloudfoundry.com/),</p>
发现利用two pointers解决的题目数量很大。two pointers我指的是一类题，而不一定是真正的two pointers,</p>
比如可能是three pointers, 也可能不是pointer， 而是index。这类题基本上就是发生在array,</p>
string, linked</p>
list这三种数据结构上，是一种基本的算法和编程技巧，同样超高频率的出现，可以说是面试必遇的题。</li>
</ol>
<p>two pointers常常和其他的算法混杂起来出现。比如binary search本身也可以归类为two</p>
pointers的。如果这样算的话，Leetcode上边1/4的题目都跟它相关。因此，two</p>
pointers是必须熟练掌握的基本编程技巧。</p>
<p>Two pointers大概分三种类型</p>
<ol>
<li>两个pointers从头往后走：感觉绝大多数的linked</p>
list的题目都涉及到这个操作，当然还有array。这类题目很多时候又可以称为sliding</p>
window。</li>
</ol>
<p>Implement strStr()</p>
<p>Longest Substring Without Repeating Characters</p>
<p>Minimum Window Substring</p>
<p>Remove Duplicates from Sorted Array &amp;</p>
II</p>
<p>Remove Duplicates from Sorted List &amp; II</p>
<p>Remove Element</p>
<p>Remove Nth Node From End of List</p>
<p>Reverse Linked Llist II</p>
<p>Rotate List</p>
<p>Substring with Concatenation of All Words</p>
<p>Swap Nodes in Pairs</p>
2.</p>
两个pointers从两头往中间走：一般面试出现的的都是singly linked list,</p>
因此这类题主要是array题。</p>
<p>3Sum</p>
<p>3Sum Closest</p>
<p>4Sum</p>
<p>Container With Most Water</p>
<p>Sort Colors</p>
<p>Trapping Rain Water</p>
<p>Two Sum</p>
<p>Binary search (will discuss it in a separate section)</p>
3.</p>
两个pointers控制两个不同的数组或链表：一般出现在跟merge相关的题目上。</p>
<p>Add Binary</p>
<p>Add Two Numbers</p>
<p>Merge Sorted Array</p>
<p>Merge Two Sorted Lists</p>
<p>Multiply Strings</p>
<p>Partition List</p>
<p>基本题，但是非常重要。面试中碰到任何一题一点也不奇怪。PIE,</p>
CC150和Leetcode都不约而同地包含了这类题。把这些题目做熟是必须的。基本上来说这类题的解法都是DFS，程序的大体框架非常类似，只是根据题目的要求代码稍作修改。当然每道题也有不同的解法，但是你应该根据自己的喜好把这类题目的解决方案统一化。熟悉了这类题目以后对于DFS(will</p>
be discussed in a separate section)</p>
的理解会非常深刻。基本上一般的DFS的题目应该没什么问题了。</p>
<p>无论是排列还是组合，这类题都有一个变形，就是要求不能有重复的输出。PIE和CC150都没有提到相应的解法，大家应该很好的体会一下。如果没有相应的准备，属于面试的时候比较容易跪的题目。</p>
<p>Permutation</p>
<p>输入没有重复：Permutations, CC150 9.5, PIE Chapter7 Permutations of a</p>
String输入有重复，输出不能有重复：Permutations</p>
II</p>
<p>Next Permutation: 经典算法，背吧</p>
<p>Permutation Sequence: 非常有意思的题目</p>
<p>Combination</p>
<p>纯粹的subset</p>
<p>输入没有重复：Subsets, CC150 9.4, PIE Chapter7 Combinations of a</p>
String输入有重复，输出不能有重复：Subsets</p>
II</p>
<p>需要满足一定要求的组合</p>
<p>一个元素只能取一次(输入没有重复): Combinations</p>
<p>一个元素可以取多次(输入没有重复): Combination Sum, CC150</p>
9.8一个元素只能取一次(输入有重复，输出不能有重复）:</p>
Combination Sum II</p>
<p>Gray Code: 具有subset的序列特点 （考虑CC150 9.4 Solution#2:</p>
Combinatorics)</p>
<p>数据结构</p>
<p>Array, ArrayList</p>
<p>String, StringBuffer</p>
<p>LinkedList</p>
<p>HashMap, HashSet</p>
<p>Stack and Queue</p>
<p>Tree:</p>
<p>BT: binary tree</p>
<p>BST: binary search tree,</p>
<p>Balanced BST (red-black tree): TreeMap, TreeSet</p>
<p>Trie: prefix tree</p>
<p>Heap: PriorityQueue</p>
Grpah</p>
<p>注意：</p>
<p>Array和Linkedlist是最最基本的数据结构，因为他们可以构造很多其他的数据结构，比如String</p>
(C语言里String就是字符数组），HashMap, Stack和Queue</p>
(Java里Queue就是LinkedList实现了Queue的interface;</p>
Ruby里stack和queue都是array）, 以及Heap。</p>
<p>Heap is a tree logically, but array physically.</p>
<p>HashMap, Stack and</p>
Queue通常不会出现在问题里的数据结构中，因此一般作为solution的数据结构。但是面试中也常会让你实现这三种数据结构，另外就是CC150的3.2和3.5都是典型的Stack和Queue的题。Leetcode中并不涵盖这些内容，这几种数据结构在Leetcode中都是作为solution数据结构出现的</p>
(没有的原因是这些题目不太适合OJ，因此需要单独练习）。</p>
<p>目前Leetcode还不包含graph的题型</p>
<p>算法</p>
<p>Sort: quick sort, merge sort, count sort, heap sort, bucket sort,</p>
radix sort, external sort, K selection etc.</p>
<p>Merge: 2 array/list merge, k-way merge, interval merge</p>
etc.</p>
<p>Binary search:</p>
<p>Stack:</p>
<p>Recursion and Iteration:</p>
<p>DFS：pre-order, in-order, post-order for trees</p>
<p>BFS: 需要用Queue</p>
<p>DP: Top down and bottom up</p>
<p>Greedy:</p>
<p>Toposort: 需要用Queue</p>
<p>注意：</p>
<p>Leetcode并没有包含各种sort算法，而通常面试很少让你直接去实现sort算法，但是大部分的相关编程技巧是包含在很多题目当中的,</p>
比如quick sort的two pointers。</p>
<p>Merge跟sort是紧密相关的，单独拿出来是因为有很多这个类型的题目，需要一起总结。Merge操作的对象基本都是已经排好序的。</p>
<p>Stack虽说是数据结构，但是一般出现在solution里，因此代表了一类算法</p>
<p>Toposort面试作为难题也很有可能遇到，目前Leetcode还没有包括进去</p>
<p>玩竞赛对面试不利的一个地方就是面试经常遇到的数据结构比如LinkedList, Tree, 和算法Binary</p>
search，竞赛很少涉及到，因此一直心里都感觉到有些不安。</p>
<p>Binary search非常tricky，虽说道理简单，但是面试的时候却很容易出bug，因此总结一下是必须的。假设i=0,</p>
j=A.length-1, 我做了一下LeetCode上的所有binary</p>
search的题目，发现了以下几点值得注意。</p>
<p>终止条件不同 i&lt;=j, i&lt;j</p>
<p>mid的上下取向不同 i+(j-i)/2, j-(j-i)/2</p>
<p>如何合理分半</p>
<p>分半的时候取=mid, mid-1, or mid+1</p>
<p>Search a 2D Matrix： 这是一道普通的binary search。终止条件i&lt;=j,</p>
mid取向i+(j-i)/2, 分半的时候=mid-1 or mid+1。</p>
<p>Search for a Range：这道题需要终止条件i&lt;j,</p>
mid取向两种都需要用到，分半的时候需要用到=mid。我发现一般＝mid的时候，终止条件往往是i&lt;j,</p>
不然会有死循环。</p>
<p>如何合理分半：下边这几道题都很tricky，分半的时候都有各自的特点，很不容易一次写对。需要多多练习和体会。</p>
<p>Search in Rotated Sorted Array</p>
<p>Search in Rotated Sorted Array II</p>
<p>Median of Two Sorted Arrays</p>
<p>还有一个有趣的现象就是很多数学相关的题目也是通过binary search来解决的：</p>
<p>Divide Two Integers：这题没做过面试也容易跪</p>
<p>Pow(x, n)</p>
<p>Sqrt(x)：其实算是一道典型的binary</p>
search题目，不过里边包括了几个tricky的地方，很难一次写对</p>
<p>总的来说，LeetCode上边的这些binary</p>
search的题目cover的还比较全面，而且题目全部是面试高频题，需要练习一次写对</p>
<p>首先LeetCode上几乎所有的Linked list的题目都可以用two pointers来解决，或者会用到two</p>
pointers这个基本编程技巧。因此two pointers跟linked list是紧密相关的。因为two</p>
pointers以前已经总结过了，就不多讲了。</p>
<p>其次，因为LinkedList和Array/ArrayList一样都具备有List的特性，因此很多题目都出现在了两种数据结构上，或者说很多题目都是可以把这两种数据结构互换的。比如：</p>
<p>Add Two Numbers</p>
<p>Convert Sorted List to Binary Search</p>
Tree</p>
<p>Insert Interval</p>
<p>Merge Intervals</p>
<p>Merge k Sorted</p>
Lists</p>
<p>Merge Two Sorted</p>
Lists</p>
<p>Remove Duplicates from Sorted</p>
List</p>
<p>Remove Duplicates from Sorted List</p>
 II</p>
<p>第三，LinkedList的题目大多自然而然使用iteration来解决的，但是我发现有些时候iteration比较容易出bug，换成recursion实现更容易。面试的时候万一iteration卡住可以换换recursion的思路。</p>
<p>第四，dummy head非常有用，可以使代码简洁很多，并且容易写bug</p>
free的code。这个技巧可以大量使用。</p>
<p>第五，今天做了一遍LinkedList的题目，发现两个地方容易出bug。一是two pointers</p>
loop完之后常常会有一个收尾的工作，比如Add Two</p>
Numbers需要处理carrier>0的情况。二是在swap了nodes之后，新的tail需要把next置空，不然就出现死循环了。</p>
<p>一直没有总结Tree，这次想总结一下结果却发现没有什么太多可以总结的。Leetcode上tree的题目还是比较全面的。我做了一遍发现基本上跑不出三个套路：</p>
<ol>
<li>Recursive DFS
</li>
<li>
<p>Iterative DFS</p>
</li>
<li>
<p>BFS</p>
</li>
</ol>
<p>有些tree的题目比较tricky一些，但是最终解法还是逃不出这三个套路，所以我觉得面试的时候代码的质量就变得更加的重要了。因为没有什么太多总结的，下边就随便聊一下了。</p>
<p>Leetcode上graph的题目涉及的很少，不过从算法和coding来说DFS，BFS完全适用于tree和graph。因此，把tree的题目练好了，graph的多数题目应该也不会有什么问题才对。当然graph涉及的算法比tree还是要多的，比如shortest</p>
path,</p>
toposort等等，但是DFS,BFS还是基本中的基本。因此做Leetcode上的tree的题目也相当于练习了graph的题目了。</p>
<p>由于Tree的题目比较多，我感觉一些可以skip掉，如果时间不充裕的话。或者做一遍即可，不需要反复练习。这些题目或者太简单，或者面试不太可能碰到。</p>
<p>Balanced Binary Tree</p>
<p>Binary Tree Level Order Traversal II</p>
<p>Maximum Depth of Binary Tree</p>
<p>Minimum Depth of Binary Tree</p>
<p>Same Tree</p>
<p>Symmetric Tree</p>
<p>Unique Binary Search Trees</p>
<p>Unique Binary Search Trees II</p>
<p>Pre-order, In-order, Post-order traversal</p>
需要会recursive和iterative的两种实现方式。可惜Leetcode上只包含了In-order，有些遗憾。</p>
<p>Tree的serialization/deserialization也是常常被考到的题目，这个Leetcode目前还没有包含，当然套路还是DFS/BFS。</p>
<p>LinkedList和Binary Tree相互转换的题目。</p>
<p>Convert Sorted List to Binary Search Tree</p>
<p>Flatten Binary Tree to Linked List</p>
(这题原题在CC150是一道双向链表题，不知道Leetcode上怎么改单向了。双向链表应该更复杂一些，大家要注意一下）</p>
