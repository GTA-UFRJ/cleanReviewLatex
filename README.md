# Cleaning Latex files for review

## **Overview**

The Python script `clean_latex.py` is designed to process a LaTeX file that contains custom commands `\add{...}` and `\rem{...}`, which represent additions and removals in the text, respectively. The goal of the script is to produce a clean version of the LaTeX file where:

- Text inside `\add{...}` is retained (the added text is kept).
- Text inside `\rem{...}` is removed.
- Proper spacing is maintained, ensuring that words are neither stuck together nor separated by extra spaces.
- Punctuation is correctly handled, without introducing spaces before punctuation marks.
- Edge cases, such as `\add{...}` and `\rem{...}` appearing within words or adjacent to punctuation, are correctly managed.
