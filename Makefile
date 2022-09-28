TARGET = Logic-Sorting
PY = python

   


$(TARGET): thirdparty/main.o thirdparty/Sorter.o thirdparty/Parser.o thirdparty/Test.o
	$(PY) thirdparty/main.o
	$(PY) thirdparty/Parser.o
	$(PY) thirdparty/Sorter.o
	
	

main.o: src\main.py 
	$(PY) src\main.py

Parser.o: src\Parsingfile.py 
	$(PY) src\Parsingfile.py

Sorter.o: src\Sorting.py 
	$(PY) src\Sorting.py


test:  
	$(PY) thirdparty/Test.o
	  
Test.o: test_parsing.py	
	$(PY) test_parsing.py



	


.PHONY: all test clean

clean:
	rm $(TARGET) *.o

