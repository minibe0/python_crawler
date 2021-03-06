## JSON
* javascript object notation(JSON)
* 자바스크립트 오브젝트 표현법
* tree구조
* key, value

제이선 JSON(Javasript Object Notation)이란 자바스크립트에서 데이터 객체를 표현하는 방법을 말합니다. 제이선, 제이썬, 제이슨 등으로 읽습니다.

자바스크립트에서 사용하는 데이터를 표현 할 때 사용하는 방법이었는데 이게 생각보다 간결하고 길이도 다른 것에 비해서(xml 등) 짧습니다. 다른 표현 방법에 비해 비교적 사람이 알아보기 쉬워서 자바스크립트 말고 다른 곳에서도 많이 쓰게 되었습니다. 물론 비교적 쉽다는 것이지 처음부터 쉽다는 것은 아닙니다.

```python
json_obj = {"name":"kyeongrok"}

print(json_obj)
```

```python
json_obj = {"name":"kyeongrok", "age":"32"}

print(json_obj)
```

```python
json_obj = {"name":"kyeongrok",
            "age":"32",
            "where":"역삼동",
            "phone_number":"010-3588-6265"
            }

print(json_obj)
```

```python
json_obj = {"name":"kyeongrok",
            "age":"32",
            "where":"역삼동",
            "phone_number":"010-3588-6265",
            "friends":[{"name":"doyeon", "age":"32"}]
            }

print(json_obj['friends'])
```

```python
json_obj = {"name":"kyeongrok",
            "age":"32",
            "where":"역삼동",
            "phone_number":"010-3588-6265",
            "friends":[
                {"name":"doyeon", "age":"32"},
                {"name":"kuri", "age":"24"}
            ]
            }

friends = json_obj['friends']
for friend in friends:
    print(friend['name'])
```


## json 편하게 보는 site
* json tree
* http://jsonviewer.stack.hu/

## 실습
1. http request하기
2. url 알아내서 a tag출력하기
3. 아래 data json으로 바꾸기
```
    이름	가격	위치
    cozy 모임공간	2500	강남역 3번출구
    스터디 플래닛	3000	역삼역과 강남역 근처
    에이지 스토리	2000	서울대입구역
    스타벅스	5000	많음
```

## JSON예제

```json
{"list":[
        {"name":"kyeongrok", "age":"32"},
        {"name":"bomi", "age":"25"},
        {"name":"cl", "age":"27"}
      ]
}
```
보통은 이렇게 생겼습니다.

JSON에서 맨 뒤에 N은 노테이션(Notation)입니다. 한글로 번역하면 '표기법'입니다. 어떤 것을 표현하는 방법입니다. 뒤에서 두번째 O는 오브젝트(Object)로써 말 그대로 '어떤 것'인데 쉽게 말해서 '데이터'라고 생각하시면 됩니다.

그러면 제이선(json)으로 사람을 한번 표현 해보도록 하겠습니다.

```json
{"name":"kyeongrok"}
```
{중괄호로 시작해서 }중괄호로 끝나고
키key("name"), 벨류value("kyeongrok")로 되어 있는 것

json으로 한명의 사람을 가장 간단하게 표현해 보았습니다.

### JSON에 여러가지 값 넣기
```json
{"name":"kyeongrok", "age":"32"}
```

{}안에는 name(이름)과 age(나이) 두가지가 들어갔습니다. 구분을 할 때는 ,컴마로 구분을 합니다.

{}는 한개(one)라는 의미에서 1과 같습니다.

```json
[{"name":"kyeongrok", "age":"32"}]
```
이것은 리스트 안에 1명의 사람(item)이 들어가 있는 형태 입니다.

```json
[1]
```
위와 구조가 같습니다. 1이라는 숫자(item)이 한개가 들어있는 형태 입니다.

### json여러가지 표현 방법
```json
[{"name":"kyeongrok", "age":32}]
```

```json
[1]
```

```json
{}
```

```json
1
```

[1, 2]는 []안에 몇개의 item(항목)이 들어 있을까요? 2개
[{}, {}]는 []안에 몇개의 item(항목)이 들어 있을까요? 2개

```json
[
    1, 2
]
```
[]안에 몇개의 item(항목)이 들어 있을까요? 2개

```json
[
    {}, {}
]
```
[]안에 몇개의 item(항목)이 들어 있을까요? 2개

```json
[
    {},
    {}
]
```
[]안에 몇개의 item(항목)이 들어 있을까요? 2개

```json
[{"name":"kyeongrok", "age":32}]
```
[]안에 몇개의 item(항목)이 들어 있을까요? 1개
{}안에 몇개의 item(항목)이 들어 있을까요? 2개

```json
[
    {"name":"kyeongrok", "age":32}
]
```
[]안에 몇개의 item(항목)이 들어 있을까요? 1개

```json
[
    {"name":"kyeongrok", "age":32},
    {"name":"anna", "age":34}
]
```
[]안에 몇개의 item(항목)이 들어 있을까요? 2개


### 표 형태의 데이터를 json으로 표현하기
| name        | age       | math  |
| ----------- |:--------:| -----:|
| kyeongrok   | 32      | 90 |
| bomi        | 25      | 85 |

항목이 3개가 들어 있는 3행 2열의 표 입니다.

```json
[
  {"name":"kyeongrok", "age":"32", "math":"90"},
  {"name":"bomi", "age":"25", "math":"85"}
]
```
json으로 표현하면 이렇게 표현 할 수 있습니다.

