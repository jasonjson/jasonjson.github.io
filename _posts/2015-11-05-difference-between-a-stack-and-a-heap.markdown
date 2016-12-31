---
layout: post
title: Difference between a stack and a heap
date: 2015-11-05 23:26:17.000000000 -05:00
type: post
published: true
status: publish
categories:
- Reading Notes
tags: []
meta:
  _wpcom_is_markdown: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465133812;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1437;}i:1;a:1:{s:2:"id";i:1312;}i:2;a:1:{s:2:"id";i:1629;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<ul>
<li>Where are the stack and heap stored?
<ul>
<li>They are both stored in the computer’s RAM (Random Access Memory). For a refresher on RAM and virtual memory, read this article: How Virtual Memory Works</li>
</ul>
</li>
<li>How do threads interact with the stack and the heap? How do the stack and heap work in multithreading?
<ul>
<li>In a multi-threaded application, each thread will have its own stack. But, all the different threads will share the heap. Because the different threads share the heap in a multi-threaded application, this also means that there has to be some coordination between the threads so that they don’t try to access and manipulate the same piece(s) of memory in the heap at the same time.</li>
</ul>
</li>
<li>Can an object be stored on the stack instead of the heap?
<ul>
<li>Yes, an object can be stored on the stack. If you create an object inside a function without using the “new” operator then this will create and store the object on the stack, and not on the heap. Suppose we have a C++ class called Member, for which we want to create an object. We also have a function called some function(). Here is what the code would look like:</li>
</ul>
</li>
<li>Code to create an object on the stack:</li>
</ul>
<pre>
void somefunction( )
{
/* create an object "m" of class Member
    this will be put on the stack since the 
    "new" keyword is not used, and we are 
   creating the object inside a function
*/

  Member m;

} //the object "m" is destroyed once the function ends
</pre>
<p>So, the object “m” is destroyed once the function has run to completion – or, in other words, when it “goes out of scope”. The memory being used for the object “m” on the stack will be removed once the function is done running.</p>
<ul>
<li>If we want to create an object on the heap inside a function, then this is what the code would look like:</li>
</ul>
<p>Code to create an object on the heap:</p>
<pre>
void some function( )
{
/* create an object "m" of class Member
    this will be put on the heap since the 
    "new" keyword is used, and we are 
   creating the object inside a function
*/

  Member* m = new Member( ) ;

  /* the object "m" must be deleted
      otherwise a memory leak occurs
  */

  delete m; 
} 
</pre>
<p>In the code above, you can see that the “m” object is created inside a function using the “new” keyword. This means that “m” will be created on the heap. But, since “m” is created using the “new” keyword, that also means that we must delete the “m” object on our own as well – otherwise we will end up with a memory leak.</p>
<ul>
<li>How long does memory on the stack last versus memory on the heap?
<ul>
<li>Once a function call runs to completion, any data on the stack created specifically for that function call will automatically be deleted. Any data on the heap will remain there until it’s manually deleted by the programmer.</li>
</ul>
</li>
<li>Can the stack grow in size? Can the heap grow in size?
<ul>
<li>The stack is set to a fixed size, and can not grow past it’s fixed size (although some languages have extensions that do allow this). So, if there is not enough room on the stack to handle the memory being assigned to it, a stack overflow occurs. This often happens when a lot of nested functions are being called, or if there is an infinite recursive call.
</li>
<li>
<p>If the current size of the heap is too small to accommodate new memory, then more memory can be added to the heap by the operating system. This is one of the big differences between the heap and the stack.</p>
</li>
</ul>
</li>
<li>
<p>How are the stack and heap implemented?</p>
<ul>
<li>The implementation really depends on the language, compiler, and run-time – the small details of the implementation for a stack and a heap will always be different depending on what language and compiler are being used. But, in the big picture, the stacks and heaps in one language are used to accomplish the same things as stacks and heaps in another language.</li>
</ul>
</li>
<li>Which is faster – the stack or the heap? And why?
<ul>
<li>The stack is much faster than the heap. This is because of the way that memory is allocated on the stack. Allocating memory on the stack is as simple as moving the stack pointer up.</li>
</ul>
</li>
<li>How is memory deallocated on the stack and heap?
<ul>
<li>Data on the stack is automatically deallocated when variables go out of scope. However, in languages like C and C++, data stored on the heap has to be deleted manually by the programmer using one of the built in keywords like free, delete, or delete[ ]. Other languages like Java and .NET use garbage collection to automatically delete memory from the heap, without the programmer having to do anything..</li>
</ul>
</li>
<li>What can go wrong with the stack and the heap?
<ul>
<li>If the stack runs out of memory, then this is called a stack overflow – and could cause the program to crash. The heap could have the problem of fragmentation, which occurs when the available memory on the heap is being stored as noncontiguous (or disconnected) blocks – because used blocks of memory are in between the unused memory blocks. When excessive fragmentation occurs, allocating new memory may be impossible because of the fact that even though there is enough memory for the desired allocation, there may not be enough memory in one big block for the desired amount of memory.</li>
</ul>
</li>
</ul>
