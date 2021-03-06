"""empty message

Revision ID: f5249e3d35fc
Revises: 
Create Date: 2017-03-26 21:10:17.819000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5249e3d35fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('visitors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=True),
    sa.Column('lastname', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('visits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('visitor_id', sa.Integer(), nullable=True),
    sa.Column('visiting', sa.String(length=100), nullable=True),
    sa.Column('purpose', sa.Text(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['visitor_id'], ['visitors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visits')
    op.drop_table('visitors')
    op.drop_table('user_profiles')
    # ### end Alembic commands ###
