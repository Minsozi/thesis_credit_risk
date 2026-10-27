"""
Build Full Thesis Manuscript
Concatenates front matter, chapters 1 to 6, and references into a single cohesive dissertation.
"""

from pathlib import Path

base = Path(r"C:\Users\201061589\Documents\thesis_credit_risk\thesis")
chapters_dir = base / "chapters"

files = [
    "front_matter.md",
    "chapter_1_introduction.md",
    "chapter_2_literature_review.md",
    "chapter_3_methodology.md",
    "chapter_4_results_and_evaluation.md",
    "chapter_5_sociotechnical_and_regulatory_analysis.md",
    "chapter_6_conclusions_and_future_work.md",
    "references.md"
]

combined = []
for f in files:
    p = chapters_dir / f
    if p.exists():
        content = p.read_text(encoding="utf-8")
        combined.append(content)
        combined.append("\n\n---\n\n")
        print(f"Added {f} ({len(content)} characters)")
    else:
        print(f"MISSING: {f}")

master_path = base / "full_thesis_manuscript.md"
master_path.write_text("".join(combined), encoding="utf-8")
print(f"\nMaster thesis created at: {master_path} (Total size: {master_path.stat().st_size} bytes)")
