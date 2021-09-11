"""Create vk tables

Revision ID: 8f3df9b77865
Revises: d3757747793b
Create Date: 2021-08-23 21:48:53.814303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f3df9b77865'
down_revision = 'd3757747793b'
branch_labels = None
depends_on = None


def upgrade():
    op.execut("""
        CREATE TABLE sdamteam.users
        (
            user_id bigserial PRIMARY KEY,
            user_vk_id bigint NOT NULL,
            current_flow integer DEFAULT NULL,
            last_state_index integer DEFAULT 0,
            FOREIGN KEY (current_flow) REFERENCES sdamteam.flows (flow_id) ON DELETE SET NULL
        )
        WITH (OIDS = FALSE)
        TABLESPACE pg_default;
        
        CREATE TABLE sdamteam.states
        (
            state_id bigserial PRIMARY KEY,
            state_text varchar NOT NULL
        )
        WITH (OIDS = FALSE)
        TABLESPACE pg_default;
        
        CREATE TABLE sdamteam.flows
        (
            flow_id bigserial PRIMARY KEY,
            flow_text varchar NOT NULL,
            states integer[] NOT NULL
        )
        WITH (OIDS = FALSE)
        TABLESPACE pg_default;
        
        ALTER TABLE sdamteam.users
            OWNER TO sdamteam_user;
        ALTER TABLE sdamteam.states
            OWNER TO sdamteam_user;
        ALTER TABLE sdamteam.flows
            OWNER TO sdamteam_user;
    """)


def downgrade():
    pass
