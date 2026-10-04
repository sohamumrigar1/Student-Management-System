import csv
import math
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
from bs4 import BeautifulSoup


# PROJECT SETTINGS

BASE_DIR = Path("gtu_pds_project")
BASE_DIR.mkdir(exist_ok=True)

TEXT_FILE = BASE_DIR / "students.txt"
CSV_FILE = BASE_DIR / "students.csv"
PICKLE_FILE = BASE_DIR / "students.pkl"

INTERACTIVE_INPUT = False


# PRACTICAL 1 - LIBRARIES

def practical1():
    print("\n--- PRACTICAL 1: PYTHON DATA SCIENCE ENVIRONMENT ---")
    print("Python Environment Ready")
    print("NumPy, Pandas, Matplotlib, SciPy, Seaborn")
    print("BeautifulSoup installed and ready")


# PRACTICAL 2 - STUDENT DETAILS

def practical2():
    print("\n--- PRACTICAL 2: STUDENT DETAILS ---")

    if INTERACTIVE_INPUT:
        student = {
            "Roll_No": int(input("Enter Roll No: ")),
            "Name": input("Enter Name: "),
            "Branch": input("Enter Branch: "),
            "Semester": int(input("Enter Semester: "))
        }
    else:
        student = {
            "Roll_No": 101,
            "Name": "Rushit",
            "Branch": "Computer Engineering",
            "Semester": 5
        }

    for key, value in student.items():
        print(key, ":", value)

    return student


# PRACTICAL 3 - MARKS AND GRADE

def practical3():
    print("\n--- PRACTICAL 3: MARKS, PERCENTAGE AND GRADE ---")

    marks = {
        "Python": 82,
        "DBMS": 76,
        "CN": 71,
        "Maths": 68,
        "OS": 85
    }

    total = sum(marks.values())
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    result = "PASS" if all(x >= 40 for x in marks.values()) else "FAIL"

    print("Marks:", marks)
    print("Total:", total)
    print("Percentage:", round(percentage, 2))
    print("Grade:", grade)
    print("Result:", result)


# PRACTICAL 4 - OPERATORS

def practical4():
    print("\n--- PRACTICAL 4: MEMBERSHIP AND BITWISE OPERATORS ---")

    clubs = ["Coding", "Robotics", "Sports", "Music"]
    student_club = "Coding"

    print("Club:", student_club)
    print("Club available:", student_club in clubs)

    LIBRARY = 1
    LAB = 2
    HOSTEL = 4

    permission = LIBRARY | LAB | HOSTEL

    print("Permission code:", permission)
    print("Library:", bool(permission & LIBRARY))
    print("Lab:", bool(permission & LAB))
    print("Hostel:", bool(permission & HOSTEL))


# PRACTICAL 5 - DATA STRUCTURES

def practical5():
    print("\n--- PRACTICAL 5: DATA STRUCTURES ---")

    name = "Rushit"

    subjects = ["Python", "DBMS", "CN"]
    subjects.append("OS")

    semesters = (1, 2, 3, 4, 5)

    clubs = {"Coding", "Robotics"}
    clubs.add("Sports")

    student = {
        "Roll_No": 101,
        "Branch": "Computer Engineering"
    }

    marks = np.array([82, 76, 71, 68, 85])

    print("String:", name)
    print("List:", subjects)
    print("Tuple:", semesters)
    print("Set:", clubs)
    print("Dictionary:", student)
    print("NumPy Array:", marks)
    print("Average:", marks.mean())


# PRACTICAL 6 - FUNCTION AND MATH

def attendance_percentage(attended, total):
    if total == 0:
        return 0

    return attended / total * 100


def practical6():
    print("\n--- PRACTICAL 6: FUNCTION AND MATH MODULE ---")

    attendance = [1, 1, 1, 0, 1]

    attended = sum(attendance)
    total = len(attendance)

    percentage = attendance_percentage(attended, total)

    print("Attendance:", attendance)
    print("Percentage:", percentage)
    print("Rounded Up:", math.ceil(percentage))


# PRACTICAL 7 - PICKLE AND EXCEPTION

