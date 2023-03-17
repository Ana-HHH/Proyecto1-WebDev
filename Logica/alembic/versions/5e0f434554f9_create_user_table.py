"""create user table

Revision ID: 5e0f434554f9
Revises: 
Create Date: 2023-02-28 18:31:14.893642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e0f434554f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nick_name', sa.String(50), nullable=False),
        sa.Column('full_name', sa.Unicode(50))
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
