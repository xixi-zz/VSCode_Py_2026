import os
def clear():
    os.system("clear")
def load_contacts(contacts):#加载
    try:
        with open("contacts.txt","r") as file:
            lines=file.readlines()
            if not lines:
                return
            for line in lines:
                First=line.split()
                name=First[0].split(":")[1]
                phone=First[1].split(":")[1]
                email=First[2].split(":")[1]
                contacts.append({'name':name,'phone':phone,'email':email})
    except FileNotFoundError:
        return
def save_contacts(contacts):#保存  
    with open("contacts.txt","w") as file:
        for person in contacts:
            file.write(
                f"name:{person['name']} " 
                f"phone:{person['phone']} "
                f"email:{person['email']}\n"
            )
def add_contact(contacts):#添加联系人  
    name=input("请输入待添加联系人名字:").strip()
    if not name:
        print("添加人名字不能为空")
        return
    for person in contacts:
        if name==person["name"]:
            print("添加失败，名字已存在")
            return
    phone=input("请输入待添加联系人电话:")
    if not phone:
        print("添加失败,电话号码不能为空")
        return
    email=input("请输入待添加联系人邮箱:")
    if not email:
        print("添加失败,邮箱不能为空")
        return
    contacts.append({"name":name,"phone":phone,"email":email})
    print("添加成功")
def delete_contact(contacts):#删除
    name=input("请输入要删除的联系人:").lower().strip()
    if not name:
        print("待删除名字不能为空")
        return
    flag=False
    for person in contacts:
        if name==person["name"].lower():
            contacts.remove(person)
            print("删除成功")
            return
    for person in contacts:
        if name in person["name"].lower():
            print(person["name"])
            flag=True
    if flag:
        rename=input("已显示所有相关联系人,请再次输入:").lower().strip()
        if not rename:
            print("待删除名字不能为空")
            return
        for person in contacts:
            if rename==person["name"].lower():
                contacts.remove(person)
                print("删除成功")
                break
        else:
            print("删除失败,未输入正确名字")  
    else:
        print("删除失败,暂无相关联系人信息")          
def update_contact(contacts):#替换
    name=input("请输入要修改的联系人").lower().strip()
    if not name:
        print("待修改名字不能为空")
        return
    flag=False
    for person in contacts:
        if name==person["name"].lower():
            newname=input("请输入修改后的名字:").strip()
            if not newname:
                print("修改失败,修改后的名字不能为空")
                return
            newphone=input("请输入修改后的电话号码:").strip()
            if not newphone:
                print("修改失败,修改后的电话不能为空") 
                return
            newemail=input("请输入要修改后的邮箱:").strip()
            if not newemail:
                print("修改失败,修改后的邮箱不能为空")
                return
            person["name"]=newname
            person["phone"]=newphone
            person["email"]=newemail
            print("修改成功")
            return
    for person in contacts:
        if name in person["name"].lower():
            print(person["name"])
            flag=True
    if flag:
        rename=input("已显示所有相关联系人,请再次输入:").lower().strip()
        if not rename:
            print("待修改名字不能为空")
            return
        for person in contacts:
            if rename==person["name"].lower():
                newname=input("请输入修改后的名字:").strip()
                if not newname:
                    print("修改失败,修改后的名字不能为空")
                    return
                newphone=input("请输入修改后的电话号码:").strip()
                if not newphone:
                    print("修改失败,修改后的电话不能为空") 
                    return
                newemail=input("请输入要修改后的邮箱:").strip()
                if not newemail:
                    print("修改失败,修改后的邮箱不能为空")
                    return
                person["name"]=newname
                person["phone"]=newphone
                person["email"]=newemail
                print("修改成功")
                break
        else:
            print("修改失败,未输入正确名字")  
    else:
        print("修改失败,暂无相关联系人信息")      
def search_contact(contacts):#查找
    name=input("请输入要查找的联系人名字:").lower().strip()
    if not name:
        print("查找失败,待查找联系人不能为空")
        return
    flag=False
    for person in contacts:
        if name==person["name"].lower():
            print("查找成功")
            print(f"name:{person['name']} "
                  f"phone:{person['phone']} "
                  f"email:{person['email']}"
                )
            return
    for person in contacts:
        if name in person["name"].lower():
            print(person["name"])
            flag=True
    if flag:
        rename=input("已显示所有相关联系人,请再次输入以获取详细信息:").lower().strip()
        if not rename:
            print("待查找名字不能为空")
            return
        for person in contacts:
            if rename==person["name"].lower():
                print("查找成功")
                print(f"name:{person['name']} "
                    f"phone:{person['phone']} "
                    f"email:{person['email']}"
                    )
                break
        else:
            print("此联系人不在通讯录中")  
    else:
        print("此联系人不在通讯录中")   
def view_contacts(contacts):#查看
    if not contacts:
        print("暂无任何联系人信息")
        return
    for person in contacts:
        print(f"name:{person['name']} "
            f"phone:{person['phone']} "
            f"email:{person['email']}\n"
            ) 
def main():
    contacts=[]
    load_contacts(contacts)
    while True:
        clear()
        print("---------通讯录---------")
        print("-----输入add添加联系人----")
        print("---输入delete删除联系人---")
        print("---输入update修改联系人---")
        print("---输入search查找联系人---")
        print("-----输入view查看联系人---")
        print("------输入exit退出-------")
        print("----可输入首字母执行操作---")
        choice=input("请选择你要执行的操作:").lower().strip()
        if choice in ("exit","e"):
            save_contacts(contacts)
            print("退出成功")
            return
        elif choice in ("add","a"):
            add_contact(contacts)
            input("请输入回车返回菜单...")
        elif choice in ("delete","d"):
            delete_contact(contacts)
            input("请输入回车返回菜单...")
        elif choice in ("update","u"):
            update_contact(contacts)
            input("请输入回车返回菜单...")
        elif choice in ("search","s"):
            search_contact(contacts)
            input("请输入回车返回菜单...")
        elif choice in ("view","v"):
            view_contacts(contacts)
            input("请输入回车返回菜单...")
        else:
            print("输入错误,请重新输入...")
main()

