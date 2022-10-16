"""add content table to post table

Revision ID: 8ed86184f05f
Revises: 5d9abfc7cdfb
Create Date: 2022-10-15 18:58:33.362981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ed86184f05f'
down_revision = '5d9abfc7cdfb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
