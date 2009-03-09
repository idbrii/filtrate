MAIN = rr_main.py
INPUT_FILE=sampletestlist.txt
OUTPUT_FILE=out_tests_to_run.txt
.PHONY:	init run clean 

init:	$(INPUT_FILE)

run:	init
	python $(MAIN)

$(INPUT_FILE):
	ls * > $@

clean:
	-rm *.pyc
	-rm $(INPUT_FILE) $(OUTPUT_FILE)
