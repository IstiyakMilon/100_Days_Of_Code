def second_highest(arr):
    student_marks={}
    num=len(arr)
    marks=set([arr[i][0] for i in range(num)])
    
    for i in range(num):
      if round(arr[i][0],2) not in student_marks:
        student_marks[arr[i][0]]=[arr[i][1]]
      else:
        student_marks[arr[i][0]].append(arr[i][1])
    marks=list(marks)
    marks.sort()
    print(marks)
    final_result=student_marks[marks[1]]
    final_result.sort()
    for name in final_result:
      print(name)



second_highest([[37.21,'Harry'], [37.21,'Berry'],  [37.20,'Tina'],  [41.00,'Akriti'],  [39.00,'Harsh'] ])