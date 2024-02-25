from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Integer
from piccolo.columns.column_types import Serial
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table


class Product(Table, tablename="product", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=True,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )
    number_batch = Integer(
        default=0,
        null=False,
        primary_key=False,
        unique=True,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name=None,
        secret=False,
    )


ID = "2024-02-26T00:26:57:370359"
VERSION = "1.3.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="test_task", description=DESCRIPTION
    )

    manager.alter_column(
        table_class_name="Task",
        tablename="task",
        column_name="number_batch",
        db_column_name="number_batch",
        params={
            "references": Product,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": "number_batch",
            "null": True,
            "unique": False,
        },
        old_params={
            "references": None,
            "on_delete": None,
            "on_update": None,
            "target_column": None,
            "null": False,
            "unique": True,
        },
        column_class=ForeignKey,
        old_column_class=Integer,
        schema=None,
    )

    manager.alter_column(
        table_class_name="Product",
        tablename="product",
        column_name="number_batch",
        db_column_name="number_batch",
        params={"default": 0, "null": False, "unique": True},
        old_params={"default": None, "null": True, "unique": False},
        column_class=Integer,
        old_column_class=ForeignKey,
        schema=None,
    )

    return manager
