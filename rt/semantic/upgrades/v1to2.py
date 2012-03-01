# -*- coding: utf-8 -*-
from rt.semantic import logger


def upgrade(context):
    '''
    Upgrade from version 1 to version 2
    '''
    logger.info("Updating types info")
    context.runImportStepFromProfile(profile_id='profile-rt.semantic:default',
                                     step_id='typeinfo')
