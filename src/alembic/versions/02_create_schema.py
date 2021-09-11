"""Create schema

Revision ID: d3757747793b
Revises: 9359efd7412e
Create Date: 2021-08-23 21:45:42.028921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3757747793b'
down_revision = '9359efd7412e'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE SCHEMA sdamteam;
        
        ALTER ROLE sdamteam_user
        IN DATABASE sdamteam
        SET search_path
        TO sdamteam;
    """)


def downgrade():
    op.execute("""
        DROP SCHEMA sdamteam CASCADE;
        
        ALTER ROLE sdamteam_user
        IN DATABASE sdamteam
        RESET serach_path;
    """)
