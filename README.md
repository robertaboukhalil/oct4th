# oct4th

CLI tool to convert CSV/TSV files to Excel spreadsheets, while not converting gene names (e.g. OCT4, DEC1) into dates in the process.

For converting small files, you can use the [Oct4th web application](https://oct4th.sandbox.bio).

To learn more about this issue, check out [this article](https://medium.com/@robaboukhalil/how-to-fix-excels-gene-to-date-conversion-5c98d0072450).

## Installation

```bash
pip3 install -U oct4th
```

If you don't have access to a computer where you can run `pip`, check out this [Colab notebook](https://colab.research.google.com/drive/1c7wGcEySoR6hIidVoZZKTQDYcOtC8UgU?usp=sharing).

## Usage

### As a CLI:

```bash
# Convert a CSV file to XLSX
oct4th --input ./data/test.csv --output ./data/test.xlsx
```

### From Python:

```python
import oct4th

# Convert a CSV file to XLSX
oct4th.csv_to_xlsx(file_in="./data/test.csv", file_out="./data/test.xlsx")
```

## Developing

```bash
python3 -m venv ve
. ve/bin/activate
pip install setuptools wheel twine pytest xlsxwriter pandas xlrd
```

## Run Tests

```bash
PYTHONPATH=. pytest ./tests/
```

## Deploy

```bash
# Clean up and rebuild
. ve/bin/activate
rm -rf ./build/ ./dist/
python3 setup.py sdist bdist_wheel

# Check before deploying
twine check dist/*

# Upload to testpypi
python3 -m twine upload --repository testpypi dist/*

# Test install
deactivate; pip3 install -U -i https://test.pypi.org/simple/ oct4th==1.0.0b9

# Deploy to pypi
# python3 -m twine upload --repository pypi dist/*
```
