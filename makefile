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
    --include "Factorial.py"               \
    --include "FactorialT.py"              \
    --include "Cache.py"                   \
    --include "Copy.py"                    \
    --include "Reduce.py"                  \
    --include "ReduceT.py"                 \
    --include "Iteration.py"               \
    --include "Comprehensions.py"          \
    --include "Iterables.py"               \
    --include "Yield.py"                   \
    --include "Map.py"                     \
    --include "MapT.py"                    \
    --include "FileInputOutput.py"         \
    --include "FormattedOutput.py"         \
    --include "RangeIterator.py"           \
    --include "RangeIteratorT.py"          \
    --include "Range.py"                   \
    --include "FunctionKeywords.py"        \
    --include "FunctionDefaults.py"        \
    --include "FunctionUnpacking.py"       \
    --include "FunctionTuple.py"           \
    --include "FunctionDict.py"            \
    --include "Reduce2.py"                 \
    --include "Reduce2T.py"                \
    --include "Classes.py"                 \
    --include "Complex.py"                 \
    --include "ComplexT.py"                \
    --exclude "*"                          \
    ../../examples/python/ examples

travis:
	cd examples; make travis
