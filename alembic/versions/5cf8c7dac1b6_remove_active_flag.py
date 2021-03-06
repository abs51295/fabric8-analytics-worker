"""remove active flag

Revision ID: 5cf8c7dac1b6
Revises: 33b719488061
Create Date: 2018-02-08 13:34:13.629328

"""

# revision identifiers, used by Alembic.
revision = '5cf8c7dac1b6'
down_revision = '33b719488061'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('monitored_upstreams', 'active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('monitored_upstreams', sa.Column('active', sa.BOOLEAN(),
                                                   autoincrement=False,
                                                   nullable=False))
    # ### end Alembic commands ###
