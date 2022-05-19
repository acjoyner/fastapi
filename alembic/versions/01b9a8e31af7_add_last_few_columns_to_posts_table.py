"""add last few columns to posts table.

Revision ID: 01b9a8e31af7
Revises: 19c08eb5bfbc
Create Date: 2022-05-17 13:31:46.737028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01b9a8e31af7'
down_revision = '19c08eb5bfbc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published',sa.Boolean(),nullable=False, server_default='TRUE'),)
    op.add_column('posts',sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
