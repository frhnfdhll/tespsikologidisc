"""empty message

Revision ID: b5c5bb4638fe
Revises: 468ffd8bef3a
Create Date: 2022-01-09 19:42:14.735570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5c5bb4638fe'
down_revision = '468ffd8bef3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dataset',
    sa.Column('id_dataset', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('dominance', sa.Integer(), nullable=True),
    sa.Column('influance', sa.Integer(), nullable=True),
    sa.Column('steadiness', sa.Integer(), nullable=True),
    sa.Column('compliance', sa.Integer(), nullable=True),
    sa.Column('tipe_kepribadian', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id_dataset')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dataset')
    # ### end Alembic commands ###
