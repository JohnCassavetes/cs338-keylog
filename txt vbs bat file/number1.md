Prompt: find how to make .bat file open txt and execute python file in insiders folders

To create a `.bat` (batch) file that will open a `.txt` file and execute a Python script in the "Insiders" folder, follow these steps:

1. **Create a new `.bat` file**: Open Notepad and save a new file with a `.bat` extension, like `run_script.bat`.

2. **Edit the .bat file**: Add commands to:
   - Open the `.txt` file.
   - Run the Python script from the "Insiders" folder.

Here’s an example of what your `.bat` file might look like:

```bat
@echo off

REM Step 1: Open the .txt file
start "" "C:\path\to\your\file.txt"

REM Step 2: Run the Python script
cd /d "C:\path\to\Insiders"
python your_script.py

REM Optional: Pause to see output before closing
pause
```

### Explanation of Each Line:
- `@echo off`: Hides commands in the terminal for a cleaner look.
- `start "" "C:\path\to\your\file.txt"`: Opens the `.txt` file using the default text editor. Replace `C:\path\to\your\file.txt` with the actual path to your text file.
- `cd /d "C:\path\to\Insiders"`: Navigates to the "Insiders" folder. Replace `C:\path\to\Insiders` with the actual path.
- `python your_script.py`: Runs the Python script. Make sure `python` is in your system’s PATH; otherwise, you may need to specify the full path to Python.
- `pause`: Keeps the terminal open so you can see any output from the Python script. You can remove it if you don’t need this.

### Save and Run:
- Save the `.bat` file and double-click it to execute. It should open the `.txt` file and run the Python script in sequence.