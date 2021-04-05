"""first

Revision ID: 960bf41e87d4
Revises: 
Create Date: 2021-04-05 19:08:34.642630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '960bf41e87d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('face', sa.String(length=150), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('message', sa.String(length=100), nullable=False),
    sa.Column('checked', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eventss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('file', sa.String(length=1000), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grantss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('pers_name', sa.String(length=300), nullable=False),
    sa.Column('what', sa.String(length=1000), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('file', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('file', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('partnerss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('file', sa.String(length=1000), nullable=False),
    sa.Column('pub_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('peoples',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.String(length=500), nullable=False),
    sa.Column('file', sa.String(length=1000), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projectss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('file', sa.String(length=1000), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.CHAR(36), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=14), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('weathers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=False),
    sa.Column('icon', sa.String(length=150), nullable=False),
    sa.Column('pub_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('newss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=170), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('file', sa.String(length=1000), nullable=False),
    sa.Column('pub_date', sa.DateTime(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['categorys.id'], name='fk_newss_categorys_id_category'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('newss')
    op.drop_table('weathers')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('projectss')
    op.drop_table('peoples')
    op.drop_table('partnerss')
    op.drop_table('organizations')
    op.drop_table('historys')
    op.drop_table('grantss')
    op.drop_table('eventss')
    op.drop_table('contacts')
    op.drop_table('categorys')
    # ### end Alembic commands ###