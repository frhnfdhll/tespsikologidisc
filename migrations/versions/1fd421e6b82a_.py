"""empty message

Revision ID: 1fd421e6b82a
Revises: 875caa447c7b
Create Date: 2022-01-09 13:25:58.075214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fd421e6b82a'
down_revision = '875caa447c7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data_tipekepribadian', sa.Column('ciri_umum', sa.String(length=1000), nullable=False))
    op.add_column('data_tipekepribadian', sa.Column('nilai_dalam_team', sa.String(length=1000), nullable=False))
    op.add_column('data_tipekepribadian', sa.Column('kemungkinan_kelemahan', sa.String(length=1000), nullable=False))
    op.add_column('data_tipekepribadian', sa.Column('ketakutan_terbesar', sa.String(length=1000), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('data_tipekepribadian', 'ketakutan_terbesar')
    op.drop_column('data_tipekepribadian', 'kemungkinan_kelemahan')
    op.drop_column('data_tipekepribadian', 'nilai_dalam_team')
    op.drop_column('data_tipekepribadian', 'ciri_umum')
    # ### end Alembic commands ###
