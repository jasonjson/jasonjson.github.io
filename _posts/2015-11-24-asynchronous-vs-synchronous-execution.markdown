---
layout: post
title: Asynchronous vs synchronous execution
date: 2015-11-24 10:56:59.000000000 -05:00
type: post
published: true
status: publish
categories:
- Reading Notes
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1461579146;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1437;}i:1;a:1:{s:2:"id";i:1312;}i:2;a:1:{s:2:"id";i:1400;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>Explanation 1:</p>
<p>When you execute something synchronously, you wait for it to finish before moving on to another task. When you execute something asynchronously, you can move on to another task before it finishes.</p>
<p>That being, said, in the context of computers this translates into executing a process or task on another "thread." A thread is a series of commands--a block of code--that exists as a unit of work. The operating system can manage multiple threads and assign a thread a piece ("slice") of processor time before switching to another thread to give it a turn to do some work. At its core (pardon the pun), a processor can simply execute a command--it has no concept of doing two things at one time. The operating system simulates this by allocating slices of time to different threads.</p>
<p>Now, if you introduce multiple cores/processors into the mix, then things CAN actually happen at the same time. The operating system can allocate time to one thread on the first processor, then allocate the same block of time to another thread on a different processor.</p>
<p>All of this is about allowing the operating system to manage the completion of your task while you can go on in your code and do other things. Asynchronous programming is a complicated topic because of the semantics of how things tie together when you can do them at the same time. There are numerous articles and books on the subject; have a look!</p>
<p>Explanation 2:</p>
<p>As an aside, I should mention that technically, the concept of synchronous vs. asynchronous really does not have anything to do with threads. Although, in general, it would be unusual to find asynchronous tasks running on the same thread, it is possible, (see below for e.g.) and it is common to find two or more tasks executing synchronously on separate threads... This concept has to do solely with whether or not a second or subsequent task can be initiated until the other task has completed, and that is all. What thread (or threads), or processes, or CPUs, or indeed, what hardware the task[s] are executed on is not relevant.</p>
<p>ASYNCHRONOUS EXAMPLE. In solving many engineering problems, the software is designed to split up the overall problem into multiple individual tasks, and then execute them asynchronously. Inverting a matrix, or a finite element analysis problem, are good examples. In computing, sorting a list is an example. The quick sort routine, for example, splits the list into two lists, and sorts each of them by calling itself recursively. In both of the above examples, the two tasks can (and often were) executed asynchronously. They do not need to be on separate threads. Even a machine with one CPU, and only one thread of execution can be coded to initiate processing of a second task before a first one has completed. The only criterion is that the results of one task are not necessary as inputs to the other task. As long as the start and end times of the tasks overlap, (possible only if the output of neither is needed as inputs to the other), they are being executed asynchronously, no matter how many threads are in use.</p>
<p>SYNCHRONOUS EXAMPLE. Any process consisting of multiple tasks where the tasks must be executed in sequence, but one must be executed on another machine (Fetch and/or update data, get a stock quote from a financial service, etc.). If it's on a separate machine it is on a separate thread, whether synchronous or asynchronous.</p>
