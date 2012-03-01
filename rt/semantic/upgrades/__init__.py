from plone.app.upgrade.utils import loadMigrationProfile
from plutonian.gs import upgrade_to
from plutonian import Configurator

config = Configurator('rt.semantic')


@upgrade_to(2)
def semantic_behavior(context):
    loadMigrationProfile(context, 'profile-rt.semantic:default',
        steps=('typeinfo',))

