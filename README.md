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
Here is testing result based on our PC (RAM: 16gb, CPU Core: 8 (Intel Core i7 8th Gen))

1. Exclusive-only Simple Locking
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

## Analysis

-------