from piccolo.columns import Boolean, Varchar, Integer, Date, Text, ForeignKey, Serial, Timestamp, OnDelete, OnUpdate
from piccolo.table import Table


class Test(Table):

    id = Serial(primary_key=True, unique=True)
    test_name = Varchar()
    test_surname = Varchar()


class Task(Table):

    id = Serial(primary_key=True, unique=True)
    is_closed = Boolean(default=False) # "СтатусЗакрытия": false,
    closed_at = Timestamp(nullable=True, default=None) # время закрытия
    task = Varchar() # "ПредставлениеЗаданияНаСмену": "Задание на смену 2345",
    line = Varchar() # "Линия": "Т2",
    shift = Varchar() # "Смена": "1",
    group = Varchar() # "Бригада": "Бригада №4",
    number_batch = Integer(unique=True)
    #number_batch = ForeignKey(references=Product, target_column=Product.number_batch) # "НомерПартии": 22222,
    date_batch = Timestamp(unique=True) # "ДатаПартии": "2024-01-30",
    nomenclature = Text() # "Номенклатура": "Какая то номенклатура",
    code = Varchar() # "КодЕКН": "456678",
    index = Varchar() # "ИдентификаторРЦ": "A",
    date_begin = Timestamp() # "ДатаВремяНачалаСмены": "2024-01-30T20:00:00+05:00",
    date_end = Timestamp() # "ДатаВремяОкончанияСмены": "2024-01-31T08:00:00+05:00"


class Product(Table):

    id = Serial(primary_key=True, unique=True)
    unique_code = Varchar(unique=True) # "УникальныйКодПродукта": "12gRV60MMsn1"
    #number_batch = Integer(unique=True)  #"НомерПартии": 22222,
    #number_batch = ForeignKey(references=Task, target_column=Task.number_batch, null=True)
    number_batch = Integer()
    is_aggregated = Boolean(null=True)
    aggregated_at = Timestamp(null=True)
    date_product = Date() #"ДатаПартии": "2024-01-30"
