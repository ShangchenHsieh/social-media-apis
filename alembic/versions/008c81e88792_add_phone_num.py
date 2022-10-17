"""add phone num

Revision ID: 008c81e88792
Revises: d7b13035f4ff
Create Date: 2022-10-16 20:36:19.135362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '008c81e88792'
down_revision = 'd7b13035f4ff'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    pass
