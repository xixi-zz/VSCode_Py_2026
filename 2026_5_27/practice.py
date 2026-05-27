#输入
s = "Name:Tom Age:18 Number:123"
#输出Tom 18 123
#code:
first=s.split()
for i in range(3):
    second=first[i].split(":")
    print(second[1])


#输入
nums = [8,2,5,1,9]
#要求升序和降序输出
#code:
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

#输入
people = [
    {"name":"Tom","age":18},
    {"name":"Jack","age":20},
    {"name":"Bob","age":16}
]
#要求按年龄和名字排序
#code:
people.sort(key=lambda x:x["name"])
print("按名字排序")
for person in people:
    print(person)
people.sort(key=lambda x:x["age"])
print("按年龄排序")
for person in people:
    print(person)


#输入
word=["I","love","zz"]
# #要求I-love-zz
s="-".join(word)
print(s)


#输入
s = "student_system"
#输出
#student system
print(s[0:7])
print(s[8:14])