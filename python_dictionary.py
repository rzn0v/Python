student_scores = {
  "Bennett": 81,
  "Zhongli": 78,
  "Ayato": 99, 
  "Cyno": 74,
  "Neuvillette": 62,
}
student_grades={}
for student in student_scores:
  scores=student_scores[student]
  if scores>90:
    student_grades[student]="Outstanding"
  elif scores>80:
    student_grades[student]="Exceeds Expectations"
  elif scores>70:
    student_grades[student]="Acceptable"
  else:
    student_grades[student]="Fail"
print(student_grades)