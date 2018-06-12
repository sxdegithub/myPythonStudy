# [Python3网络爬虫开发实战] 5.1.2-JSON文件存储

# 2. 读取json
#
# import json
#
# str = '''
# [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-10-18"
# }, {
#     "name": "Selina",
#     "gender": "female",
#     "birthday": "1995-10-18"
# }]
# '''
#
# data = json.loads(str)
# print(data)
# print(type(data))
#
# print(data[0]['name'])
# # 通过get()方法
# print(data[0].get('name'))
# # 如果获取的属性不存在,那么返回后面的默认值
# print(data[0].get('age', 25))

# ***************************************
# 值得注意的是，JSON的数据需要用双引号来包围，不能使用单引号。例如，若使用如下形式表示，则会出现错误：
# ***************************************

# 下面的这个会报错


# ***************************************
# str1 = '''
# [{
#     'name': 'Bob',
#     'gender': 'male',
#     'birthday': '1992-10-18'
# }]
# '''
#
# data1 = json.loads(str1)
# ***************************************

# 3.输出json

import json

data = [{
    'name': 'Bob',
    'gender': '男',
    'birthday': '1992-10-18'
}]

with open('.\\data.json', 'w',encoding='utf-8') as file:
    file.write(json.dumps(data))

with open('.\\data1.json', 'w',encoding='utf-8') as file1:
    json.dump(data, file1,ensure_ascii=False)

# json.dump()
