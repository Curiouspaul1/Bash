"""empty message

Revision ID: 8119510851f6
Revises: 
Create Date: 2019-12-18 12:13:20.095426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8119510851f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Parent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pname', sa.String(length=100), nullable=True),
    sa.Column('raddress', sa.String(length=100), nullable=True),
    sa.Column('oaddress', sa.String(length=100), nullable=True),
    sa.Column('tel', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('family', sa.String(length=100), nullable=True),
    sa.Column('siblings', sa.String(length=50), nullable=True),
    sa.Column('etel', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Siblings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('s_name', sa.String(length=100), nullable=True),
    sa.Column('s_class_', sa.String(length=100), nullable=True),
    sa.Column('s_year', sa.String(length=100), nullable=True),
    sa.Column('parentid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parentid'], ['Parent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sname', sa.String(length=100), nullable=True),
    sa.Column('dob', sa.String(length=100), nullable=True),
    sa.Column('bg', sa.String(length=100), nullable=True),
    sa.Column('bp', sa.String(length=100), nullable=True),
    sa.Column('state', sa.String(length=50), nullable=True),
    sa.Column('gen', sa.String(length=50), nullable=True),
    sa.Column('lga', sa.String(length=50), nullable=True),
    sa.Column('sex', sa.String(length=10), nullable=True),
    sa.Column('ail', sa.String(length=10), nullable=True),
    sa.Column('school', sa.Text(length=200), nullable=True),
    sa.Column('school_address', sa.String(length=200), nullable=True),
    sa.Column('class_', sa.String(length=100), nullable=True),
    sa.Column('year', sa.String(length=100), nullable=True),
    sa.Column('parentid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parentid'], ['Parent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Subscriber',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('parentid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parentid'], ['Parent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Subscriber')
    op.drop_table('Student')
    op.drop_table('Siblings')
    op.drop_table('Parent')
    # ### end Alembic commands ###
