def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        ss=string[i:i+k]
        outStr=""
        for s in ss:
          if s not in outStr:
            outStr+=s
        print(outStr)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)