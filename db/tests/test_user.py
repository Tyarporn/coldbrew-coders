import os

import pytest

import db.user as usr


RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)

TEST_DEL_NAME = 'Game to be deleted'