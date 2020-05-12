List_students = [('Sadat', 66), ('Shamsun', 64), ('Shakib', 69), ('Soumya', 72)]
List_class = [3, 6, 3, 3]
class_height={}
for i in range(len(List_class)):
  if List_class[i] not in class_height:
    class_height[List_class[i]]=List_students[i][1]
  else:
    class_height[List_class[i]]+=List_students[i][1]
class_height_average={key:value/List_class.count(key) for key, value in class_height.items()}
print(class_height_average)