def practical7():
    print("\n--- PRACTICAL 7: PICKLE AND EXCEPTION HANDLING ---")

    student = {
        "Roll_No": 101,
        "Name": "Rushit",
        "Marks": [82, 76, 71, 68, 85]
    }

    try:
        with open(PICKLE_FILE, "wb") as file:
            pickle.dump(student, file)

        with open(PICKLE_FILE, "rb") as file:
            data = pickle.load(file)

        print("Stored:", student)
        print("Retrieved:", data)

    except Exception as error:
        print("Error:", error)


# PRACTICAL 8 - TEXT FILE CRUD

def practical8():
    print("\n--- PRACTICAL 8: TEXT FILE CRUD ---")

    with open(TEXT_FILE, "w", encoding="utf-8") as file:
        file.write("101,Rushit\n")
        file.write("102,Aarav\n")

    with open(TEXT_FILE, "r", encoding="utf-8") as file:
        print("Records:")
        print(file.read())

    with open(TEXT_FILE, "a", encoding="utf-8") as file:
        file.write("103,Neel\n")

    print("New record added.")


# PRACTICAL 9 - CSV CRUD

def practical9():
    print("\n--- PRACTICAL 9: CSV CRUD ---")

    records = [
        {"Roll_No": 101, "Name": "Rushit"},
        {"Roll_No": 102, "Name": "Aarav"},
        {"Roll_No": 103, "Name": "Neel"}
    ]

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Roll_No", "Name"]
        )

        writer.writeheader()
        writer.writerows(records)

    with open(CSV_FILE, "r", encoding="utf-8") as file:
        data = list(csv.DictReader(file))

    print("CSV Data:")
    print(data)


# PRACTICAL 10 - DATABASE CONCEPT

def practical10():
    print("\n--- PRACTICAL 10: DATABASE CRUD CONCEPT ---")

    data = pd.DataFrame({
        "Roll_No": [101, 102, 103],
        "Name": ["Rushit", "Aarav", "Neel"],
        "Marks": [82, 76, 90]
    })

    print("CREATE")
    print(data)

    print("\nREAD")
    print(data[data["Roll_No"] == 101])

    data.loc[data["Roll_No"] == 101, "Marks"] = 88

    print("\nUPDATE")
    print(data)

    data = data[data["Roll_No"] != 103]

    print("\nDELETE")
    print(data)


# DATASET GENERATION

def generate_dataset():

    np.random.seed(42)

    departments = [
        "Computer Engineering",
        "IT Engineering",
        "AI/ML",
        "Electronics"
    ]

    data = []

    for i in range(1, 151):

        base = np.random.normal(68, 12)

        python = np.clip(
            base + np.random.normal(5, 8),
            0,
            100
        )

        dbms = np.clip(
            base + np.random.normal(0, 9),
            0,
            100
        )

        cn = np.clip(
            base + np.random.normal(-2, 10),
            0,
            100
        )

        maths = np.clip(
            base + np.random.normal(-5, 12),
            0,
            100
        )

        os = np.clip(
            base + np.random.normal(1, 9),
            0,
            100
        )

        attendance = np.clip(
            65 + (base - 50) * 0.55
            + np.random.normal(0, 8),
            45,
            100
        )

        assignment = np.clip(
            base + np.random.normal(2, 10),
            0,
            100
        )

        data.append({
            "Roll_No": i,
            "Name": "Student_" + str(i),
            "Department": np.random.choice(departments),
            "Python": round(python, 2),
            "DBMS": round(dbms, 2),
            "CN": round(cn, 2),
            "Maths": round(maths, 2),
            "OS": round(os, 2),
            "Attendance": round(attendance, 2),
            "Assignment": round(assignment, 2)
        })

    df = pd.DataFrame(data)

    # Missing values
    df.loc[5, "Python"] = np.nan
    df.loc[17, "Maths"] = np.nan
    df.loc[35, "Attendance"] = np.nan
    df.loc[61, "DBMS"] = np.nan

    # Outlier
    df.loc[10, "Maths"] = 5

    # Duplicate
    df = pd.concat(
        [df, df.iloc[[20]]],
        ignore_index=True
    )

    return df


# PRACTICAL 11 - NUMPY

def practical11(df):

    print("\n--- PRACTICAL 11: NUMPY ANALYSIS ---")

    subjects = [
        "Python",
        "DBMS",
        "CN",
        "Maths",
        "OS"
    ]

    marks = df[subjects].fillna(
        df[subjects].mean()
    ).to_numpy()

    total = marks.sum(axis=1)
    percentage = total / 5

    print("First Student Marks:", marks[0])
    print("Total:", round(total[0], 2))
    print("Percentage:", round(percentage[0], 2))


