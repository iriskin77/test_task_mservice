#### Описание

Необходимо было разработать систему контроля заданий на выпуск продукции. 
Её функционал заключается в том, чтобы получать сменные задания (партии) и уникальные идентификаторы продукции в рамках этой партии, 
а так же проверять (по запросу из внешней системы), принадлежит ли данный идентификатор продукции данной партии.

Выполненные условия:

#### Основные задачи:

- [x] Эндпойнт добавления сменных заданий
- [x] Эндпойнт получения сменного задания по ID
- [x] Эндпойнт изменения сменного задания по ID
- [x] Эндпойнт получения списка сменных заданий по фильтрам
- [x] Эндпойнт "аггрегации" продукции
- [ ] Тесты
- [x] docker
- [ ] Базовый CI/CD

#### Схема БД

Рис. 1

![Рис. 1](https://github.com/iriskin77/test_task_mservice/blob/master/images/db_schema_test_task.png)

#### Схема приложения

![Рис. 2](https://github.com/iriskin77/test_task_mservice/blob/master/images/grpc_services.png)
