# Assignment 2: File System Analysis

# Elias Berrada

## Project Overview

This assignment focuses on interacting with the Linux file system using Python. The program receives a directory path from the user, explores its contents, and retrieves important information about each file, including its size and access permissions.

The objective is to demonstrate how Python can communicate with the operating system and access file metadata through standard system interfaces.

---

## Technical Report: Libraries and Functions Used

To access file system information efficiently, the program relies on Python's built-in operating system modules. The following functions were selected for their direct relationship with Linux file management mechanisms:

### 1. `os.listdir(path)`

**Purpose:**
This function retrieves all entries contained in a specified directory. It allows the program to discover the files available for analysis.

**Justification:**
Internally, it relies on operating system services responsible for reading directory contents. This provides an efficient way to obtain file names without manually accessing low-level file system structures.

### 2. `os.stat(path)`

**Purpose:**
This function collects detailed metadata about a file.

**Justification:**
It provides direct access to information maintained by the operating system, such as file size, timestamps, ownership, and permission settings. In this project, it is mainly used to obtain the file size (`st_size`) and permission data (`st_mode`).

### 3. `stat.filemode()`

**Purpose:**
This utility converts permission information into a readable format.

**Justification:**
The permission values returned by the operating system are stored as numerical bit masks. Using `stat.filemode()` makes the output easier to understand by displaying permissions in the traditional Linux format, such as:

```text
-rw-r--r--
```

This representation clearly indicates read, write, and execute permissions for the owner, group members, and other users.

---

## Execution Example

A document containing an example of the program execution is included:

**tp2 screen.pdf**


## How to Execute the Program

To run the application in a Linux environment, Killercoda, or Google Colab, use the following command:

```bash
python3 file_analyzer.py
```
