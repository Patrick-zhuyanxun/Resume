# Resume Update Rules for AI Agents

**CRITICAL INSTRUCTIONS FOR AI ASSISTANTS:**
When prompted to update or modify the resumes in this repository, you MUST adhere to the following rules:

## 1. Bilingual Synchronization
- **Always maintain parity:** Any update made to the Chinese resume (`Chinese/resume.tex`) MUST be accurately translated and synced to the English resume (`English/resume.tex`), and vice versa.
- Do not let the two documents diverge in professional experience, academic history, or project details.

## 2. Formatting & Phrasing Standards
- **STAR Method:** Write all bullet points strongly adhering to the STAR (Situation, Task, Action, Result) format.
- **Action Verbs:** Start bullet points (especially in English) with strong action verbs (e.g., *Engineered*, *Architected*, *Developed*, *Optimized*).
- **Quantitative Metrics:** Always prioritize and highlight quantitative metrics (e.g., "achieved 90% success rate", "improved latency to 10 seconds", "annotated 3,000 images"). Never invent these numbers; query the user if metrics are missing.
- **Conciseness:** Keep bullet points under two lines if possible. Remove redundant or overly detailed descriptive text. ATS systems and recruiters favor brevity and impact.

## 3. Technical Stack Alignment
- Ensure that the tools, libraries, and frameworks listed in the "Technical Skills" section match the tools mentioned in the actual bullet points of the Experience and Projects sections.
- When adding a new project, verify if a new technical skill needs to be appended to the bottom section.

## 4. Compilation & Verification
- **Compilation Engine:** You MUST compile the `resume.tex` files using `xelatex`. Standard `pdflatex` will fail due to the `xeCJK` and `fontspec` packages used for CJK characters and specific fonts (Arial / Microsoft JhengHei).
- **Verification:** After modifying the `.tex` files, always run `xelatex resume.tex` in both directories to ensure no syntax errors were introduced and that the PDF was generated successfully.

## 5. Version Control Workflow
- Create a new branch with the current date before making extensive changes: `git checkout -b YYYY-MM-DD`.
- When work is finalized and approved by the user, draft a commit detailing the specific additions or removals.
- Create a tag for the release: `git tag YYYY-MM-DD`.
- Push the changes to the user's remote repository (both the branch and the tag).
