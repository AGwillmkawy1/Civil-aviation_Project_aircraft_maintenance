# LaTeX Documentation Guide: Aircraft Predictive Maintenance

## Files Created

### 1. **Aircraft_Maintenance_Report.tex** (Technical Report)
A comprehensive, detailed technical report covering the entire CRISP-DM methodology.

**Contents:**
- Executive Summary with key results
- Phase 1: Business Understanding (success metrics, safety-first prioritization)
- Phase 2: Data Understanding (6,000 records, 30:1 class imbalance)
- Phase 3: Data Preparation (SMOTE methodology, feature scaling)
- Phase 4: Modeling (3-model comparison, Logistic Regression selection)
- Phase 5: Evaluation (confusion matrix, ROC-AUC, threshold optimization)
- Phase 6: Deployment (API specification, production artifacts)
- Key Trade-offs (Recall vs. Precision, Simple vs. Complex models)
- Limitations & Future Directions

**Page Count:** ~20 pages
**Audience:** Technical stakeholders, data scientists, ML engineers

---

### 2. **Aircraft_Maintenance_Presentation.tex** (Beamer Slides)
A professional presentation with 19 slides optimized for both technical and non-technical audiences.

**Slide Structure:**
1. Title Slide
2. Agenda
3. The Problem (reactive vs. predictive maintenance)
4. Business Objectives (safety-first metrics)
5. CRISP-DM Framework Overview
6. Data Understanding & Imbalance
7. SMOTE Solution
8. Model Comparison
9. Evaluation Results
10. Trade-off #1: Recall vs. Precision
11. Trade-off #2: Complex vs. Simple Models
12. Business Impact Projection
13. Deployment Architecture
14. Monitoring & Retraining
15. Key Findings Summary
16. Limitations & Future Directions
17. Key Takeaways (6 points)
18. Next Steps (actionable timeline)
19. Q&A Slide

**Audience:** All stakeholders (executives, engineers, mechanics)

---

## How to Compile

### Option 1: Using Online Tools (Easiest)
1. Go to **Overleaf.com** (free account)
2. Create new project → Upload files
3. Platform compiles automatically
4. Download PDF with one click

### Option 2: Local Compilation (Recommended)

**Prerequisites:**
- **Windows:** MiKTeX or TeX Live
- **macOS:** MacTeX
- **Linux:** TeX Live

**Commands:**

```bash
# Compile report
pdflatex Aircraft_Maintenance_Report.tex
pdflatex Aircraft_Maintenance_Report.tex  # Run twice for TOC

# Compile presentation
pdflatex Aircraft_Maintenance_Presentation.tex
```

Or use one-liner scripts:
```bash
# Windows PowerShell
for ($i=1; $i -le 2; $i++) { pdflatex Aircraft_Maintenance_Report.tex }
pdflatex Aircraft_Maintenance_Presentation.tex

# Linux/macOS
pdflatex Aircraft_Maintenance_Report.tex && pdflatex Aircraft_Maintenance_Report.tex
pdflatex Aircraft_Maintenance_Presentation.tex
```

### Option 3: Using VS Code with LaTeX Workshop
1. Install **LaTeX Workshop** extension
2. Open `.tex` file
3. Press `Ctrl+Alt+B` to build
4. PDF appears in `build/` directory

---

## Document Customization

### Change Colors
Edit color definitions in the preamble:
```latex
\definecolor{darkblue}{RGB}{0, 51, 102}      % Change main color
\definecolor{success}{RGB}{46, 204, 113}     % Change success indicators
```

### Add Company Logo (Presentation)
In `Aircraft_Maintenance_Presentation.tex`, add after `\begin{document}`:
```latex
\logo{\includegraphics[width=0.15\textwidth]{your_logo.png}}
```

### Modify Author/Date
```latex
\author{Your Name, Data Science Team}
\date{April 1, 2026}
```

### Change Report Title
```latex
\title{\Large\textbf{\textcolor{darkblue}{Your Custom Title}}}
```

---

## Key Content Highlights

### Report Unique Features
✓ **Table of Contents** with automatic page numbers
✓ **Detailed cost-benefit analysis** (FP vs FN trade-offs)
✓ **SMOTE mathematical explanation** with formulas
✓ **Cross-validation stability metrics**
✓ **Hyperparameter tuning results**
✓ **Monthly retraining workflow**

