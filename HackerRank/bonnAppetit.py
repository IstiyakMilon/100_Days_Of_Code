def bonAppetit(bill, k, b):
  originalBillTotal=0
  for i in range(len(bill)):
    if i==k:
      continue
    originalBillTotal+=bill[i]
  if originalBillTotal/2==b:
    print("Bon Appetit")
  else:
    print(b-(originalBillTotal//2))


bonAppetit([1,2,3],1,3)