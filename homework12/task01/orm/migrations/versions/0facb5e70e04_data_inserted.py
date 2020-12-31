"""data inserted

Revision ID: 0facb5e70e04
Revises: c6777012b80e
Create Date: 2020-12-31 16:11:58.431309

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from orm.models import Homework, Student, Teacher
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = "0facb5e70e04"
down_revision = "c6777012b80e"
branch_labels = None
depends_on = None


def upgrade():
    op.bulk_insert(
        Teacher.__table__,
        [
            {
                "first_name": "Ilya",
                "last_name": "Samartsev",
            }
        ],
    )
    op.bulk_insert(
        Student.__table__,
        [
            {
                "first_name": "Karina",
                "last_name": "Maikenova",
            }
        ],
    )
    op.bulk_insert(
        Homework.__table__,
        [
            {
                "text": "OOP homework",
                "date": datetime(2020, 12, 1),
                "deadline": 1,
                "author": 1,
                "is_done": True,
                "checked_by": 1,
            }
        ],
    )


def downgrade():
    conn = op.get_bind()
    conn.execute(text("DELETE FROM teachers WHERE first_name = 'Ilya'"))
    conn.execute(text("DELETE FROM students WHERE first_name = 'Karina'"))
    conn.execute(text("DELETE FROM homeworks WHERE text = 'OOP homework'"))
