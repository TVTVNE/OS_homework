# Assignment 4: Multithreading and Synchronization

## Elias Berrada

## Project Overview

This assignment investigates the behavior of concurrent threads when they access shared resources. The objective is to understand how race conditions can occur in multi-threaded applications and how synchronization mechanisms can be used to protect shared data from corruption.

The project is divided into two parts: the first demonstrates the effects of unsynchronized access to a shared variable, while the second introduces a locking mechanism to ensure safe and predictable execution.

---

## Technical Report

### 1. Understanding Race Conditions

The results obtained in the first part highlight a common problem in concurrent programming known as a **race condition**.

A race condition appears when several threads attempt to access and modify the same shared variable at the same time without any synchronization mechanism. Because thread execution is controlled by the operating system scheduler, the order in which operations are performed cannot be predicted.

Although the instruction:

```python id="e4z9lx"
counter += 1
```

seems to be a single operation, it is actually composed of several internal steps:

1. Retrieve the current value of the counter.
2. Increase that value by one.
3. Store the updated value back in memory.

If two or more threads perform these steps simultaneously, one thread may overwrite the changes made by another. As a result, some increments are lost and the final value becomes lower than expected.

This explains why the counter obtained in Part 1 does not reach the theoretical result of **4,000,000**.

---

### 2. Using a Lock to Ensure Thread Safety

To prevent inconsistent updates, the second part introduces a synchronization mechanism using `threading.Lock()`.

A lock guarantees that only one thread can access the critical section of code at a given moment.

The process works as follows:

* A thread requests ownership of the lock before modifying the shared variable.
* If the lock is already being used by another thread, the requesting thread waits until it becomes available.
* Once the current thread finishes updating the counter, it releases the lock so that another thread may continue.

By forcing threads to execute the update operation one after another, simultaneous access to the shared variable is eliminated.

This controlled access prevents lost updates and ensures that every increment is correctly counted. Consequently, the final result matches the expected value of **4,000,000**.

---

## Execution Example

A document containing an example of the program execution is included:

**tp4 screen.pdf**

## How to Run the Program

Run the script from a Linux terminal or cloud-based environment using the following command:

```bash id="m3d2pa"
python3 thread_sync.py
```
