message = "내 이름은 철수이고, 파이썬을 좋아합니다."

# split
word_list = message.split(" ") #해당하는 문자를 기준으로 message를 나눕니다.

for w in word_list:
    print(w)

# join
joined_string = '--'.join(word_list) #쓰는방법이 특이하므로, 기억해둘것
print("\n" + joined_string) #해당하는 문자를 가지고 합친다.

# replace
print(message.replace(' ', '~')) #왼쪽의 문자열을 오른쪽의 문자열로 바꾼다.
print(message.replace('이', '2'))

# upper
eng_string = "My name is HwangDongJun"
print(eng_string.upper()) #전부다 대문자로

# lower
print(eng_string.lower()) #전부다 소문자로

# startswitch
print(eng_string.startswith('I am')) #해당 문자열로 시작하는지에 따라 bool값을 return
print(eng_string.startswith('My name'))

# endswitch
print(eng_string.endswith('Jun')) #마지막에 어떻게 오느냐에 따른 bool값을 return