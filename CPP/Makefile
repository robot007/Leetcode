all: 1_1_3_LongestConsecutiveSequence.exe RemoveDuplicates_class.exe RemoveDuplicates_func.exe TestCompiler.exe

# all: $(patsubst %.c, %.exe, $(wildcard *.c))
%.exe: %.cpp Makefile
	g++ $< -o $@ -std=c++14 -Wall -O2
