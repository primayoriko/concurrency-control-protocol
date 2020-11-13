# Concurrency Control Protocol

-------

First of all, this task or project is mainly based on [this repo](https://github.com/dhatch/database-concurrency-control).

For the instruction of the task and algorithm could be seen from `instruction.txt`

This code is mainly for testing performance (benchmarking) each concurrency control algorithm in C++.

## Algorithm Tested

-------

1. Exclusive-only Simple Locking
2. Serial Optimistic Concurrency Control (OCC)
3. Multiversion Timestamp Ordering Concurrency Control (MVCC)

## Requirement

-------
To run this program you should have

1. C++ compiler
2. GNU Make
3. Linux-based OS (haven't tested in Windows or macOS)

## How to Run

-------
Just execute

    make test

in the terminal with root project directory as the terminal path. 

## Testing Result

-------
We perform benchmarking on some devices, and here is testing result based on our first device (HP Pavilion Laptop -> RAM: 16gb; CPU: 8 cores (Intel Core i7 8th Gen))

1. Exclusive-only Simple Locking
    
   First test

   ![lock-1](docs/ExclusiveLock.png)

   Second test

   ![lock-2](docs/ExclusiveLock.png)

2. Serial Optimistic Concurrency Control (OCC)
   
    First test 

    ![occ-1](docs/OCC.png)

    Second test

    ![occ-2](docs/OCC-2.png)
    
3. Multiversion Timestamp Ordering Concurrency Control (MVCC)
   
   First test

   ![mvcc-1](docs/MVCC.png)

   Second test

   ![mvcc-2](docs/MVCC-2.png)

4. Comparison
   
    First test

    ![mixed-1](docs/mixed.png)

Then here is testing result based on our second device (RAM: 8gb, CPU Core: 6, Thread : 12 (Intel Core i7-9750 9th Gen))
1. Exclusive-only Simple Locking
    First test

    ![Lock-3](docs/ExclusiveLock-3.jpg)

    Second test

    ![Lock-4](docs/ExclusiveLock-4.png)
2. Serial Optimistic Concurrency Control (OCC)
   
    First test

    ![occ-3](docs/OCC-3.png)

    Second test

    ![occ-4](docs/OCC-4.png)
    
3. Multiversion Timestamp Ordering Concurrency Control (MVCC)
   
   First test

   ![mvcc-3](docs/MVCC-3.png)

   Second test

   ![mvcc-4](docs/MVCC-4.png)

## Analysis

-------