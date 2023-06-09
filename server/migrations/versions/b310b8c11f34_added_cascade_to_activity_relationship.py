"""added cascade to activity relationship

Revision ID: b310b8c11f34
Revises: 63c4d9eaa3ee
Create Date: 2023-04-11 08:22:05.542635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b310b8c11f34'
down_revision = '63c4d9eaa3ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campers', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campers', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
