"""empty message

Revision ID: fd4288ed00b7
Revises: 77b0de627528
Create Date: 2022-01-13 10:29:49.032350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd4288ed00b7'
down_revision = '77b0de627528'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hasiltes',
    sa.Column('id_hasil', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('most_D', sa.Integer(), nullable=False),
    sa.Column('most_I', sa.Integer(), nullable=False),
    sa.Column('most_S', sa.Integer(), nullable=False),
    sa.Column('most_C', sa.Integer(), nullable=False),
    sa.Column('least_D', sa.Integer(), nullable=False),
    sa.Column('least_I', sa.Integer(), nullable=False),
    sa.Column('least_S', sa.Integer(), nullable=False),
    sa.Column('least_C', sa.Integer(), nullable=False),
    sa.Column('change_D', sa.Integer(), nullable=False),
    sa.Column('change_I', sa.Integer(), nullable=False),
    sa.Column('change_S', sa.Integer(), nullable=False),
    sa.Column('change_C', sa.Integer(), nullable=False),
    sa.Column('hasil_tipekepribadian', sa.String(length=100), nullable=False),
    sa.Column('rekomendasi_pekerjaan', sa.Text(), nullable=False),
    sa.Column('date_submit', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id_hasil')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hasiltes')
    # ### end Alembic commands ###