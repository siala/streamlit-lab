# Installation procedure.

Requires Python 3.13 or newer.

Follow every step in order. Do not skip a step.

## 1. CHECK PYTHON

**macOS / Linux:** `python3 --version`

**Windows:** `py --version`

The version must be 3.13 or newer, otherwise you need to install a recent version (and make it your default runner).

## 2. OPEN A COMMAND WINDOW IN THIS FOLDER

The folder that contains `app.py`, `test.py` and `requirements.txt`.

**Windows:** open the folder in File Explorer, click the address bar,
type `cmd` and press Enter.

**macOS/Linux:** open Terminal and cd to this folder. In my machine, this is done using the command:

```sh
$cd /Users/msiala/Desktop/ProhiCode
```

## 3. CREATE THE ENVIRONMENT

**macOS / Linux:** `python3 -m venv .venv`

**Windows:** `py -m venv .venv`

## 4. ACTIVATE THE ENVIRONMENT

**macOS / Linux:** `source .venv/bin/activate`

**Windows PowerShell:** `.venv\Scripts\Activate.ps1`

**Windows Command Prompt:** `.venv\Scripts\activate.bat`

The prompt must now begin with `(.venv)`.

If PowerShell refuses to run the script, use Command Prompt instead.

## 5. INSTALL THE PACKAGES

```sh
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 6. RUN THE TEST

```sh
python -m streamlit run test.py
```

## 7. OPEN THE APP

The command window prints: URL: http://127.0.0.1:8501 (or something similar)

If no browser opens by itself. Copy that address into your browser.

The dataset table must (magically) appear as a web page.

Congratulations, you are now running a proper local web server!

## 8. STOP THE SERVER

Click the command window, then press `Ctrl+C` to kill the process.
