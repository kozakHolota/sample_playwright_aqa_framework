# Project Title

A short description of your project here.

## Pre-Requisites

You must have the following installed:

- Python 3
- Node Package Manager (npm)

## Installation Steps

1. Clone the repository

   ```
   git clone https://github.com/kozakHolota/sample_playwright_aqa_framework.git
   ```

2. Go to the project directory

   ```
   cd <project_directory>
   ```

### For Windows Users

3. Setting up Python virtual environment

   ```
   python -m venv env
   ```

4. Activating virtual environment

   ```
   .\env\Scripts\activate
   ```

### For Linux/macOS Users

3. Setting up Python virtual environment

   ```
   python -m venv env
   ```

4. Activating virtual environment

   ```
   source env/bin/activate
   ```

Finally,  

5. Pip Install Dependencies

   ```
   pip install -r requirements.txt
   ```

## Testing

You can run tests using `pytest` from the project root directory. 
Test report will be generated in `reports/` directory. 
Screenshots from test failures will be stored in `test_results/` directory. 
Sample report can be found in `reports/sample_report.html`.

## Deployment
To deploy this project run:
```bash
pthon setup.py install
```

