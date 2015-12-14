.PHONY: clean test verbose coverage all paperfig

clean:
	find .. -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" -o -name "testnib.nii.gz" -o -name "temp.txt" | xargs rm -f

test:
	nosetests code/utils/tests -w ..

verbose:
	nosetests -v code/utils/tests -w ..


coverage:
	nosetests code/utils/tests -w .. --with-coverage --cover-package=utils/functions

all: 
	cd scripts && make histograms
	cd scripts && make smoothing
	cd scripts && make glm
	cd scripts && make logistic
	cd scripts && make diagnostics
	cd scripts && make mixedmodel

paperfig:
