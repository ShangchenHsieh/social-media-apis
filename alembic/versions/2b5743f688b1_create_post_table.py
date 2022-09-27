"""create post table

Revision ID: 2b5743f688b1
Revises: 
Create Date: 2022-09-26 11:32:18.014674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b5743f688b1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table("posts", sa.Column("id", sa.Integer, nullable=False, primary_key=True),
                    sa.Column("title", sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
