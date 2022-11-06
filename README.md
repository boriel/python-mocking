# python-mocking
Tricky mocking scenarios in with Python unittest.

This little project just show some typical unit test mocking cases.
The functions to test are placed in src/common package (folder).

Test are located in folder `tests/common`.

## Installing (project setup)

This test uses AWS `boto3` library, so just type
```shell
pip install boto3
```
or
```shell
pip install -r requirements.txt
```

## Testing
To run the test fron the command line just do:
```shell
python -m unittest tests/common/*.py -v
```
