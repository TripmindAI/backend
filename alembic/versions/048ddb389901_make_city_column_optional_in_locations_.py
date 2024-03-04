"""Make city column optional in locations table

Revision ID: 048ddb389901
Revises: 2bbe898a1026
Create Date: 2024-03-03 23:16:25.148329

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '048ddb389901'
down_revision: Union[str, None] = '2bbe898a1026'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('locations', 'city',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('locations', 'city',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
