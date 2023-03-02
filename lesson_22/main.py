# import json
# writeF = open("file.json", "w", encoding="utf-8")
# # writeF.write("True")
# content = [None, True, (1, 2, 3), [1, 2, 3], "hello", "всем кискам пис✌"]
# json.dump(content, writeF, ensure_ascii=False) # в json и в файл
# writeF.close()

# import json
# readF = open("file.json", "r", encoding="utf-8")
# # print(readF.read())
# print(json.load(readF))
# readF.close()

# первый задачей
# import json
#
# readF = open("file.txt", "r", encoding="utf-8")
# content = readF.readlines()
# readF.close()
#
# print(content)
#
# d = {}
# for record in content:
#     splited = record.split(": ")
#     d[splited[0]] = splited[1].rstrip()
# print(d)
#
# f = open("file.json", "w", encoding="utf-8")
# json.dump(d, f, ensure_ascii=False)
# f.close()

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()["iss_position"]
print(f"широта:{data['latitude']}. долго, да:{data['longitude']}")
