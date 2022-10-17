"""auto vote

Revision ID: d7b13035f4ff
Revises: 64cf35e698de
Create Date: 2022-10-16 20:35:54.980826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7b13035f4ff'
down_revision = '64cf35e698de'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('votes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'post_id')
                    )
    pass


def downgrade() -> None:
    op.drop_table('votes')
    pass
