#CSV Column Cleaner

## Overview

This application helps you clean up a CSV files by selecting only the columns you need, making your data more manageable and focused. It's a simple tool that allows you to:

- Upload a CSV file
- Select which columns to keep
- Preview the cleaned data
- Download a new CSV file with only the columns you selected

## Installation Guide for Windows 11

### One-Time Setup (Ask IT for help if needed)

1. **Install Python**:
   - Download Python from [python.org](https://www.python.org/downloads/)
   - **IMPORTANT:** Check "Add Python to PATH" during installation (this checkbox is on the first screen)
   - Click "Install Now" with the recommended options
   - After installation completes, restart your computer to ensure PATH settings are updated

2. **Install Required Packages**:
   - Open Command Prompt as Administrator (search for "cmd", right-click and select "Run as administrator")
   - Copy and paste this command:
   ```
   pip install streamlit pandas openpyxl
   ```
   - Press Enter and wait for installation to complete

### Fixing "streamlit is not recognized" Error

If you see an error that says "streamlit is not recognized", try these solutions:

**Solution 1: Use Python with the command**
```
python -m streamlit run excel_cleaner.py
```

**Solution 2: Install streamlit directly**
```
pip install --user streamlit
python -m streamlit run excel_cleaner.py
```

**Solution 3: Use full path to streamlit**
```
C:\Users\YonahFeld\AppData\Local\Programs\Python\Python39\Scripts\streamlit.exe run excel_cleaner.py
```
(Your actual path may be different - look in your Python installation folder)

**Solution 4: Create a launcher batch file**
1. Create a new text file in the same folder as the application
2. Add this line to the file:
   ```
   python -m streamlit run excel_cleaner.py
   ```
3. Save the file as "start_app.bat"
4. Double-click on start_app.bat to launch the application

### Running the Application

1. **Start the Application**:
   - Navigate to the folder containing the application files
   - Right-click in an empty area while holding the Shift key
   - Select "Open PowerShell window here" or "Open command window here"
   - Use one of these commands (try the first, and if it doesn't work, try the others):
   ```
   streamlit run excel_cleaner.py
   ```
   OR
   ```
   python -m streamlit run excel_cleaner.py
   ```
   - The application will start and automatically open in your web browser
   - If it doesn't open automatically, go to: http://localhost:8501

2. **Using the Application**:
   - The application runs in your web browser, but everything is processed locally on your computer (your data never leaves your machine)
   - Follow the 3 steps shown in the application:
     1. Upload your CSV file
     2. Select columns to keep
     3. Preview and download the cleaned file

## How to Use

### Step 1: Upload Your File
- Click the "Browse files" button and select your CSV file
- Wait for the file to upload and process
- You'll see a success message when the file is ready

### Step 2: Select Columns to Keep
- Use the "Quick Selection" options:
  - "Select All" - keeps all columns
  - "Select Bare Minimum" - selects only the essential columns (names, contact info, company details)
- Or use the dropdown menu to manually select which columns to keep
- You can add or remove columns as needed

### Step 3: Preview and Download
- Preview the first 5 rows of your cleaned file
- See how much smaller your file will be
- Click the "Download Cleaned File" button to save your new CSV file
- The downloaded file will have the same name as your original file with "_cleaned" added

## Troubleshooting

- **Application won't start**: Make sure Python and all required packages are installed correctly
- **File won't upload**: Ensure your file is in CSV format (.csv extension)
- **Browser doesn't open**: Try going to http://localhost:8501 manually
- **Columns missing**: Use the "Select All" option and then manually deselect the columns you don't want



- Windows 11
- Intel Core Ultra 7 processor or equivalent
- 4GB RAM minimum
- 100MB free disk space
- Internet connection (for first-time setup only) 
