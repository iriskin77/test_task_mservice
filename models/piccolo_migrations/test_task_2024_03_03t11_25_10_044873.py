from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Integer


ID = "2024-03-03T11:25:10:044873"
VERSION = "1.3.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="test_task", description=DESCRIPTION
    )

    manager.alter_column(
        table_class_name="Product",
        tablename="product",
        column_name="number_batch",
        db_column_name="number_batch",
        params={"null": False},
        old_params={"null": True},
        column_class=Integer,
        old_column_class=ForeignKey,
        schema=None,
    )

    return manager
