TARGET = Logic-Sorting
PY = python
TEST = python -m unittest  


$(TARGET): RUN Test 
	RUN
	Test

RUN: thirdparty/main.o thirdparty/Sorter.o thirdparty/Parser.o
	$(PY) thirdparty/main.o
	$(PY) thirdparty/Parser.o
	$(PY) thirdparty/Sorter.o


main.o: src\main.py 
	$(PY) src\main.py

Parser.o: src\Parsingfile.py 
	$(PY) src\Parsingfile.py

Sorter.o: src\Sorting.py 
	$(PY) src\Sorting.py

Test: test/test_parsing.py test/test_sorting.py
	$(Test) test/test_parsing.py 
	$(Test) test/test_sorting.py




clean:
	rm $(TARGET) *.o

