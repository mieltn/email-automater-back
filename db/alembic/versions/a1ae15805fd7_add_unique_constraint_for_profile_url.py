"""add unique constraint for profile_url

Revision ID: a1ae15805fd7
Revises: 8a54969f0952
Create Date: 2023-11-16 22:30:53.834362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1ae15805fd7'
down_revision = '8a54969f0952'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'linkedin_prospects', ['profile_url'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'linkedin_prospects', type_='unique')
    # ### end Alembic commands ###
