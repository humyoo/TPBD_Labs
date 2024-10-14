"""Add new field to table

Revision ID: a8f77ee4ed35
Revises: 
Create Date: 2024-10-14 22:45:12.461244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'a8f77ee4ed35'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # Add the new column 'Description' to the 'Genres' table
    op.add_column('Genres', sa.Column('Description', sa.String(length=255), nullable=True))

    # Populate the new column with default values
    op.execute("UPDATE Genres SET Description = 'Default Description' WHERE Description IS NULL")

def downgrade():
    # Remove the 'Description' column on downgrade
    op.drop_column('Genres', 'Description')
