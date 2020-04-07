def staircase(n):
  
  for i in range(n):
    string=""
    k=n-i-1
    for j in range(0, k):
      string+=" "
    for l in range(0,i+1):
      string+="#"
    print(string)
staircase(4)
# def pypart2(n): 
      
#     # number of spaces 
#     k = 2*n - 2
  
#     # outer loop to handle number of rows 
#     for i in range(0, n): 
      
#         # inner loop to handle number spaces 
#         # values changing acc. to requirement 
#         for j in range(0, k): 
#             print(end=" ") 
      
#         # decrementing k after each loop 
#         k = k - 2
      
#         # inner loop to handle number of columns 
#         # values changing acc. to outer loop 
#         for j in range(0, i+1): 
          
#             # printing stars 
#             print("* ", end="") 
      
#         # ending line after each row 
#         print("\r")

# pypart2(4)