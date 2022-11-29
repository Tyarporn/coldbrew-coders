import os

import pytest

import db.bot_info as bi


RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)
