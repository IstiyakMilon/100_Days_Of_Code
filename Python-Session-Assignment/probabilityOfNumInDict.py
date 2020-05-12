# List = [2, 1, 2, 99, 4, 99, 21, 99, 8, 17]
List = [1, 1, 2, 1, 4, 99, 21, 99, 8, 7] 
prob_list={x:List.count(x)/len(List) for x in List}
print(prob_list)
