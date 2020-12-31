"""data structures created

Revision ID: c6777012b80e
Revises: 826c3f2e32a4
Create Date: 2020-12-31 16:07:28.093362

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c6777012b80e"
down_revision = "826c3f2e32a4"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "students",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("first_name", sa.TEXT(), nullable=False),
        sa.Column("last_name", sa.TEXT(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "teachers",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("first_name", sa.TEXT(), nullable=False),
        sa.Column("last_name", sa.TEXT(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "homeworks",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("text", sa.TEXT(), nullable=False),
        sa.Column("date", sa.DATETIME(), nullable=False),
        sa.Column("deadline", sa.INTEGER(), nullable=False),
        sa.Column("author", sa.INTEGER(), nullable=True),
        sa.Column("is_done", sa.BOOLEAN(), nullable=False),
        sa.Column("checked_by", sa.INTEGER(), nullable=True),
        sa.CheckConstraint("is_done IN (0, 1)"),
        sa.ForeignKeyConstraint(
            ["author"],
            ["teachers.id"],
        ),
        sa.ForeignKeyConstraint(
            ["checked_by"],
            ["students.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("homeworks")
    op.drop_table("teachers")
    op.drop_table("students")
