"""create different tables

Revision ID: 9454c68e092e
Revises: 506f1e4d4932
Create Date: 2022-10-15 13:31:53.160974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9454c68e092e'
down_revision = '506f1e4d4932'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    op.create_table('votes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'post_id')
                    )
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'), )
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')), )
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
        'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                                       primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    pass
