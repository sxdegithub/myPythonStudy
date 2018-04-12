# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: sx

# 2018年3月10日23:56:42 可以完成读写

# 存储文件位置
contactsFile = r"D:\python\helloWorld\Contacts\contactsFile2.dat"
# 用来存联系人
contactsDic = {}


# 存入联系人
def add_contacts():
    with open(contactsFile, 'r', encoding='utf-8') as f:
        for line in f:
            (key, value) = line.strip().split(':')
            contactsDic[key] = value

    print(contactsDic)
    # 输入姓名

    input_name_true = True
    input_num_true = True
    while input_name_true:
        set_name_info = input("请输入姓名:")
        if (len(set_name_info) > 0) and (len(set_name_info) < 20):
            input_name_true = False

    # 输入手机号
    while input_num_true:
        set_phone_info = input("请输入手机号:")
        if (len(set_phone_info) > 0) and (len(set_phone_info) < 20):
            input_num_true = False

    # 姓名对应的电话号码存入
    contactsDic[set_name_info] = set_phone_info
    print(contactsDic)
    # 将字典存入txt文件中
    with open(contactsFile, 'w+', encoding='utf-8', newline='\n') as f:
        for (key, value) in contactsDic.items():
            f.write('%s:%s\n' % (key, value))

    contactsDic.clear()


# 查找联系人对应的号码
def find_number_by_name():
    with open(contactsFile, 'r', encoding='utf-8') as f:
        for line in f:
            (key, value) = line.strip().split(':')
            contactsDic[key] = value

    name = input("输入需要查询的姓名:")
    if len(name) == 0:
        print("输入的姓名为空,请重试!")

    elif name in contactsDic:
        print("{}的电话号码是{}".format(name, contactsDic[name]))
    else:
        print("查询的 {} 不在电话簿中".format(name))


if __name__ == '__main__':
    print(
        '''
            ***************欢迎使用phonebook电话簿工具******************
                                       1. 添加联系人
                                       2. 删除联系人
                                       3. 查找联系人
                                       4. 编辑联系人
                                       5. 显示所有联系人信息
                                       6. 清空所有联系人
                                       7. 帮助菜单
                                       8. 保存电话簿
                                       9. 退出系统
            ***************************************************************
        '''
    )
    choose_num = input("输入您需要选择的功能:")

    # print(choose_num)

    if choose_num == '1':
        add_contacts()
    elif choose_num == '2':
        pass
    elif choose_num == '3':
        find_number_by_name()
