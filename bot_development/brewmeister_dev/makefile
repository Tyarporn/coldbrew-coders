LINTER = flake8
brewmeister_directory = /Users/shashankasharma/cs_stuff/coldbrew-coders/bot_development/brewmeister_dev
REQ_DIR = .
PYTESTFLAGS = -vv --verbose --tb=short

FORCE:

bot_tests: lint unit

unit: FORCE
	cd $(brewmeister_directory); pytest $(PYTESTFLAGS)

lint: FORCE
	$(LINTER) $(brewmeister_directory)/endpoints.py
	$(LINTER) $(brewmeister_directory)/brewmeister.py