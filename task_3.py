import sys
import json


result_dict = dict()

with open('users.csv', 'r', encoding='utf-8') as f1, \
    open('hobby.csv', 'r', encoding='utf-8') as f2:
    for line_1 in f1:
        line_2 = f2.readline().strip()
        if not line_2:
            line_1 = None
        if line_1 not in result_dict:
            result_dict[line_1.strip()] = line_2
    content = f2.read()
    if content:
        sys.exit(1)

with open('result.json', 'w', encoding='utf-8') as result_file:
    dict_as_string = json.dumps(result_dict, ensure_ascii=False)
    result_file.write(dict_as_string)
with open('result.json', 'r', encoding='utf-8') as f:
    content = f.read()
    result = json.loads(content)
print(result)