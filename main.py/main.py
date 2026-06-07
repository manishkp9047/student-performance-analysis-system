
import matplotlib.pyplot as plt
import pandas as pd

# Read CSV
df = pd.read_csv("data/students.csv")

# First look at data
print(df.head())

# Dataset information
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Store original row count
rows_before = len(df)

# Remove missing values
df = df.dropna()

# Check duplicates
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Final row count
rows_after = len(df)

print("\nRows Before Cleaning:", rows_before)
print("Rows After Cleaning :", rows_after)

print("\nClean Dataset:")


# calaulate total marks
df["Total"] =(
    df["Math"] +
    df["Science"] +
    df["English"] +
    df["Computer"]
)
print("\nDataset with Total Marks:")


# percentage calaculator
df["Percentage"] = df["Total"] / 4
print("\nDataset with Percentage")



#  adding grouping

def grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 60:
        return "C"
    else:
        return "D"
df["Grade"] = df ["Percentage"].apply(grade)

print("\nDataset with Grades:")
print(df)

# finding topper

topper = df.loc[df["Percentage"].idxmax()]
print("\nTopper Details:")
print(topper)

#  finding weak student
weak_studensts = df[df["Percentage"] < 60]
print("\nweak students:")
print(weak_studensts)


# subject wise analysis

print("\nSubject Averages")

print("Math:", df["Math"].mean())
print("Science:", df["Science"].mean())
print("English:", df["English"].mean())
print("Computer:", df["Computer"].mean())

# Find Best Subject

subjects = ["Math", "Science", "English", "Computer"]

for subject in subjects:
    print(subject, "Average:", df[subject].mean())
subject_avg = {
    "Math": df["Math"].mean(),
    "Science": df["Science"].mean(),
    "English": df["English"].mean(),
    "Computer": df["Computer"].mean()
}

best_subject = max(subject_avg, key=subject_avg.get)

print("\nBest Performing Subject:")
print(best_subject)

# chart making

subjects = ["Math", "Science", "English", "Computer"]

averages = [
    df["Math"].mean(),
    df["Science"].mean(),
    df["English"].mean(),
    df["Computer"].mean()
]

plt.figure(figsize=(8,5))

plt.bar(subjects, averages)

plt.title("Subject Wise Average Marks")

plt.xlabel("Subjects")

plt.ylabel("Average Marks")

plt.savefig("charts/subject_average.png")

print("\nChart Saved Successfully!")

plt.figure(figsize=(10,5))

plt.bar(df["Name"], df["Percentage"])

plt.title("Student Percentage Comparison")

plt.xlabel("Students")

plt.ylabel("Percentage")

plt.savefig("charts/student_performance.png")

plt.show()


# creating the report file

with open("reports/report.txt", "w") as file:

    file.write("STUDENT PERFORMANCE REPORT\n")
    file.write("=========================\n\n")

    file.write(f"Total Students: {len(df)}\n")

    file.write(
        f"Average Percentage: {df['Percentage'].mean():.2f}\n"
    )

    file.write(
        f"Topper: {topper['Name']} ({topper['Percentage']}%)\n"
    )

    file.write(
        f"Best Subject: {best_subject}\n"
    )

print("\nReport Generated Successfully!")