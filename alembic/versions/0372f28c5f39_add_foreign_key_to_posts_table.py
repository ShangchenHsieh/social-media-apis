"""add foreign key to posts table

Revision ID: 0372f28c5f39
Revises: 5595a9e98ada
Create Date: 2022-10-16 20:35:20.570316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0372f28c5f39'
down_revision = '5595a9e98ada'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
        'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
