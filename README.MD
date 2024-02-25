## Описание

см. подробное описание в ветке "description-task"

Выполненные условия:

**Основные задачи:**

- [x] Эндпойнт добавления сменных заданий
- [x] Эндпойнт получения сменного задания по ID
- [x] Эндпойнт изменения сменного задания по ID
- [x] Эндпойнт получения списка сменных заданий по фильтрам
- [x] Эндпойнт "аггрегации" продукции

**Задачи "со звездочкой":**

- [ ] Тесты
- [x] docker
- [ ] Базовый CI/CD

## Как сделать миграции

+ piccolo migrations new test_task --auto
  + warning: test_task может быть заменено на all
+ piccolo migrations forwards test_task
  + warning: test_task может быть заменено на all

Ссылка на документацию piccolo о миграциях: 
+ https://piccolo-orm.readthedocs.io/en/latest/piccolo/migrations/create.html

## Как запустить

#### 1) Запуск из docker контейнера

+ Клонировать репозиторий: git clone
+ Перейти в папку с проектом: cd test_task
+ Создать и запустить docker контейнер командами:
  + docker-compose build
  + docker-compose up
+ После этого приложение будет доступно на порте http://127.0.0.1:8090/docs

#### 2) Запуск в качестве python-script

+ Клонировать репозиторий: git clone
+ Создать виртуальное окружение: python3 -m venv venv
+ Активировать виртуальное окружение: source venv/bin/actibate
+ Установить зависимости: pip install -r requirements.txt
+ Запустить приложение: uvicorn main:app --reload
+ После этого приложение будет доступно на порте http://127.0.0.1:8090/docs


