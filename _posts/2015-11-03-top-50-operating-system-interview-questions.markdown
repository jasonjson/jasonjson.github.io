---
layout: post
title: Top 50 Operating System Interview Questions
date: 2015-11-03 22:49:09.000000000 -05:00
tags:
- Algorithm
categories:
- Reading Notes
- OS
author: Jason
---
<p><a href="http://career.guru99.com/">ZZ from</a></p>
<ul>
<li>Explain the main purpose of an operating system?
<ul>
<li>Operating systems exist for two main purposes. One is that it is designed to make sure a computer system performs well by managing its computational activities. Another is that it provides an environment for the development and execution of programs.</li>
</ul>
</li>
<li>What is demand paging?
<ul>
<li>Demand paging is a system wherein area of memory that are not currently being used are swapped to disk to make room for an application’s need.</li>
</ul>
</li>
<li>What are the advantages of a multiprocessor system?
<ul>
<li>With an increased number of processors, there is considerable increase in throughput. It can also save more money because they can share resources. Finally, overall reliability is increased as well.</li>
</ul>
</li>
<li>What is kernel?
<ul>
<li>Kernel is the core of every operating system. It connects applications to the actual processing of data. It also manages all communications between software and hardware components to ensure usability and reliability.</li>
</ul>
</li>
<li>What are real-time systems?
<ul>
<li>Real-time systems are used when rigid time requirements have been placed on the operation of a processor. It has well defined and fixed time constraints.</li>
</ul>
</li>
<li>What is virtual memory?
<ul>
<li>Virtual memory is a memory management technique for letting processes execute outside of memory. This is very useful especially is an executing program cannot fit in the physical memory.</li>
</ul>
</li>
<li>Describe the objective of multiprogramming.
<ul>
<li>The main objective of multiprogramming is to have process running at all times. With this design, CPU utilization is said to be maximized.</li>
</ul>
</li>
<li>What are time sharing systems?
<ul>
<li>In a Time sharing system, the CPU executes multiple jobs by switching among them, also known as multitasking. This process happens so fast that users can actually interact with each program while it is running.</li>
</ul>
</li>
<li>What is SMP?
<ul>
<li>SMP is short for Symmetric MultiProcessing, and is the most common type of multiple- processor systems. In this system, each processor runs an identical copy of the operating system, and these copies communicate with one another as needed.</li>
</ul>
</li>
<li>How are server systems classified?
<ul>
<li>Server systems can be classified as either computer-server systems or file server systems. In the first case, an interface is made available for clients to send requests to perform an action. In the second case, provisions are available for clients to create, access and update files.</li>
</ul>
</li>
<li>What is asymmetric clustering?
<ul>
<li>In asymmetric clustering, a machine is in a state known as hot standby mode where it does nothing but to monitor the active server. That machine takes the active server’s role should the server fails.</li>
</ul>
</li>
<li>What is a thread?
<ul>
<li>A thread is a basic unit of CPU utilization. In general, a thread is composed of a thread ID, program counter, register set and the stack.</li>
</ul>
</li>
<li>Give some benefits of multithreaded programming.
<ul>
<li>there is an increased responsiveness to the user</li>
<li>resource sharing within the process</li>
<li>economy</li>
<li>utilization of multiprocessing architecture</li>
</ul>
</li>
<li>Briefly explain FCFS.
<ul>
<li>FCFS is short for First-come, first-served, and is one type of scheduling algorithm. In this scheme, the process that requests the CPU first is allocated the CPU first. Implementation is managed by a FIFO queue.</li>
</ul>
</li>
<li>What is RR scheduling algorithm?
<ul>
<li>RR (round-robin) scheduling algorithm is primarily aimed for time-sharing systems. A circular queue is setup in such a way that the CPU scheduler goes around that queue, allocating CPU to each process for a time interval of up to around 10 to 100 milliseconds.</li>
</ul>
</li>
<li>What necessary conditions can lead to a deadlock situation in a system?
<ul>
<li>Deadlock situations occur when four conditions occur simultaneously in a system: Mutual exclusion; Hold and Wait; No preemption; and Circular wait.</li>
</ul>
</li>
<li>Enumerate the different RAID levels.
<ul>
<li>RAID 0 – Non-redundant striping</li>
<li>RAID 1 – Mirrored Disks</li>
<li>RAID 2 – Memory-style error-correcting codes </li>
<li>RAID 3 - Bit-interleaved Parity</li>
<li>RAID 4 – Block-interleaved Parity</li>
<li>RAID 5 – Block-interleaved distributed Parity </li>
<li>RAID 6 – P+Q Redundancy</li>
</ul>
</li>
<li>Describe Banker’s algorithm
<ul>
<li>Banker’s algorithm is one form of deadlock-avoidance in a system. It gets its name from a banking system wherein the bank never allocates available cash in such a way that it can no longer satisfy the needs of all of its customers.</li>
</ul>
</li>
<li>What factors determine whether a detection-algorithm must be utilized in a deadlock avoidance system?
<ul>
<li>One is that it depends on how often a deadlock is likely to occur under the implementation of this algorithm. The other has to do with how many processes will be affected by deadlock when this algorithm is applied.</li>
</ul>
</li>
<li>Differentiate logical from physical address space.
<ul>
<li>Logical address refers to the address that is generated by the CPU. On the other hand, physical address refers to the address that is seen by the memory unit.</li>
</ul>
</li>
<li>How does dynamic loading aid in better memory space utilization?
<ul>
<li>With dynamic loading, a routine is not loaded until it is called. This method is especially useful when large amounts of code are needed in order to handle infrequently occurring cases such as error routines.</li>
</ul>
</li>
<li>What are overlays?
<ul>
<li>Overlays are used to enable a process to be larger than the amount of memory allocated to it. The basic idea of this is that only instructions and data that are needed at any given time are kept in memory.</li>
</ul>
</li>
<li>What is the basic function of paging?
<ul>
<li>Paging is a memory management scheme that permits the physical-address space of a process to be noncontiguous. It avoids the considerable problem of having to fit varied sized memory chunks onto the backing store.</li>
</ul>
</li>
<li>What is fragmentation?
<ul>
<li>Fragmentation is memory wasted. It can be internal if we are dealing with systems that have fixed-sized allocation units, or external if we are dealing with systems that have variable-sized allocation units.</li>
</ul>
</li>
<li>How does swapping result in better memory management?
<ul>
<li>During regular intervals that are set by the operating system, processes can be copied from main memory to a backing store, and then copied back later. Swapping allows more processes to be run that can fit into memory at one time.</li>
</ul>
</li>
<li>Give an example of a Process State.
<ul>
<li>New State – means a process is being created</li>
<li>Running – means instructions are being executed</li>
<li>Waiting – means a process is waiting for certain conditions or events to occur </li>
<li>Ready – means a process is waiting for an instruction from the main processor - Terminate – means a process is done executing</li>
</ul>
</li>
<li>What is a socket?
<ul>
<li>A socket provides a connection between two applications. Each endpoint of a communication is a socket.</li>
</ul>
</li>
<li>What is Direct Access Method?
<ul>
<li>Direct Access method is based on a disk model of a file, such that it is viewed as a numbered sequence of blocks or records. It allows arbitrary blocks to be read or written. Direct access is advantageous when accessing large amounts of information.</li>
</ul>
</li>
<li>When does trashing occur?
<ul>
<li>Trashing refers to an instance of high paging activity. This happens when it is spending more time paging instead of executing.</li>
</ul>
</li>
<li>What is the best page size when designing an operating system?
<ul>
<li>The best paging size varies from system to system, so there is no single best when it comes to page size. There are different factors to consider in order to come up with a suitable page size, such as page table, paging time, and its effect on the overall efficiency of the operating system.</li>
</ul>
</li>
<li>When designing the file structure for an operating system, what attributes are considered?
<ul>
<li>Typically, the different attributes for a file structure are naming, identifier, supported file types, and location for the files, size, and level of protection.</li>
</ul>
</li>
<li>What is root partition?
<ul>
<li>Root partition is where the operating system kernel is located. It also contains other potentially important system files that are mounted during boot time.</li>
</ul>
</li>
<li>What are device drivers?
<ul>
<li>Device drivers provides a standard means of representing I/O devices that maybe manufactured by different companies. This prevents conflicts whenever such devices are incorporated in a systems unit.</li>
</ul>
</li>
<li>What are the primary functions of VFS?
<ul>
<li>VFS, or Virtual File System, separates file system generic operations from their implementation by defining a clean VFS interface. It is also based on a file-representation structure known as vnode, which contains a numerical designator needed to support network file systems.</li>
</ul>
</li>
<li>What are the different types of CPU registers in a typical operating system design?
<ul>
<li>Accumulators</li>
<li>Index Registers</li>
<li>Stack Pointer</li>
<li>General Purpose Registers</li>
</ul>
</li>
<li>What is the purpose of an I/O status information?
<ul>
<li>I/O status information provides info about which I/O devices are to be allocated for a particular process. It also shows which files are opened, and other I/O device state.</li>
</ul>
</li>
<li>What is multitasking?
<ul>
<li>Multitasking is the process within an operating system that allows the user to run several applications at the same time. However, only one application is active at a time for user interaction, although some applications can run “behind the scene”.</li>
</ul>
</li>
<li>What are some pros and cons of a command line interface?
<ul>
<li>A command line interface allows the user to type in commands that can immediately provide results. Many seasoned computer users are well accustomed to using the command line because they find it quicker and simpler. The main problem with a command line interface is that users have to be familiar with the commands, including the switches and parameters that come with it. This is a downside for people who are not fond of memorizing commands.</li>
</ul>
</li>
<li>What is caching?
<ul>
<li>Caching is the processing of utilizing a region of fast memory for a limited data and process. A cache memory is usually much efficient because of its high access speed.</li>
</ul>
</li>
<li>What is spooling?
<ul>
<li>Spooling is normally associated with printing. When different applications want to send an output to the printer at the same time, spooling takes all of these print jobs into a disk file and queues them accordingly to the printer.</li>
</ul>
</li>
<li>What is an Assembler?
<ul>
<li>An assembler acts as a translator for low level language. Assembly codes, written using mnemonic commands are translated by the Assembler into machine language.</li>
</ul>
</li>
<li>What are interrupts?
<ul>
<li>Interrupts are part of a hardware mechanism that sends a notification to the CPU when it wants to gain access to a particular resource. An interrupt handler receives this interrupt signal and “tells” the processor to take action based on the interrupt request.</li>
</ul>
</li>
<li>What is GUI?
<ul>
<li>GUI is short for Graphical User Interface. It provides users with an interface wherein actions can be performed by interacting with icons and graphical symbols. People find it easier to interact with the computer when in a GUI especially when using the mouse. Instead of having to remember and type commands, users just click on buttons to perform a process.</li>
</ul>
</li>
<li>What is preemptive multitasking?
<ul>
<li>Preemptive multitasking allows an operating system to switch between software programs. This in turn allows multiple programs to run without necessarily taking complete control over the processor and resulting in system crashes.</li>
</ul>
</li>
<li>Why is partitioning and formatting a prerequisite to installing an operating system?
<ul>
<li>Partitioning and formatting creates a preparatory environment on the drive so that the operating system can be copied and installed properly. This includes allocating space on the drive, designating a drive name, determining and creating the appropriate file system structure.</li>
</ul>
</li>
<li>What is plumbing / piping?
<ul>
<li>It is the process of using the output of one program as an input to another. For example, instead of sending the listing of a folder or drive to the main screen, it can be piped and sent to a file, or sent to the printer to produce a hard copy.</li>
</ul>
</li>
<li>What is NOS?
<ul>
<li>NOS is short for Network Operating System. It is a specialized software that will allow a computer to communicate with other devices over the network, including file/folder sharing.</li>
</ul>
</li>
<li>Differentiate internal commands from external commands.
<ul>
<li>Internal commands are built-in commands that are already part of the operating system. External commands are separate file programs that are stored in a separate folder or directory.</li>
</ul>
</li>
<li>Under DOS, what command will you type when you want to list down the files in a directory, and at the same time pause after every screen output?
<ul>
<li>a) dir /w</li>
<li>b) dir /p</li>
<li>c) dir /s</li>
<li>d) dir /w /p</li>
<li>Answer: d) dir /w /p</li>
</ul>
</li>
<li>How would a filenamed EXAMPLEFILE.TXT appear when viewed under the DOS command console operating in Windows 98?
<ul>
<li>The filename would appear as EXAMPL~1.TXT . The reason behind this is that filenames under this operating system is limited to 8 characters when working under DOS environment.</li>
</ul>
</li>
</ul>
