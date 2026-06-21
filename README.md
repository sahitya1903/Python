# Python Practice & Projects

Welcome to the **Python Practice & Projects** repository! This repository contains a curated collection of Python programs ranging from basic language fundamentals and mathematical problems to advanced data structure implementations, CLI mini-projects, and university course assignments.

---

## 📂 Repository Structure

The code is organized into topic-specific folders to make it easy to navigate and review:

| Folder | Description | Key Contents |
| :--- | :--- | :--- |
| [📂 Basic_Programs](./Basic_Programs/) | Python basics, arithmetic operations, loops, math utilities, recursion, and patterns. | Basic syntaxes, patterns, LCM, Armstrong numbers, prime numbers, dictionary/list/string practices. |
| [📂 Data_Structures_and_Algorithms](./Data_Structures_and_Algorithms/) | Formally implemented classical data structures and algorithms in Python. | Stack, Linear Queue, Circular Queue, Priority Queue, BST (Binary Search Tree), LinkedList (DLL, CLL), Sorting, Searching. |
| [📂 Lab_and_Assignments](./Lab_and_Assignments/) | Academic laboratory files, assignments, and exam/PYQ solutions. | `cslab.py` (comprehensive B.Tech I lab questions), `assignment1/2/3.py`, `pyq.py`. |
| [📂 Mini_Projects](./Mini_Projects/) | Standalone utility applications and console-based CLI games. | Hotel Management System (MySQL connected), Rock-Paper-Scissors (with Login/Register authentication), Translator, Turtle graphics. |
| [📂 File_Handling](./File_Handling/) | Demonstration of Python's built-in file handling capabilities. | Reading/writing text files, parsing character/word statistics alongside sample datasets (`story.txt`, `alpha.txt`). |
| [📂 Practice_and_Misc](./Practice_and_Misc/) | Rough scripts, video helper tools, and general scratchpads. | Scratch codes, `videoduration.py` calculator, `practice.py` variations. |

---

## 🎯 Highlights

### 🏨 Hotel Management System (`Mini_Projects/new.py`)
A comprehensive Hotel Management CLI application featuring:
- **MySQL Integration**: Persistent database storing customer details, booking records, and billing details.
- **Comprehensive Billing**: Calculates Room Rent, Restaurant meals, Gaming lounge hours, and Fashion Store shopping items to generate a consolidated checkout bill.

### 🎮 Rock Paper Scissors with CLI Authentication (`Mini_Projects/website.py`)
A console application simulating website-like user authentication:
- **Sign-Up/Login**: Enforces strict password policies (mixture of lower/uppercase characters, symbols, minimum 8 characters).
- **RPS Game**: An interactive rock-paper-scissors session against the computer with scoreboard capability.

### 🌳 DSA Implementations (`Data_Structures_and_Algorithms/`)
Implementations from scratch of classical data structures:
- **Linked Lists**: Circular Linked List ([cll.py](./Data_Structures_and_Algorithms/cll.py)), Doubly Linked List ([dll.py](./Data_Structures_and_Algorithms/dll.py)), and Linked List Rotations ([llrotation.py](./Data_Structures_and_Algorithms/llrotation.py)).
- **Queues**: Circular Queue ([circularqueue.py](./Data_Structures_and_Algorithms/circularqueue.py)) and Priority Queue ([priorityqueue.py](./Data_Structures_and_Algorithms/priorityqueue.py)).
- **Trees & Graphs**: Binary Search Trees with In-order traversals ([bst.py](./Data_Structures_and_Algorithms/bst.py)) and Adjacency List Graph traversals ([graphs.py](./Data_Structures_and_Algorithms/graphs.py)).

---

## 🚀 Getting Started

### Prerequisites
Make sure you have [Python 3.x](https://www.python.org/) installed. 

For the Hotel Management System script to function correctly, install the MySQL Connector:
```bash
pip install mysql-connector-python
```

### Running the Programs
To run any script, navigate to its parent directory and execute it using Python:

```bash
python Basic_Programs/fibonacci.py
```

---

## 📄 License
This repository is licensed under the [MIT License](./LICENSE) - see the `LICENSE` file for details.
