# def decor_result(result_func):
#     def distinction(marks):
#         for m in marks:
#             if m>=75:
#                 print('Distinction')
#         else:
#             result_func(marks)
#     return distinction
# @decor_result
# def result(marks):
#     for m in marks:
#         if m>33:
#             pass
#         else:
#             print('Fail')
#             break
#     else:
#         print("Pass")

# result([55,66,70,45,80])




# def create_adder(x):
#     def adder(y):
#         return x+y
 
#     return adder
 
# add_15 = create_adder(15)
 
# print(add_15(10))






def hello_decorator(func):
    def inner1(*args, **kwargs):
        print(args,kwargs)
        print("before execution")
        returned_value=func(*args, **kwargs)
        print("After Execution")
        return returned_value
    return inner1

@hello_decorator
def sum_two_numbers(a,b):
    print(a,b)
    print('Inside the function')
    return a+b

def main():
    a,b=1,2
    f1=sum_two_numbers(a,b)
    print('Sum is',f1)

main()
