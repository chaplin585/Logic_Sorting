TARGET = Logic-Sorting
PY = python

$(TARGET): thirdparty\main.o thirdparty/Sorter.o thirdparty/Parser.o 
	$(PY) thirdparty\main.o
	$(PY) thirdparty\Parser.o
	$(PY) thirdparty\Sorter.o	

main.o: src\main.py 
	$(PY) src\main.py

Parser.o: src\Parsingfile.py 
	$(PY) src\Parsingfile.py

Sorter.o: src\Sorting.py 
	$(PY) src\Sorting.py

test:  
	$(PY) test/test_main_btns.py
	$(PY) test/test_main_btn2.py
	$(PY) test/test_main_label.py
	  


.PHONY: all test clean

clean:
	rm $(TARGET) *.o

