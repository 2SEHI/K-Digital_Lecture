# json파일 읽는 법

json.loads로 하면 안되므로 한줄씩 읽어야 합니다.



```
import json

news = []
#줄단위로 읽기
file = open('news.json', 'r')

#읽어온 파일의 내용을 dict 의 list 로 만들기
li = []
for line in file:
    x = eval(line)
    li.append(x)

print(li)
```

```
import yaml
y = {'key': 'value'}
with open('y.yaml', 'w') as f:
    yaml.dump(y, f)
```