# PRACTICAL 12 - SCIPY

def practical12(df):

    print("\n--- PRACTICAL 12: SCIPY STATISTICS ---")

    values = df["Python"].dropna()

    print("Mean:", round(stats.tmean(values), 2))
    print("Median:", round(np.median(values), 2))
    print(
        "Standard Deviation:",
        round(stats.tstd(values), 2)
    )
    print(
        "Variance:",
        round(np.var(values, ddof=1), 2)
    )
    print(
        "Skewness:",
        round(stats.skew(values), 2)
    )


# PRACTICAL 13 - PANDAS

def practical13(df):

    print("\n--- PRACTICAL 13: PANDAS STATISTICS ---")

    subjects = [
        "Python",
        "DBMS",
        "CN",
        "Maths",
        "OS"
    ]

    result = pd.DataFrame({
        "Mean": df[subjects].mean(),
        "Median": df[subjects].median(),
        "Std": df[subjects].std(),
        "Variance": df[subjects].var()
    })

    print(result.round(2))


# PRACTICAL 14 - BEAUTIFULSOUP

def practical14(df):

    print("\n--- PRACTICAL 14: BEAUTIFULSOUP ---")

    html = """
    <html>
    <body>
        <table>
            <tr>
                <th>Roll_No</th>
                <th>City</th>
                <th>Club</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Surat</td>
                <td>Coding</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Ahmedabad</td>
                <td>Robotics</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Vadodara</td>
                <td>Music</td>
            </tr>
        </table>
    </body>
    </html>
    """

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    rows = []

    for row in soup.find_all("tr")[1:]:
        cells = row.find_all("td")

        rows.append([
            cells[0].text,
            cells[1].text,
            cells[2].text
        ])

    scraped_df = pd.DataFrame(
        rows,
        columns=["Roll_No", "City", "Club"]
    )

    scraped_df["Roll_No"] = (
        scraped_df["Roll_No"].astype(int)
    )

    print(scraped_df)

    return df


# PRACTICAL 15 - DATA PREPROCESSING

def practical15(df):

    print(
        "\n--- PRACTICAL 15: "
        "DATA CLEANING AND PREPROCESSING ---"
    )

    df = df.copy()

    print("Original Shape:", df.shape)

    # Remove duplicates
    df = df.drop_duplicates()

    subjects = [
        "Python",
        "DBMS",
        "CN",
        "Maths",
        "OS",
        "Attendance",
        "Assignment"
    ]

    # Fill missing values
    for column in subjects:
        df[column] = df[column].fillna(
            df[column].median()
        )

    # Outlier handling
    for column in subjects:

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        df[column] = df[column].clip(
            lower,
            upper
        )

    # Total
    marks_subjects = [
        "Python",
        "DBMS",
        "CN",
        "Maths",
        "OS"
    ]

    df["Total"] = df[marks_subjects].sum(axis=1)

    # Percentage
    df["Percentage"] = df["Total"] / 5

    # Normalization
    minimum = df["Percentage"].min()
    maximum = df["Percentage"].max()

    df["Normalized_Percentage"] = (
        (df["Percentage"] - minimum)
        / (maximum - minimum)
    )

    # Feature engineering
    df["Average_Marks"] = (
        df[marks_subjects].mean(axis=1)
    )

    # Result
    df["Result"] = np.where(
        df["Percentage"] >= 40,
        "PASS",
        "FAIL"
    )

    # Risk Score
    df["Risk_Score"] = (
        0.5 * (100 - df["Percentage"])
        + 0.3 * (100 - df["Attendance"])
        + 0.2 * (100 - df["Assignment"])
    )

    df["Risk_Level"] = pd.cut(
        df["Risk_Score"],
        bins=[-np.inf, 25, 45, np.inf],
        labels=["Low", "Medium", "High"]
    )

    print("\nCleaned Data:")
    print(df.head())

    return df


# DATA ENCODING USING PANDAS

def data_encoding(df):

    print("\n--- DATA ENCODING USING PANDAS ---")

    # Encode Department
    df["Department_Code"] = (
        df["Department"]
        .astype("category")
        .cat.codes
    )

    # Encode Result
    df["Result_Code"] = (
        df["Result"]
        .astype("category")
        .cat.codes
    )

    print("\nEncoded Data:")

    print(
        df[
            [
                "Department",
                "Department_Code",
                "Result",
                "Result_Code"
            ]
        ].head(10)
    )

    return df


