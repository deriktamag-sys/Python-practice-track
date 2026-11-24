###
# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)
# show(4)

# #Factorial using recursion
# def fact(n):
#     if(n==0 or n==1):
#         return 1 
#     else:
#          return n*fact(n-1)
# print(fact(4))

# ##sumt to first n natural numbers using recursion
# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1)+n

# sum_cal=sum(4)
# print(sum_cal)


#to print the list using the recursive function'
def _list(list,idx=0):
    if(idx == len(list)):
        return

    print(list[idx])
    _list(list,idx+1)
fruits = ["mango","banana","apple","kiwi"]
_list(fruits)

