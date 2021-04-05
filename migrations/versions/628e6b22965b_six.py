"""six

Revision ID: 628e6b22965b
Revises: 4178a9799b8c
Create Date: 2021-04-05 19:42:01.874207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '628e6b22965b'
down_revision = '4178a9799b8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('newss', 'title',
               existing_type=sa.VARCHAR(length=170),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('newss', 'title',
               existing_type=sa.VARCHAR(length=170),
               nullable=False)
    # ### end Alembic commands ###