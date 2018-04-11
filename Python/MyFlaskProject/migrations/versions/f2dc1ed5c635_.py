"""empty message

Revision ID: f2dc1ed5c635
Revises: 8e462ff0f71f
Create Date: 2017-11-07 20:06:27.933613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2dc1ed5c635'
down_revision = '8e462ff0f71f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gift',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.Column('obtain', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('score', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'score')
    op.drop_table('gift')
    # ### end Alembic commands ###
