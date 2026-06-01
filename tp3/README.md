# Assignment 3: Process Management and Inter-Process Communication

## Elias Berrada

---

## Project Overview

The purpose of this assignment is to illustrate how operating systems manage processes and enable communication between them. The program creates a child process from a parent process and establishes a communication channel that allows data exchange between both entities.

The parent process sends a text message to the child process. The child then modifies the received string by reversing its content and converting all characters to uppercase before sending the result back to the parent process for display.

---

## Technical Report: Choice of Communication Method

To exchange information between the two processes, the project uses an **anonymous pipe implemented through `multiprocessing.Pipe()`**.

### Reasons for Choosing a Pipe

### 1. Direct Communication Between Two Processes

A pipe provides a dedicated communication channel linking exactly two processes. Since this project only requires interaction between one parent process and one child process, a pipe offers a simple and efficient solution without unnecessary complexity.

### 2. Bidirectional Data Exchange

The communication channel created by `Pipe()` supports two-way communication. This means the parent can send data to the child and receive a response using the same connection, reducing resource usage and simplifying implementation.

### 3. Built-in Synchronization

The `recv()` function waits until data becomes available before continuing execution. This behavior naturally synchronizes both processes and ensures that the parent does not attempt to read data before the child has completed its task.

---

## Process Creation

The child process is created using Python's multiprocessing module.

On Linux-based systems, launching a new process through `start()` relies on native operating system mechanisms for process creation. The child process inherits the communication endpoints required for the pipe, allowing both processes to exchange information while maintaining separate memory spaces.

---

## Execution Example

A document containing an example of the program execution is provided:

**tp3 screen.pdf**


## How to Run the Program

Execute the following command in a Linux terminal, Killercoda environment, or Google Colab session:

```bash
python3 process_ipc.py
```
