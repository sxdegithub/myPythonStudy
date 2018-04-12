# !/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: phonebook.py
# Author: qianghaohao(CodeNutter)
# Email: codenutter@foxmail.com

# ------------------------------------编码问题------------------------------------
# import sys
# import locale
# print sys.getdefaultencoding()    # 系统的缺省编码(一般就是ascii)
# print locale.getdefaultlocale()   # 系统当前的编码
# print locale.getlocale()          # 系统代码中临时被更改的编码
# print sys.getfilesystemencoding() # 文件系统编码
# print sys.stdin.encoding          # 终端输入编码
# print sys.stdout.encoding         # 终端输出编码
#                                   # 代码缺省编码 :文件头 # -*- conding: utf-8 -*-
# --------------------------------------------------------------------------------
#         在python中内部编码是unicode，因此当前编码要先转换成unicode，然后再由unicode
# 转换成你需要的编码. 转换通过encode和decode函数,unicode相当于中间编码.
#           decode                encode
#    str-------------->unicode-------------->str1
# ---------------------------------------------------------------------------------

import sys
import os
import pickle
import locale


# 联系人类--->最终联系人都是以此类的对象保存的,也就是对象序列化保存
class Contacts:
    def __init__(self, name, tel, sex, email, address, birth):
        self.name = name
        self.tel = tel
        self.sex = sex
        self.email = email
        self.address = address
        self.birth = birth

    def GetContactsInfo(self):
        print('姓名:%s' % (self.name).decode('utf-8'))  # 将utf-8转成Unicode输出，避免错误
        print('电话:%s' % (self.tel).decode('utf-8'))
        print('性别:%s' % (self.tel).decode('utf-8'))
        print('邮件:%s' % (self.email).decode('utf-8'))
        print('地址:%s' % (self.address).decode('utf-8'))
        print('出生日期:%s' % (self.birth).decode('utf-8'))

    def SetName(self, name):
        self.name = name

    def SetTel(self, tel):
        self.tel = tel

    def SetSex(self, sex):
        self.sex = sex

    def SetMail(self, mail):
        self.mail = mail

    def SetAddress(self, address):
        self.address = address

    def SetBirth(self, birth):
        self.birth = birth


# ----------------------------------------------------------------------------------------
#  封装自己的raw_input函数，避免重复的代码，为了保持很好的兼容性，先将提示串decode成unicode
#  然后再encode成和终端一样的编码，如果不这样做就会出现字符串的编码和终端编码不一致的状况，从而
#  导致乱码问题的出现。然后将raw_input函数的返回值再次decode成unicode，注意此时参数是stdin的
#  的编码，之所以这么做是因为stdin的编码不一定和python文本的编码一致，所以先转换成unicode，再
#  由unicode编码encode成utf-8编码，这样就保证了输入的字符串的编码和python源文件的编码一致了。
#  ---------->这样做好绕...没办法，2.7.x就这样，也许还有其他解决方案，我先这么写.要是linux下
#             就没这么麻烦了...
# -----------------------------------------------------------------------------------------
def MyRawInput(prompt):
    return input(prompt.decode('utf-8').encode(sys.stdout.encoding)).decode(sys.stdin.encoding).encode('utf-8')


def ShowMenu():
    print('''
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
    ''')


def EditMenu():
    print('''
          ----------------编辑选项-----------------
                        a. 编辑姓名
                        b. 编辑电话
                        c. 编辑性别
                        d. 编辑邮件
                        e. 编辑地址
                        f. 编辑出生日期
                        g. 调出菜单
                        h. 退出编辑
          -----------------------------------------
    ''')


def GetHelp():
    print('''
    GNU phonebook 1.0
               By  qianghaohao(CodeNutter)
    Usage: phonebook [OPTION]... [FILENAME]...

        --open       打开或新建电话簿
        --version    版本信息
        --help       使用帮助
    ''')


