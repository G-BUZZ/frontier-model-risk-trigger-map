PYTHON ?= python3
export PYTHONPATH := src

.PHONY: validate build test brief clean

validate:
	$(PYTHON) -m frontier_trigger_map.cli validate

build: validate
	$(PYTHON) -m frontier_trigger_map.cli build

test:
	$(PYTHON) -m unittest discover -s tests -v

brief:
	mkdir -p outputs/rendered
	pandoc docs/policy_brief.md -s -o outputs/rendered/policy_brief.html
	pandoc docs/executive_summary_eu_ai_office.md -s -o outputs/rendered/executive_summary_eu_ai_office.html

clean:
	rm -f outputs/trigger_map.csv outputs/trigger_map.md
	rm -rf outputs/rendered
report:
	python3 -m frontier_trigger_map.report
