## Installation

You can install the application by following the instructions:

1. Make sure Python is installed:
   - Windows: [Python Downloads](https://www.python.org/downloads/windows/)
   - Ubuntu: `sudo apt install python3`

2. Install Poetry: [Poetry Installation](https://python-poetry.org/docs/#installation)
   - Using pipx: 
        ```
        pipx install poetry
        ```
   - Windows (PowerShell): 
        ```
        (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
        ```
   - Linux, macOS, WSL:  
        ```
        curl -sSL https://install.python-poetry.org | python3 -
        ```

3. Add Poetry to environment variables (PATH):
   - Windows: `%APPDATA%\Python\Scripts`
   - Unix: `$HOME/.local/bin`

4. Install Graphviz: [Graphviz Download](https://graphviz.org/download/)
   - Windows: Download the installer
   - Ubuntu: 
        ```
        sudo apt install graphviz
        ```

5. Make sure to add Graphviz to environment variables (PATH):
   - In Windows, check *`Add Graphviz to the system PATH for …`* in the install options screen while installing it.
   - In Ubuntu, it should be added automatically after the installation.

6. *(Optional)* On WSL and Ubuntu, if you encounter an error indicating that there is no module named Tkinter, use the following:
   ```
   sudo apt-get install python3-tk
   ```

7. In the root folder where the file *`pyproject.toml`* exists, run the following command to install all the dependencies:
   ```
   poetry install
   ```

## Running the application

You can run the application using any of the following methods:

- **Method 1: Activating Poetry Virtual Environment:**
  ```
  poetry shell
  python main.py
  ```

- **Method 2: Running a command inside Poetry without activating the environment:**
  ```
  poetry run python main.py
  ```
