"""setting up database

Revision ID: f666c83a4471
Revises: 
Create Date: 2023-08-09 15:25:31.853924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f666c83a4471'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scenes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scene_num', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('choice_A', sa.String(), nullable=True),
    sa.Column('choice_A_next_scene', sa.Integer(), nullable=True),
    sa.Column('choice_B', sa.String(), nullable=True),
    sa.Column('choice_B_next_scene', sa.Integer(), nullable=True),
    sa.Column('wolf', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('hero_id', sa.Integer(), nullable=True),
    sa.Column('antagonist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['antagonist_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['hero_id'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('storylines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('story_id', sa.Integer(), nullable=True),
    sa.Column('scene_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['scene_id'], ['scenes.id'], ),
    sa.ForeignKeyConstraint(['story_id'], ['stories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('storylines')
    op.drop_table('stories')
    op.drop_table('scenes')
    op.drop_table('characters')
    # ### end Alembic commands ###