if (len(sys.argv) < 2):
    print('phonebook: missing OPTION')
    print('Usage: phonebook [OPTION]... [FILENAME]...')
    print()
    print("Try 'phonebook --help' for more options")
    sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print('phonebook: Version 1.0')
    elif option == 'help':
        GetHelp()
    elif option == 'open':
        if len(sys.argv) < 3:
            print('''
            phonebook: missing FILENAME
            Usage: phonebook [OPTION]... [FILENAME]...
            ''')
            sys.exit()
        filename = sys.argv[2]
        try:
            if os.path.exists(filename):  # 如果电话簿文件存在,则加载到phonebook字典
                f = file(filename)
                phonebook = pickle.load(f)
            else:  # 电话簿不存在则新建电话簿
                phonebook = {}
        except EOFError:  # 如果文件为空,则加载失败,抛出异常,在此捕获异常并新建空字典
            phonebook = {}
        ShowMenu()

        while True:
            choice = MyRawInput('请输入您的选择(1-9)输入7可以调出帮助菜单:')
            if choice == '1':
                name = MyRawInput('姓名:')
                tel = MyRawInput('电话:')
                sex = MyRawInput('性别:')
                mail = MyRawInput('邮件:')
                address = MyRawInput('地址:')
                birthday = MyRawInput('出生日期:')
                phonebook[name] = Contacts(name, tel, sex, mail, address, birthday)
            elif choice == '2':
                name_to_del = MyRawInput('请输入要删除人的姓名:')
                if name_to_del in phonebook:
                    del phonebook[name_to_del]
                    print('联系人: %s 删除成功!' % name_to_del.decode('utf-8'))
                else:
                    print('您要删的联系人:<%s> 不存在!' % name_to_del.decode('utf-8'))
            elif choice == '3':
                name_to_find = MyRawInput('请输入要查找人的姓名:')
                if name_to_find in phonebook:
                    phonebook[name_to_find].GetContactsInfo()
                else:
                    print('您要查找的联系人:<%s>不存在!' % name_to_find.decode('utf-8'))
            elif choice == '4':
                name_to_modify = MyRawInput('请输入要编辑人的姓名:')
                if name_to_modify in phonebook:
                    print('===========您要编辑的联系人信息如下===========:')
                    phonebook[name_to_modify].GetContactsInfo()
                    EditMenu()
                else:
                    print('您要编辑的联系人:<%s>不存在!' % name_to_modify.decode('utf-8'))
                    continue
                while True:
                    to_modify_potion = MyRawInput('请输入您要编辑的选项(a-h)输入g调出菜单:')
                    if to_modify_potion == 'a':
                        new_name = MyRawInput('请输入新名字:')
                        phonebook[name_to_modify].SetName(new_name)
                    elif to_modify_potion == 'b':
                        new_tel = MyRawInput('请输入新电话:')
                        phonebook[name_to_modify].SetTel(new_tel)
                    elif to_modify_potion == 'c':
                        new_sex = MyRawInput('请输入新性别:')
                        phonebook[name_to_modify].SetSex(new_sex)
                    elif to_modify_potion == 'd':
                        new_mail = MyRawInput('请输入新邮件:')
                        phonebook[name_to_modify].SetMail(new_mail)
                    elif to_modify_potion == 'e':
                        new_addres = MyRawInput('请输入新地址:')
                        phonebook[name_to_modify].SetAddress(new_addres)
                    elif to_modify_potion == 'f':
                        new_birthday = MyRawInput('请输入新出生日期:')
                        phonebook[name_to_modify].SetBirth(new_birthday)
                    elif to_modify_potion == 'g':
                        EditMenu()
                    elif to_modify_potion == 'h':
                        break
                    else:
                        print('输入错误,请重新输入(a-h)!')
            elif choice == '5':
                print('===============所有联系人==============')
                for name, contacts in list(phonebook.items()):
                    contacts.GetContactsInfo()
                    print('---------------------------------------')
            elif choice == '6':
                phonebook.clear()
            elif choice == '7':
                ShowMenu()
            elif choice == '8':
                f = file(filename, 'w')
                pickle.dump(phonebook, f)  # 存储电话簿到文件
                f.close()
                print('''\n电话簿已保存,注意您的电话簿路径为: %s''' % (os.path.abspath(filename)).decode('utf-8'))
            elif choice == '9':
                sys.exit()
            else:
                print('请输入正确的选择(1-9)!')
    else:
        print('Unknown option!')
        print("Try 'phonebook --help' for more options")
        sys.exit()
else:
    print('''
    The option must start with '--'
    Example: phonebook --open filename
    print "Try 'phonebook --help' for more information."
    ''')
    sys.exit()
