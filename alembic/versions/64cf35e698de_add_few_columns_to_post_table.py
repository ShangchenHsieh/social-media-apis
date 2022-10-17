"""add few columns to post table

Revision ID: 64cf35e698de
Revises: 0372f28c5f39
Create Date: 2022-10-16 20:35:44.167905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64cf35e698de'
down_revision = '0372f28c5f39'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'), )
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')), )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
