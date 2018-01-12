.DEFAULT_GOAL := all

FILES :=                    \
    Hello                   \
    UnitTests3              \
    Coverage1               \
    Coverage2               \
    Coverage3               \
    IsPrime                 \
    IsPrimeT                \
    Exceptions              \
    Types                   \
    Operators               \
    Variables               \
    Factorial               \
    FactorialT              \
    Cache                   \
    Copy                    \
    Reduce                  \
    ReduceT                 \
    Iteration               \
    Comprehensions          \
    Iterables               \
    Yield                   \
    Map                     \
    MapT                    \
    FileInputOutput         \
    FormattedOutput         \
    RangeIterator           \
    RangeIteratorT          \
    Range                   \
    FunctionKeywords        \
    FunctionDefaults        \
    FunctionUnpacking       \
    FunctionTuple           \
    FunctionDict            \
    Reduce2                 \
    Reduce2T                \
    Classes                 \
    Complex

.pylintrc:
	pylint --disable=locally-disabled --reports=no --generate-rcfile > $@

%.pyx: %.py .pylintrc
	-mypy     $<
	-pylint   $<
	-coverage run    --branch $<
	-coverage report -m

all:

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -rf .mypy_cache

run: $(FILES:=.pyx)

travis:
	make clean
	ls -al
	make run
