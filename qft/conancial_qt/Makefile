FILENAME=talk
TESTNAME=test
paper: $(FILENAME).tex
	xelatex $(FILENAME).tex
	xelatex $(FILENAME).tex
test: $(TESTNAME).tex
	xelatex $(TESTNAME).tex
	xelatex $(TESTNAME).tex
clean:
	rm -f *.out $(FILENAME).bib *.bbl *.log *.blg  *.aux *.nav *.snm *.toc 
