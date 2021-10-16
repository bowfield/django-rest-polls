### Типы
<br>

### Методы

`GET` `/polls` - Получить список активных опросов<br>
<b>Пример ответа:</b>
```json
{
    "polls": [
        {
            "id": 18,
            "text": "Как твои дела?",
            "type": "single",
            "start_date": "2021-10-01T19:39:06Z",
            "end_date": "2021-10-31T00:00:00Z",
            "answers": [
                {
                    "id": 35,
                    "poll": 18,
                    "text": "Хорошо",
                    "users": [ ]
                },
                {
                    "id": 36,
                    "poll": 18,
                    "text": "Плохо",
                    "users": [ ]
                },
                {
                    "id": 37,
                    "poll": 18,
                    "text": "А твои?",
                    "users": [ ]
                }
            ]
        },
        {
            "id": 20,
            "text": "Кто ты?",
            "type": "input",
            "start_date": "2021-10-01T00:00:00Z",
            "end_date": "2021-10-21T00:00:00Z",
            "answers": [
                {
                    "id": 41,
                    "poll": 20,
                    "text": "",
                    "users": [
                        {
                            "real_id": 0,
                            "answer": -1,
                            "value": "мальчик"
                        }
                    ]
                }
            ]
        },
        {
            "id": 22,
            "text": "Что ты хочешь?",
            "type": "multiple",
            "start_date": "2021-10-01T00:00:00Z",
            "end_date": "2021-10-26T00:00:00Z",
            "answers": [
                {
                    "id": 45,
                    "poll": 22,
                    "text": "Сено",
                    "users": []
                },
                {
                    "id": 46,
                    "poll": 22,
                    "text": "Стул",
                    "users": [
                        {
                            "real_id": 0,
                            "answer": 46,
                            "value": null
                        }
                    ]
                },
                {
                    "id": 47,
                    "poll": 22,
                    "text": "Кушать",
                    "users": []
                }
            ]
        }
    ]
}
```

<hr>

`GET` `/me?user_id=0` - Получить ответы в которых участвовал юзер<br>
<b>Пример ответа:</b>
```json
{
    "data": [
        {
            "id": 35,
            "poll": 18,
            "text": "Хорошо",
            "users": [
                {
                    "real_id": 0,
                    "answer": 35,
                    "value": null
                }
            ]
        }
    ]
}
```

<hr>

`POST` `/answer` - Отправить ответ (Тип: simple)<br>
<b>Пример запроса:</b>
```
{
    "answer_simple": {
        "user_id": 0,
        "answer_id" : 36
    }
}
```
<b>Пример ответа:</b>
```
{
    "success": "Answer id: 23 added"
}
```

<hr>

`POST` `/answer` - Отправить ответ (Тип: multiple)<br>
<b>Пример запроса:</b>
```
{
    "answer_multiple": {
        "user_id": 0,
        "answers" : [35, 36, 37]
    }
}
```
<b>Пример ответа:</b>
```
{
    "success": "Answer id: 23 added"
}
```
<hr>

`POST` `/answer` - Отправить ответ (Тип: input)<br>
<b>Пример запроса:</b>
```
{
    "answer_input": {
        "user_id": 0,
        "answer_id" : 68,
        "answer_input" : ""
    }
}
```
<b>Пример ответа:</b>
```
{
    "success": "Answer id: 23 added"
}
```
