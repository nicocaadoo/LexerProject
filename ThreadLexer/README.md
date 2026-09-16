# Parallel Syntax Highlighter — Multi-File Processing

**Evidence 2 — Implementation of Computational Methods**
Tecnológico de Monterrey

## Authors

- Regina Fernanda Portela Palacios
- Nicolás Casillas Larrañaga

## Description

This project extends the [lexical syntax highlighter built in Evidence 1](#) to support processing **multiple Python source files** at once. The program accepts a list of paths — which can be individual files or directories — automatically identifies files with a `.py` extension, and generates a corresponding syntax-highlighted `.html` file for each one. This automates the analysis of many files without needing to run the tool manually per file.

## Approaches Implemented

Two versions of the multi-file processing pipeline were implemented and compared:

- **Sequential version:** files are processed one after another.
- **Parallel version:** built on execution threads, allowing multiple files to be analyzed simultaneously.

Since the processing of each file is independent of the others, the problem is well suited to parallelization — this approach makes better use of system resources and reduces the total time required to complete the analysis.

## Core Algorithm

The lexical highlighting itself is based on the same **Deterministic Finite Automaton (DFA)** approach from Evidence 1, represented via a transition table. The program scans each character of a file, determines its category, and transitions between states until it identifies the different token types: keywords, identifiers, operators, numbers, comments, and string literals.

## Code Conventions

- Descriptive names for functions and variables
- Clear program structure and consistent indentation
- Comments to aid readability
- Basic exception handling to avoid unexpected failures while reading/processing files

## Performance Evaluation

Execution time was measured for both versions to directly compare the sequential and parallel implementations and calculate the resulting speedup.

- The parallel version generally showed better execution times, since work is distributed across multiple threads, reducing the total time needed to process the file set.
- The observed improvement depends on factors such as the number of files, their size, and the overhead of thread creation and synchronization.

## Complexity Analysis

The theoretical time complexity of the algorithm is **O(N)**, where N is the total number of characters processed — each character is analyzed exactly once via the automaton's transitions. When processing multiple files, complexity remains linear with respect to the total number of characters analyzed across all files. Experimental results were consistent with this: execution time increased approximately proportionally to the total input size.

## Ethical Considerations

Automated code-analysis tools like this one can improve educational processes, boost developer productivity, and automate repetitive tasks. However, they could also be misused to inspect code without authorization or to excessively monitor others' work. It's essential that these technologies be used responsibly, respecting privacy, intellectual property, and the ethical principles associated with handling digital information.

## Repository Structure

> ✏️ *Adjust to match the actual files once organized in the repo, for example:*

```
├── lexer.py              # DFA implementation and lexer logic
├── highlighter.py        # HTML generation from tokenized output
├── sequential_runner.py  # Sequential multi-file processing
├── parallel_runner.py    # Thread-based parallel multi-file processing
├── benchmarks/           # Timing results / speedup comparisons
├── examples/              # Sample .py inputs and generated .html outputs
└── README.md
```

## Usage

> ✏️ *Fill in with the actual CLI/usage once confirmed, for example:*

```bash
# Sequential
python sequential_runner.py path1.py path2.py my_dir/

# Parallel
python parallel_runner.py path1.py path2.py my_dir/
```
