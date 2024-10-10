def sumfunc(n):
    return sum(range(1, n+1))

try:
    number = int(input("1이상의 정수를 입력 하세요 : "))
    if number >= 1:
        result = sumfunc(number)
        print(f"1~{number}까지 정수의 합은 {number} 입니다.")
        if result == 210:
            print("합은 210 입니다. ")
    else:
        print("1이상의 정수를 입력해주세요.")
except ValueError:
    print("유효한 정수를 입력하세요.")