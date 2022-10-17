"""add content column to posts table

Revision ID: 9cd5b65e9746
Revises: 3e4fa8792526
Create Date: 2022-10-16 20:33:02.984040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cd5b65e9746'
down_revision = '3e4fa8792526'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
