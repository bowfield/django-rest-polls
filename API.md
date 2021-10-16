### Типы
<br>

### Методы

`GET` `/polls` - Получить список активных опросов<br>
<b>Пример ответа:</b>
```json
{
	"polls": [
		{
			"id": 8,
			"text": "Кто?",
			"type": "multiple", 
			"start_date": "2021-10-01T00:00:00Z", 
			"end_date": "2021-10-13T00:00:00Z", 
			"answers": [
				{
					"text": "\u042f", 
					"votes": 0
				}
			]
		}
	]
}
```

`GET` `/get_me?user_id=1` - Получить ответы в которых участвовал юзер<br>
<b>Пример ответа:</b>
```json
{
	"polls": [
			{
				"poll_id": 7,
				"answer_id": 0
			}
		]
}
```

`GET` `/send_answer?user_id=1&poll_id=13&answer_id=0` - Отправить ответ (Тип: simple)<br>
<b>Пример ответа:</b>
```
{
	
}
```
		
`GET` `/send_answer?user_id=1&poll_id=13&answer1=0&answer2=0&answer3=1` - Отправить ответ (Тип: multiple)<br>
<b>Пример ответа:</b>
```
{
	
}
```
		
`GET` `/send_answer?user_id=1&poll_id=13&answer_text=Да` - Отправить ответ (Тип: input)<br>
<b>Пример ответа:</b>
```
{
	
}
```
