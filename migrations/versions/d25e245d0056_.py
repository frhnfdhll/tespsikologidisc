"""empty message

Revision ID: d25e245d0056
Revises: f6157d34c45e
Create Date: 2021-12-23 01:17:12.295173

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd25e245d0056'
down_revision = 'f6157d34c45e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data_tipekepribadian', sa.Column('id_tipe', sa.BigInteger(), autoincrement=True, nullable=False))
    op.drop_column('data_tipekepribadian', 'id_hasil')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data_tipekepribadian', sa.Column('id_hasil', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False))
    op.drop_column('data_tipekepribadian', 'id_tipe')
    # ### end Alembic commands ###
