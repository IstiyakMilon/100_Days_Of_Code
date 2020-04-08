def gradingStudents(grades):
  finalGrade=[]
  for grade in grades[1:]:
    if grade>95:
      if (100-grade)<3:
        finalGrade.append(100)
      else:
        finalGrade.append(grade)
    elif grade>90:
      if (95-grade)<3:
        finalGrade.append(95)
      else:
        finalGrade.append(grade)
    elif grade>85:
      if (90-grade)<3:
        finalGrade.append(90)
      else:
        finalGrade.append(grade)
    elif grade>80:
      if (85-grade)<3:
        finalGrade.append(85)
      else:
        finalGrade.append(grade)
    elif grade>75:
      if (80-grade)<3:
        finalGrade.append(80)
      else:
        finalGrade.append(grade)
    elif grade>70:
      if (75-grade)<3:
        finalGrade.append(75)
      else:
        finalGrade.append(grade)
    elif grade>65:
      if (70-grade)<3:
        finalGrade.append(70)
      else:
        finalGrade.append(grade)
    elif grade>60:
      if (65-grade)<3:
        finalGrade.append(65)
      else:
        finalGrade.append(grade)
    elif grade>55:
      if (60-grade)<3:
        finalGrade.append(60)
      else:
        finalGrade.append(grade)
    elif grade>50:
      if (55-grade)<3:
        finalGrade.append(55)
      else:
        finalGrade.append(grade)
    elif grade>45:
      if (50-grade)<3:
        finalGrade.append(50)
      else:
        finalGrade.append(grade)
    elif grade>40:
      if (45-grade)<3:
        finalGrade.append(45)
      else:
        finalGrade.append(grade)
    elif grade>35 or grade<=35:
      if (40-grade)<3:
        finalGrade.append(40)
      else:
        finalGrade.append(grade)
  return finalGrade


        

print(gradingStudents([4, 73, 67, 38, 33]))