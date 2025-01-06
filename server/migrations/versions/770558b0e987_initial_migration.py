"""initial migration

Revision ID: 770558b0e987
Revises: 
Create Date: 2025-01-06 12:27:18.916695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '770558b0e987'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('earthquakes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('magnitude', sa.Float(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('earthquakes')
    # ### end Alembic commands ###
