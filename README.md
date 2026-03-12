# Patrick Zhu (朱彥勳) - Resume

This repository contains the LaTeX source code and compiled PDF files for both the English and Chinese versions of Patrick Zhu's resume.

## Directory Structure
- `Chinese/`: Contains `resume.tex` (XeLaTeX) and the compiled `resume.pdf` for the Traditional Chinese resume.
- `English/`: Contains `resume.tex` (XeLaTeX) and the compiled `resume.pdf` for the English resume.
- `portfolio_text.txt`: The raw extracted text from the original portfolio used as a reference for resume content generation.
- `RULES.md`: CRITICAL guidelines for any AI agent or maintainer tasked with modifying these files.

## Compilation Instructions
Both resumes use the `XeLaTeX` engine to ensure proper support for typography and CJK (Chinese, Japanese, Korean) characters.

To compile a resume:
```bash
cd Chinese/ # or cd English/
xelatex resume.tex
```

## Version Control Workflow
1. Create a branch named after the current date (e.g., `git checkout -b YYYY-MM-DD`).
2. Make necessary content additions or layout adjustments to the `.tex` files.
3. Commit the changes and compile the PDF files.
4. Add a Git Tag with the date `git tag YYYY-MM-DD`.
5. Push the changes to GitHub.
