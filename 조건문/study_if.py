a = 100
b = 200

if a == b:  #조건문에 해당
    print("same")
    print("{}는 {}와 같다.".format(a, b)) #a와 b의 값을 이와 같은 방법으로 넣는다.
else: #조건이 충족되지 않을 경우
    print("different")
    print("{}는 {}와 다르다.".format(a, b))
    if a > b:
        print("{} > {}".format(a, b))
    else:
        print("{} < {}".format(a, b))

print("Finished")