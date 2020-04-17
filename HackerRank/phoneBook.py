# def searchPhoneBook(n, phoneBook, searchQuery):
#   for item in searchQuery:
#     for contact in phoneBook:
#       if contact[0]==item:
#         print("%s=%d" %(contact[0], contact[1]))
#       else:
#         print("Not found")
    
  

# searchPhoneBook([['Milon',12], ['Mi', 13], ['Ml', 14]], ['Mil', 'Mi', 'Ml'])

# list1={1:8, 2,10, 3:50, 4:100, 5:123}
# list2=[1, 4, 5, 6]
# result=[item for item in list2 if item in list1]
# print(result)
# for item in list2:
#   if item in list1:
#     print(item)
#   else:
#     print('Not Found')


n=int(input().strip())
phoneBook={}
for i in range(n):
  name, phone=input().strip().split(' ')
  phoneBook[name]=phone

while(True):
    try:
        queryName=input().strip()
        if queryName in phoneBook:
            print("{}={}".format(queryName, phoneBook[queryName]))
        else:
            print("Not Found")
    except EOFError:
        break


# import sys
# n = input()
# name_numbers = [raw_input().split() for _ in range(n)]
# phone_book = {k: v for k,v in name_numbers}
# ls = map(lambda x: x.strip(),sys.stdin.readlines())
# for name in ls:
#     if name in phone_book:
#         print('%s=%s' % (name, phone_book[name]))
#     else:
#         print('Not found')