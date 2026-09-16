# Parallel Syntax Highlighter

**Evidence 1 — Implementation of Computational Methods (Group 602)**
Tecnológico de Monterrey

## Authors

- Regina Fernanda Portela Palacios (A01786698)
- Nicolás Casillas Larrañaga (A01787292)

## Description

A lexical analyzer (lexer) built on a Deterministic Finite Automaton (DFA) that takes a Python (`.py`) source file as input and outputs an `.html` file with syntax-highlighted code. Each lexical token category is rendered in a distinct color, making the token structure of the code visually explicit.

## Token Categories & Colors

| Color | Category |
|---|---|
| 🔴 Red | Keywords (reserved words) |
| ⚫ Black | Identifiers |
| 🌸 Pink | Operators |
| 🟢 Green | Delimiters |
| 🔵 Blue | Literals |
| 🟠 Orange | Comments |
| 🟣 Purple | Error |

## How It Works

The highlighter is implemented as a DFA-based lexer:

1. **Input:** a `.py` source file.
2. **Scanning:** the automaton reads the file character by character, transitioning between states based on the current character's class (letter, digit, symbol, quote, `#`, etc.).
3. **Acceptance states:** each accepting state maps to one of the token categories above (Identifiers, Keywords, Delimiters, Operators, Literals, Comments) or to an Error state for unrecognized sequences.
4. **Output:** tokens are wrapped in HTML with the corresponding color per category, producing a fully highlighted `.html` version of the source file.

The full state-transition table and the DFA diagram (with states 0–19, including dedicated branches for literals, operators, comments, identifiers/keywords, and delimiters) are included in the project report.

## Algorithm Complexity

The lexer scans the input linearly — each character is read once to determine its token category — giving the algorithm a time complexity of **O(n)**.

## Design Notes

- Handling **acceptance states** was the most challenging part of the implementation: in some cases the pointer had to be backtracked to avoid over-consuming characters, and transitions had to be carefully ordered to respect the required matching hierarchy (e.g. distinguishing keywords from identifiers).
- Separating tokens by color in the HTML output made it much clearer how the automaton groups operators, reserved words, identifiers, and other categories automatically.

## Reflection

Tools like this can meaningfully support accessibility and education: well-highlighted code is easier to read, helping people learn to program more intuitively and, over time, helping close the digital divide. Because of this, it's important to validate that the tool behaves correctly before sharing or using it — a broken or misleading highlighter risks confusing users, which runs counter to the tool's purpose. More broadly, the ethical implications of any technology should be considered before it's deployed.

## Repository Structure

```
├── Documentation/        # DFA implementation and lexer logic
├── ejemplo.py            # example to highlight
├── lexerProyecto1.py     # Lexer implementation             
├── README.md
└── resultado.html        # HTML that shows results
```
