import os

import pytest

import db.reviews as rev


RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)

TEST_REVIEW_NAME = 'Game to be deleted'