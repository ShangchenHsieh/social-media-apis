"""add user table

Revision ID: 5595a9e98ada
Revises: 9cd5b65e9746
Create Date: 2022-10-16 20:35:05.640739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5595a9e98ada'
down_revision = '9cd5b65e9746'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
