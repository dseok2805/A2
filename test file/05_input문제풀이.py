one, two = map(int,input("가로, 세로 입력 : ").split())
area = one * two
print( "면적은 {}입니다.".format(area) )
print()

num1, num2 = map(int,input("두 수 입력 : ").split())
plus = num1 + num2
minus = num1 - num2
mul = num1 * num2
div = num1 / num2
print( "11 + 3 = {}".format(plus) )
print( "11 - 3 = {}".format(minus) )
print( "11 * 3 = {}".format(mul) )
print( "11 / 3 = {:.2f}".format(div) )
print()

time = int(input("주차 시간 : "))
print("주차요금은 ", ((time // 60)*1000 + (time - 60)*100),"원 입니다",sep='')
print()

money = int(input("시급을 입력해주세요 : "))
daytime = int(input("일일 근무 시간 : "))
monthday = int(input("한달 근무 일수 : "))
total = money * daytime * monthday
print( "예상 월급은 : {}".format(total), "원 입니다",sep='' )
print()

print("1513600원으로 무엇을 할 수 있을까요?")
print("PC방(1200원 기준) : " , total // 1200 , "시간",sep='')
print("점심(7000원 기준) : " , total // 7000 , "끼",sep='')
print("영화(11000원 기준) : " , total // 11000 , "편",sep='')
print("노래방(20000원 기준) : " , total // 20000 , "시간",sep='')
