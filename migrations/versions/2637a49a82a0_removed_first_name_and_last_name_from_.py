"""removed first_name and last_name from user

Revision ID: 2637a49a82a0
Revises: f1d50ec3cacb
Create Date: 2023-04-08 16:54:07.788843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2637a49a82a0'
down_revision = 'f1d50ec3cacb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=64), nullable=True))
        batch_op.drop_index('ix_user_login')
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)
        batch_op.drop_column('login')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.VARCHAR(length=64), nullable=True))
        batch_op.add_column(sa.Column('last_name', sa.VARCHAR(length=64), nullable=True))
        batch_op.add_column(sa.Column('login', sa.VARCHAR(length=64), nullable=True))
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.create_index('ix_user_login', ['login'], unique=False)
        batch_op.drop_column('username')

    # ### end Alembic commands ###
