one, two = map(int,input("두 수 입력 : ").split())
def calc(one, two) :
    if one > two :
        return one - two
    else :
        return two - one
print("결과 :", calc(one,two))
print()


num1, num2 = map(int,input("두 수 입력 : ").split())
def same(num1, num2) :
    print("결과 :",end='')
    for i in range(1, 101) :
        if i % num1 == 0 and i % num2 == 0 :
            print("{} ".format(i),end='')
        else :
            continue
same(num1, num2)
print()

print()


str1 = int(input("숫자 입력 : "))
def Even_Number(str1) :
    if str1 % 2 == 0 and str1 != 0:
        return "짝수입니다"
    elif str1 == 0 :
        return "0입니다"       
    else :
        return "홀수입니다"
print("함수1 :",Even_Number(str1))

def Even_Number2(str1) :
    print("함수2 : ",end='')
    if str1 % 2 == 0 and str1 != 0:
        print("짝수입니다")
    elif str1 == 0 :
        print("0입니다")
    else :
        print("홀수입니다")
Even_Number2(str1)
    

