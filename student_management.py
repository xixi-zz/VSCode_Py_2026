people=[]
flag=True
while flag:
    print("-----学生信息档案表-----")
    print("------输入exit退出-----")
    print("----输入add添加信息-----")
    print("----输入update修改信息---")
    print("---输入delete删除信息---")
    print("---输入search查找某人信息--")
    print("--输入view查看所有信息---")
    print("可输入首字母来表示想要的操作")
    choice=input("请做出选择:").lower()
    if choice in ("exit","e"):
        print("退出成功")
        break
    elif choice in ("add","a"):
        people.append({'name':input("Name:"),'age':input("Age:"),'number':input("Number:")})
        print("添加成功")
    elif choice in ("update","u"):
        name=input("Name:")
        for person in people:
            if person['name']==name:
                person['name']=input("newname:")
                person['age']=input("newage:")
                person['number']=input("newnumber:")
                print("修改成功")
                break
        else:
            print("库中不存在这个人")
    elif choice in ("delete","d"):
        name=input("Name:")
        for person in people:
            if person['name']==name:
                people.remove(person)
                print("删除成功")
                break
        else:
            print("库中不存在这个人")
    elif choice in ("search","s"):
        name=input("Name:")
        for person in people:
            if person['name']==name:
                print(f"Name:{person['name']} Age:{person['age']} Number:{person['number']}")
                break
        else:
            print("库中不存在这个人")
    elif choice in ("view","v"):
        if not people:
            print("库中暂无数据")
        else:
            for person in people:
                print(f"Name:{person['name']} Age:{person['age']} Number:{person['number']}")
        
    