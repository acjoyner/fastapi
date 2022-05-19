"""add content column to posts table

Revision ID: 8d1d91269867
Revises: 5e5abb223712
Create Date: 2022-05-17 10:17:09.333084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d1d91269867'
down_revision = '5e5abb223712'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
