exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = []
top_students = []
best_student = ("",0)

failed_students = [students for students, points in exam_points.items() if points <46]
print(failed_students)
top_students = [students for students, points in exam_points.items() if points > 90]
print(top_students)
max_point = 0
best_student = max(exam_points.items(), key= lambda x: x[1])
print(best_student)