"""add phone number

Revision ID: 299529378fba
Revises: 82e11bc046e7
Create Date: 2022-10-15 18:52:52.072363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '299529378fba'
down_revision = '82e11bc046e7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    pass
