"""Add Guest model

Revision ID: 68ea2b871984
Revises: 6074b7b55dc8
Create Date: 2025-06-22 19:58:00.610785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68ea2b871984'
down_revision = '6074b7b55dc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guests', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profession', sa.String(length=100), nullable=False))
        batch_op.drop_column('occupation')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guests', schema=None) as batch_op:
        batch_op.add_column(sa.Column('occupation', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.drop_column('profession')

    # ### end Alembic commands ###
