"""second

Revision ID: b53336444d02
Revises: 960bf41e87d4
Create Date: 2021-04-05 19:27:46.543966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b53336444d02'
down_revision = '960bf41e87d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('newss', 'title')
    op.drop_column('newss', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('newss', sa.Column('description', sa.VARCHAR(length=500), autoincrement=False, nullable=False))
    op.add_column('newss', sa.Column('title', sa.VARCHAR(length=170), autoincrement=False, nullable=False))
    # ### end Alembic commands ###