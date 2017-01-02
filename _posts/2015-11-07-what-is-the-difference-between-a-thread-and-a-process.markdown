---
layout: post
title: What is the difference between a thread and a process?
date: 2015-11-07 16:37:52.000000000 -05:00
categories:
- Reading Notes
author: Jason
---
<p>A process is an executing instance of an application. What does that mean? Well, for example, when you double-click the Microsoft Word icon, you start a process that runs Word. A thread is a path of execution within a process. Also, a process can contain multiple threads. When you start Word, the operating system creates a process and begins executing the primary thread of that process.</p>
<p>It’s important to note that a thread can do anything a process can do. But since a process can consist of multiple threads, a thread could be considered a ‘lightweight’ process. Thus, the essential difference between a thread and a process is the work that each one is used to accomplish. Threads are used for small tasks, whereas processes are used for more ‘heavyweight’ tasks – basically the execution of applications.</p>
<p>Another difference between a thread and a process is that threads within the same process share the same address space, whereas different processes do not. This allows threads to read from and write to the same data structures and variables, and also facilitates communication between threads. Communication between processes – also known as IPC, or inter-process communication – is quite difficult and resource-intensive.</p>
<p>MultiThreading</p>
<p>Threads, of course, allow for multi-threading. A common example of the advantage of multithreading is the fact that you can have a word processor that prints a document using a background thread, but at the same time another thread is running that accepts user input, so that you can type up a new document.</p>
<p>If we were dealing with an application that uses only one thread, then the application would only be able to do one thing at a time – so printing and responding to user input at the same time would not be possible in a single threaded application.</p>
<p>Each process has it’s own address space, but the threads within the same process share that address space. Threads also share any other resources within that process. This means that it’s very easy to share data amongst threads, but it’s also easy for the threads to step on each other, which can lead to bad things.</p>
<p>Multithreaded programs must be carefully programmed to prevent those bad things from happening. Sections of code that modify data structures shared by multiple threads are called critical sections. When a critical section is running in one thread it’s extremely important that no other thread be allowed into that critical section. This is called synchronization, which we wont get into any further over here. But, the point is that multithreading requires careful programming.</p>
<p>Also, context switching between threads is generally less expensive than in processes. And finally, the overhead (the cost of communication) between threads is very low relative to processes.</p>
<p>Here’s a summary of the differences between threads and processes:</p>
<ol>
<li>
<p>Threads are easier to create than processes since they<br />
don't require a separate address space.</p>
</li>
<li>
<p>Multithreading requires careful programming since threads<br />
share data strucures that should only be modified by one thread<br />
at a time.  Unlike threads, processes don't share the same<br />
address space.</p>
</li>
<li>
<p>Threads are considered lightweight because they use far<br />
less resources than processes.</p>
</li>
<li>
<p>Processes are independent of each other.  Threads, since they<br />
share the same address space are interdependent, so caution<br />
must be taken so that different threads don't step on each other.<br />
This is really another way of stating #2 above.</p>
</li>
<li>
<p>A process can consist of multiple threads.</p>
</li>
</ol>
