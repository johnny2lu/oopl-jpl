.DEFAULT_GOAL := all

all:
	cd examples; make all

clean:
	cd examples; make clean

config:
	git config -l

init:
	touch README
	git init
	git add README
	git commit -m 'first commit'
	git remote add origin git@github.com:gpdowning/oopl-jpl.git
	git push -u origin master

pull:
	make clean
	@echo
	git pull
	git status

push:
	make clean
	@echo
	git add .gitignore
	git add .travis.yml
	git add examples
	git add makefile
	git add notes
	git commit -m "another commit"
	git push
	git status

run:
	cd examples; make run

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

sync:
	@rsync -r -t -u -v --delete            \
    --include "Hello.py"                   \
    --include "Assertions.py"              \
    --include "UnitTests1.py"              \
    --include "UnitTests2.py"              \
    --include "UnitTests3.py"              \
    --include "Coverage1.py"               \
    --include "Coverage2.py"               \
    --include "Coverage3.py"               \
    --include "IsPrime.py"                 \
    --include "IsPrimeT.py"                \
    --include "Exceptions.py"              \
    --include "Types.py"                   \
    --include "Operators.py"               \
    --include "Variables.py"               \
    --include "Cache.py"                   \
    --include "Copy.py"                    \
    --include "Factorial.py"               \
    --include "Reduce1.py"                 \
    --exclude "*"                          \
    ../../examples/python/ examples

travis:
	cd examples; make travis
