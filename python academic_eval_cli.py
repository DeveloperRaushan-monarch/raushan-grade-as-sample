# academic_eval_midterm_annual.py
from dataclasses import dataclass
from typing import Dict

# -----------------------------
# Data Models
# -----------------------------

@dataclass
class Student:
    id: str
    name: str
    scores: Dict[str, float]  # {"Midterm": ..., "Annual": ...}

# -----------------------------
# Helper Functions
# -----------------------------

def letter_grade(percent: float) -> str:
    """Convert percentage to letter grade."""
    if percent >= 90: return "A"
    elif percent >= 80: return "B"
    elif percent >= 70: return "C"
    elif percent >= 60: return "D"
    else: return "F"

def evaluate_student(student: Student, assessments: Dict[str, int]) -> Dict:
    """Evaluate one student based on Midterm and Annual exam scores."""
    total = 0
    max_total = 0
    results = []

    for exam, max_score in assessments.items():
        score = student.scores.get(exam, 0)
        percent = round(score / max_score * 100, 2)
        results.append({
            "exam": exam,
            "score": score,
            "max": max_score,
            "percent": percent,
            "grade": letter_grade(percent)
        })
        total += score
        max_total += max_score

    final_percent = round(total / max_total * 100, 2)
    return {
        "student": student.name,
        "results": results,
        "final_percent": final_percent,
        "final_grade": letter_grade(final_percent)
    }

# -----------------------------
# Main Program (CLI)
# -----------------------------

def main():
    print("=== Academic Performance Evaluation System ===")
    print("Assessments: Midterm & Annual Exam")

    # Fixed assessments
    assessments = {"Midterm": 80, "Annual": 100}

    # Step 1: Input student data
    students = []
    num_students = int(input("\nEnter number of students: "))
    for i in range(num_students):
        sid = f"S{i+1}"
        name = input(f"\nEnter name for student {i+1}: ")
        scores = {}
        for exam, max_score in assessments.items():
            while True:
                try:
                    val = float(input(f"  Score for {exam} (max {max_score}): "))
                    if 0 <= val <= max_score:
                        scores[exam] = val
                        break
                    else:
                        print(f"⚠️ Enter a value between 0 and {max_score}")
                except ValueError:
                    print("⚠️ Invalid input, please enter a number.")
        students.append(Student(id=sid, name=name, scores=scores))

    # Step 2: Generate reports
    print("\n=== REPORT CARDS ===")
    for s in students:
        report = evaluate_student(s, assessments)
        print(f"\n--- {report['student']} ---")
        for r in report["results"]:
            print(f"{r['exam']}: {r['score']}/{r['max']} "
                  f"({r['percent']}%) -> {r['grade']}")
        print(f">>> Final: {report['final_percent']}% "
              f"Grade: {report['final_grade']}")

# -----------------------------
# Run Program
# -----------------------------

if __name__ == "__main__":
    main()
