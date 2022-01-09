# How to run the project 

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

### _Документация API_ (создал автодокументирование API на swagger доступно по адресу http://127.0.0.1:8000/swagger/ )
### Чтобы получить токен пользователя: 
* Request method: GET
* URL: http://localhost:8000/api/login/
* Body: 
    * username: 
    * password: 
* Example:
```
curl --location --request GET 'http://localhost:8000/api/login/' \
--form 'username=%username' \
--form 'password=%password'
```

### Чтобы создать опрос:
* Request method: POST
* URL: http://localhost:8000/api/surveysApp/create/
* Header:
   *  Authorization: Token userToken
* Body:
    * survey_name: name of survey
    * start_date: publication date can be set only when survey is created, format: YYYY-MM-DD HH:MM:SS
    * end_date: survey end date, format: YYYY-MM-DD HH:MM:SS
    * survey_description: description of survey
* Example: 
```
curl --location --request POST 'http://localhost:8000/api/surveysApp/create/' \
--header 'Authorization: Token %userToken' \
--form 'survey_name=%survey_name' \
--form 'start_date=%start_date' \
--form 'end_date=%end_date \
--form 'survey_description=%survey_description'
```

### Обновить опрос:
* Request method: PATCH
* URL: http://localhost:8000/api/surveysApp/update/[survey_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * survey_id 
* Body:
    * survey_name: name of survey
    * end_date: survey end date, format: YYYY-MM-DD HH:MM:SS
    * survey_description: description of survey
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/surveysApp/update/[survey_id]/' \
--header 'Authorization: Token %userToken' \
--form 'survey_name=%survey_name' \
--form 'end_date=%end_date \
--form 'survey_description=%survey_description'
```

### Удалить опрос:
* Request method: DELETE
* URL: http://localhost:8000/api/surveysApp/update/[survey_id]
* Header:
    * Authorization: Token userToken
* Param:
    * survey_id
Example:
```
curl --location --request DELETE 'http://localhost:8000/api/surveysApp/update/[survey_id]/' \
--header 'Authorization: Token %userToken'
```

### Посмотреть все опросы:
* Request method: GET
* URL: http://localhost:8000/api/surveysApp/view/
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/surveysApp/view/' \
--header 'Authorization: Token %userToken'
```

### Просмотр текущих активных опросов:
* Request method: GET
* URL: http://localhost:8000/api/surveysApp/view/active/
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/surveysApp/view/active/' \
--header 'Authorization: Token %userToken'
```

### Создаем вопрос:
* Request method: POST
* URL: http://localhost:8000/api/question/create/
* Header:
    * Authorization: Token userToken
* Body:
    * survey: id of survey 
    * question_text: 
    * question_type: can be only `one`, `multiple` or `text`
* Example:
```
curl --location --request POST 'http://localhost:8000/api/question/create/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Обновляем вопрос:
* Request method: PATCH
* URL: http://localhost:8000/api/question/update/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Body:
    * survey: id of survey 
    * question_text: question
    * question_type: can be only `one`, `multiple` or `text`
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Удаляем вопрос:
* Request method: DELETE
* URL: http://localhost:8000/api/question/update/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Создаем выбор:
* Request method: POST
* URL: http://localhost:8000/api/choice/create/
* Header:
    * Authorization: Token userToken
* Body:
    * question: id of question
    * choice_text: choice
* Example:
```
curl --location --request POST 'http://localhost:8000/api/choice/create/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Обновляем выбор:
* Request method: PATCH
* URL: http://localhost:8000/api/choice/update/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Body:
    * question: id of question
    * choice_text: choice
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Обновляем выбор:
* Request method: DELETE
* URL: http://localhost:8000/api/choice/update/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Создаем ответ:
* Request method: POST
* URL: http://localhost:8000/api/answer/create/
* Header:
    * Authorization: Token userToken
* Body:
    * survey: id of survey
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:
```
curl --location --request POST 'http://localhost:8000/api/answer/create/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### Обновляем ответ:
* Request method: PATCH
* URL: http://localhost:8000/api/answer/update/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Body:
    * survey: id of survey
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### Удаляем ответ:
* Request method: DELETE
* URL: http://localhost:8000/api/answer/update/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken'
```

### Просматриваем ответы пользователя:
* Request method: GET
* URL: http://localhost:8000/api/answer/view/[user_id]/
* Param:
    * user_id
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/answer/view/[user_id]' \
--header 'Authorization: Token %userToken'
