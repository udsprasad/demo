"""user db create

Revision ID: 301c8401e557
Revises: efeb9a9c56ae
Create Date: 2020-06-16 22:20:37.926504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '301c8401e557'
down_revision = 'efeb9a9c56ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.drop_column('user', 'pssowrd_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('pssowrd_hash', sa.VARCHAR(length=128), nullable=True))
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###
