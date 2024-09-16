# LaTeX Revision Cleaner

## Overview

The **LaTeX Revision Cleaner** is a Python script designed to process LaTeX files containing revision commands `\add{...}` and `\rem{...}`. These commands are commonly used during document revisions to indicate additions and removals of text. The script generates a clean version of the LaTeX document by:

- Retaining the text inside `\add{...}` commands (the added text).
- Removing the text inside `\rem{...}` commands (the removed text).
- Ensuring proper spacing and formatting, so that words are neither glued together nor separated by extra spaces.
- Handling punctuation correctly, avoiding extra spaces before punctuation marks.
- Managing edge cases, such as commands within words or adjacent to punctuation.

This tool is particularly useful when preparing the final version of a LaTeX document after revisions, ensuring that all revision marks are cleaned up and the text flows naturally.

## Context of `\add{...}` and `\rem{...}` Commands

In collaborative document editing, especially academic papers and reports written in LaTeX, it's common to use custom commands to track changes during the revision process:

- **`\add{...}`**: Marks text that has been added during revisions.
- **`\rem{...}`**: Marks text that has been removed during revisions.

These commands help collaborators and reviewers identify changes between versions. However, before final submission or publication, it's necessary to remove these revision marks to produce a clean document.

## Features

- **Handles Nested Commands**: Correctly processes nested braces within `\add{...}` and `\rem{...}` commands.
- **Context-Aware Spacing**: Maintains proper spacing between words and around punctuation after removing or adding text.
- **Edge Case Management**: Handles commands that appear within words or adjacent to punctuation without disrupting the text flow.
- **Simple Usage**: Processes files quickly with a straightforward command-line interface.

## Usage

### Requirements

- Python 3.x

### Installation

No installation is required. Simply download the `clean_latex.py` script to your local machine.

### Running the Script

To process a LaTeX file:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `clean_latex.py` script and your LaTeX file.
3. Run the script using the following command:

   ```bash
   python clean_latex.py input.tex output.tex
   ```

   - Replace `input.tex` with the name of your original LaTeX file containing `\add{...}` and `\rem{...}` commands.
   - Replace `output.tex` with the desired name for the cleaned output file.

### Example

Given an input file `draft.tex` containing:

```latex
This is a sample document. \add{We have added this sentence.} \rem{This sentence has been removed.}

Here is a word with an \add{in}sertion and a re\rem{mov}al.
```

Running the script:

```bash
python clean_latex.py draft.tex final.tex
```

Produces `final.tex`:

```latex
This is a sample document. We have added this sentence.

Here is a word with an insertion and a removal.
```

## Notes

- The script preserves the original LaTeX formatting and commands outside of `\add{...}` and `\rem{...}`.
- It is recommended to keep a backup of your original file before processing.
- The script handles various edge cases, but testing with your specific document is advised to ensure all scenarios are covered.

## Acknowledgements

This script was developed with assistance from OpenAI's ChatGPT.

## License

[MIT License](LICENSE)
