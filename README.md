# Deep-Thought

This is the official documentation and implementation(s) of Deep Thought — language used by Deep Thought supercomputer to calculate the answer to the Ultimate Question of Life, the Universe, and Everything.

## Project structure.

| Path        | Description                  |
|-------------|------------------------------|
| `README.md` | The main documentation file. |

## Deep Thought commands.

Deep Thought supports eight commands:

| Command  | Description                                                                            |
|----------|----------------------------------------------------------------------------------------|
| `101010` | Increments the value of the current cell.                                              |
| `010101` | Decrements the value of the current cell.                                              |
| `100`    | Moves the pointer to the right.                                                        |
| `111`    | Moves the pointer to the left.                                                         |
| `000`    | Outputs the ASCII value of the current cell.                                           |
| `001`    | Inputs a value and stores it in the current cell.                                      |
| `\n`     | Jumps to the next corresponding `\n\n` if the value of the current cell is zero.       |
| `\n\n`   | Jumps to the previous corresponding `\n` if the value of the current cell is non-zero. |

Each command is unambiguous and does represent one of the features of the Answer to the Ultimate Question of Life, the Universe, and Everything.

That is because binary representation of the number `42` is `101010`, and inverse is `010101`.
The rest of the commands are the binary representation of the dividers ща 42б that is `0`, `1`, `4`, `7`.

## To do.

| Path                          | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| `tests/test_deep_thought.py`  | The tests for the Deep Thought implementation.                |
| `interpreter/deep_thought.py` | The Python implementation of the Deep Thought language.       |
| `interpreter/deep_thought.s`  | The x86 assembly implementation of the Deep Thought language. |
| `compiler/deep_thought_jit.s` | The x86 assembly JIT compiler for the Deep Thought language.  |
| `documentation/main.tex`      | The LaTeX documentation of the Deep Thought language.         |