### Presentation Unique Features
✓ **19 visual slides** with clear progression
✓ **Confusion matrix visualization**
✓ **Business impact projections** ($2-5M savings)
✓ **Timeline for deployment** (actionable next steps)
✓ **Simple graphics** for stakeholder understanding
✓ **Trade-off explanations** with decision rationale

---

## What's Different from Standard Reports

### 1. **CRISP-DM Focus**
Both documents deeply explain each of the 6 CRISP-DM phases, showing how the methodology structures the project.

### 2. **Tradeoff Transparency**
Explicitly discusses:
- Why Recall > Precision (safety priority)
- Why Logistic Regression > XGBoost (simplicity)
- Why SMOTE on train-only (avoiding data leakage)

### 3. **Explainability for Non-Technical Stakeholders**
- Plain language explanations of ML concepts
- Cost analysis (dollars, not just metrics)
- Maintenance team perspective
- Business impact quantification

### 4. **Technical Rigor for Engineers**
- Formulas for key metrics
- Confusion matrix interpretation
- Data leakage prevention
- Cross-validation analysis
- Hyperparameter tuning results

### 5. **Actionable Deployment Guidance**
- API specifications with JSON schemas
- Production artifact list
- Monitoring SLAs
- Retraining schedule
- Red flags for data drift

---

## When to Use Each Document

| Situation | Document |
|-----------|----------|
| Present to executives | **Presentation** (Slides 12-14) |
| Present to technical team | **Presentation** (all slides) + **Report** |
| Audit/compliance review | **Report** (Phases 1-6) |
| Team onboarding | **Presentation** (overview) |
| Handoff to DevOps | **Report** (Phase 6: Deployment) |
| Monthly stakeholder update | **Presentation** (subset of slides) |
| Document project for archives | **Report** (complete reference) |

---

## PDF Output Details

### Report PDF
- **Format:** A4 (standard)
- **Pages:** ~20
- **Sections:** 9 (including appendices)
- **Features:** Headers/footers, table of contents, page numbers

### Presentation PDF
- **Format:** Widescreen (16:9)
- **Slides:** 19
- **Theme:** Madrid (professional blue scheme)
- **Features:** Navigable with bookmarks

---

## Troubleshooting Common LaTeX Issues

| Issue | Solution |
|-------|----------|
| `! Undefined control sequence` | Update LaTeX packages: `tlmgr update --all` |
| Tables overflow | Reduce table width: `\begin{tabularx}{0.8\textwidth}...` |
| Figures not showing | Use `[H]` for explicit positioning: `\begin{figure}[H]` |
| Colors not appearing | Ensure `xcolor` package loaded: `\usepackage{xcolor}` |
| Beamer theme errors | Use `\usetheme{Madrid}` instead of custom themes |

---

## Integration with Your Project

Both LaTeX files are now in your project root:
```
Civil aviation_Project_aircraft_maintenance/
├── Aircraft_Maintenance_Report.tex           ← Technical report
├── Aircraft_Maintenance_Presentation.tex     ← Presentation slides
├── notebooks/
├── src/
└── frontend/
```

**To generate PDFs in your workflow:**
```bash
# After updating project
pdflatex Aircraft_Maintenance_Report.tex && pdflatex Aircraft_Maintenance_Report.tex
pdflatex Aircraft_Maintenance_Presentation.tex

# Files generated:
# - Aircraft_Maintenance_Report.pdf
# - Aircraft_Maintenance_Presentation.pdf
```

---

## Sharing & Distribution

### For Email/Teams
- Send as PDF (smaller than LaTeX source)
- Include 1-page executive summary (first page of presentation)

### For Website/GitHub
- Convert to HTML: `pandoc file.tex -o file.html`
- Or embed PDF viewer

### For Printing
- Report: Print double-sided, color for figures
- Presentation: Print handout (6 slides per page)

---

## Next Steps

1. **Compile PDFs** using your preferred method (Overleaf, VS Code, or command line)
2. **Customize** colors/logos/author information
3. **Add figures** if you have visualization files (charts, confusion matrices)
4. **Present** to stakeholders using Beamer PDF
5. **Share** technical report for reference documentation

---

**Status:** ✓ Report and presentation ready for production use
**Last Updated:** March 31, 2026