# PRACTICAL 16 - VISUALIZATION

def practical16(df):

    print("\n--- PRACTICAL 16: DATA VISUALIZATION ---")

    subjects = [
        "Python",
        "DBMS",
        "CN",
        "Maths",
        "OS"
    ]

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["Percentage"],
        kde=True
    )

    plt.title(
        "Distribution of Student Percentage"
    )

    plt.xlabel("Percentage")
    plt.ylabel("Students")

    plt.show()

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df[subjects]
    )

    plt.title(
        "Subject-wise Marks"
    )

    plt.show()

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="Attendance",
        y="Percentage",
        hue="Result"
    )

    plt.title(
        "Attendance vs Percentage"
    )

    plt.show()

    plt.figure(figsize=(8, 5))

    correlation = df[
        subjects
        + [
            "Attendance",
            "Assignment",
            "Percentage"
        ]
    ].corr()

    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f"
    )

    plt.title(
        "Correlation Heatmap"
    )

    plt.show()


# PRACTICAL 17 - UNI/BIVARIATE

def practical17(df):

    print(
        "\n--- PRACTICAL 17: "
        "UNIVARIATE AND BIVARIATE ANALYSIS ---"
    )

    python_marks = df["Python"]

    print("UNIVARIATE ANALYSIS")

    print(
        "Mean:",
        round(python_marks.mean(), 2)
    )

    print(
        "Median:",
        round(python_marks.median(), 2)
    )

    print(
        "Standard Deviation:",
        round(python_marks.std(), 2)
    )

    correlation = df["Python"].corr(
        df["DBMS"]
    )

    print("\nBIVARIATE ANALYSIS")

    print(
        "Python vs DBMS Correlation:",
        round(correlation, 2)
    )

    covariance = df["Python"].cov(
        df["DBMS"]
    )

    print(
        "Covariance:",
        round(covariance, 2)
    )


# PRACTICAL 18 - NORMAL DISTRIBUTION

def practical18(df):

    print(
        "\n--- PRACTICAL 18: "
        "NORMAL DISTRIBUTION ---"
    )

    values = df["Percentage"]

    mean = values.mean()
    std = values.std()

    distribution = stats.norm(
        loc=mean,
        scale=std
    )

    pdf = distribution.pdf(70)
    cdf = distribution.cdf(40)

    probability = 1 - cdf

    print(
        "Mean:",
        round(mean, 2)
    )

    print(
        "Standard Deviation:",
        round(std, 2)
    )

    print(
        "PDF at 70:",
        round(pdf, 4)
    )

    print(
        "CDF at 40:",
        round(cdf, 4)
    )

    print(
        "P(Marks >= 40):",
        round(probability, 4)
    )

    x = np.linspace(
        mean - 4 * std,
        mean + 4 * std,
        300
    )

    y = distribution.pdf(x)

    plt.figure(figsize=(8, 5))

    plt.plot(x, y)

    plt.title(
        "Normal Distribution of Student Percentage"
    )

    plt.xlabel("Percentage")
    plt.ylabel("Probability Density")

    plt.grid(True)

    plt.show()


# MAIN PROGRAM

def main():

    print(
        "\n=============================================="
    )

    print(
        "      GTU PDS PRACTICAL 1 TO 18"
    )

    print(
        "      STUDENT PERFORMANCE ANALYSIS"
    )

    print(
        "=============================================="
    )

    practical1()
    practical2()
    practical3()
    practical4()
    practical5()
    practical6()
    practical7()
    practical8()
    practical9()
    practical10()

    # Create dataset
    df = generate_dataset()

    print(
        "\nDataset Created Successfully"
    )

    print(
        "Dataset Shape:",
        df.shape
    )

    practical11(df)
    practical12(df)
    practical13(df)
    practical14(df)

    # Data preprocessing
    df = practical15(df)

    # Data encoding
    df = data_encoding(df)

    # Visualization
    practical16(df)

    practical17(df)
    practical18(df)

    print(
        "\n=============================================="
    )

    print(
        "ALL PRACTICALS COMPLETED"
    )

    print(
        "=============================================="
    )


if __name__ == "__main__":
    main()