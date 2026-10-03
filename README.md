# 🎓 Student Data Search
A lightweight desktop application built with **Python, Tkinter and pandas** that lets you search a student's complete record by roll number from a CSV file and instantly view their details along with total marks.
## 📌 Overview
Student Data Search reads student data from a CSV file and provides a simple GUI where the user enters a roll number. The app validates the input, finds the matching student, displays all available details, and calculates the total marks across JavaScript, Python and Data Structures. No database or server is needed, only a CSV file.

## ✨ Features

- Search a student by roll number (`student_id`)
- Displays all CSV columns dynamically, so new columns appear without code changes
- Automatically calculates total marks (JS + Python + DS)
- Input validation for empty and non-numeric values
- File and column validation, with clear error messages
- Shows a "No data found" message for an invalid roll number
- Search, Clear and Exit buttons, plus an Enter-key shortcut

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core language |
| pandas | Loading and filtering CSV data |
| Tkinter | Graphical user interface |

## 📁 Project Structure

```
student-data-search/
├── student_search.py   # Main application
├── sample.csv          # Sample student data
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
```

## 📊 CSV Format

The CSV file must contain at least these columns: `student_id`, `js`, `py`, `ds`.

```csv
student_id,name,gender,age,attendance_percentage,study_hours_per_day,js,py,ds
1,Rahul Sharma,M,15,90%,4,12,13,12
2,Priya Patel,F,16,96%,2,13,12,10
```

## 🚀 Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/student-data-search.git

# 2. Go to the project folder
cd student-data-search

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python student_search.py
```

Enter a roll number (for example `1`) and click **Search** or press **Enter**.

## ⚙️ How It Works

1. The app loads `sample.csv` into a pandas DataFrame.
2. It checks that the file exists and the required columns are present.
3. The user enters a roll number, and the input is validated.
4. The DataFrame is filtered on `student_id` to find the matching row.
5. All the student's details are displayed in a scrollable text area.
6. Total marks are calculated and shown at the bottom.

## 🔮 Future Improvements

- Search by student name
- File-picker dialog to choose any CSV file
- Percentage and grade calculation
- Export a student's result to PDF
- Charts for subject-wise performance

## 👤 Author

**Bhakti Kulkarni**
Email: <kulkarnibhakti171@gmail.com>


