"""empty message

Revision ID: df5714f3129d
Revises: cb18fc926c3c
Create Date: 2017-11-26 20:00:17.463124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df5714f3129d'
down_revision = 'cb18fc926c3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tunes_data', sa.Column('iframe_string', sa.String(length=256), nullable=True))
    op.create_index(op.f('ix_tunes_data_iframe_string'), 'tunes_data', ['iframe_string'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tunes_data_iframe_string'), table_name='tunes_data')
    op.drop_column('tunes_data', 'iframe_string')
    # ### end Alembic commands ###