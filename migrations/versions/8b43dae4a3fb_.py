"""empty message

Revision ID: 8b43dae4a3fb
Revises: 
Create Date: 2020-02-16 18:34:07.438425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b43dae4a3fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lessons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lesson_name', sa.String(length=50), nullable=False),
    sa.Column('lesson_image', sa.String(length=500), nullable=True),
    sa.Column('lesson_summary', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card_name', sa.String(length=50), nullable=False),
    sa.Column('card_image', sa.String(length=500), nullable=True),
    sa.Column('english_concept', sa.String(length=50), nullable=False),
    sa.Column('hindi_concept', sa.String(length=50), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lesson_id'], ['lessons.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cards')
    op.drop_table('lessons')
    # ### end Alembic commands ###
