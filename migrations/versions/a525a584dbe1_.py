"""empty message

Revision ID: a525a584dbe1
Revises: 2fe973728b7a
Create Date: 2021-12-11 23:24:05.285129

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a525a584dbe1'
down_revision = '2fe973728b7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hasiltes',
    sa.Column('id_hasiltes', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('most_d', sa.String(length=10), nullable=False),
    sa.Column('most_i', sa.String(length=10), nullable=False),
    sa.Column('most_s', sa.String(length=10), nullable=False),
    sa.Column('most_c', sa.String(length=10), nullable=False),
    sa.Column('least_d', sa.String(length=10), nullable=False),
    sa.Column('least_i', sa.String(length=10), nullable=False),
    sa.Column('least_s', sa.String(length=10), nullable=False),
    sa.Column('least_c', sa.String(length=10), nullable=False),
    sa.Column('change_d', sa.String(length=10), nullable=False),
    sa.Column('change_i', sa.String(length=10), nullable=False),
    sa.Column('change_s', sa.String(length=10), nullable=False),
    sa.Column('change_c', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id_hasiltes')
    )
    op.drop_table('hasiltes_jadi')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hasiltes_jadi',
    sa.Column('id_hasiltes', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('most_d', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('most_i', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('most_s', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('most_c', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('least_d', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('least_i', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('least_s', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('least_c', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('change_d', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('change_i', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('change_s', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('change_c', mysql.VARCHAR(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id_hasiltes'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('hasiltes')
    # ### end Alembic commands ###
