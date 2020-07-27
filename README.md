# Тестовое задание
## Небольшое веб-приложение на основе MongoDB, FastAPI, pydantic и motor
### Установка
- Установите [docker](https://docs.docker.com/engine/install/)
- Установите [docker-compose](https://docs.docker.com/compose/install/)
- `pip install 'fabric<2.0'`
- `docker-compose build`
- `fab dev` 
- Подождите пока контейнеры поднимутся
- `fab load` - загрузка сотрудников
* Главный эндпоинт: `http://0.0.0.0/api/`
* Метод эндпоинта `GET`
* Эндпоинт может принимать следующие аргументы в для фильтрации query params:
  * `age,name, job_title, company, salary, gender, join_date , email`
  * Из них: age, salary, join_date можно комбинировать с постфиксами _gt, _lt, пример такого запроса: `http://0.0.0.0:8000/api/?age_gt=22&age_lt=33&join_date_lt=2003-12-28T18%3A18%3A10-08%3A00&join_date_gt=2005-10-10T18%3A18%3A10-08%3A00`
* Эндпоинт может принимать следующие аргументы для пагинации в query params:
  * `page, page_size` 
  * `10 <= page_size <= 30`
* Эндпоинт принимает следующие аргументы в query params для сортировки результатов:
  * `sort_by`
  * Пример: `http://0.0.0.0:8000/api/?age_gt=22&age_lt=33&sort_by=name`
  
