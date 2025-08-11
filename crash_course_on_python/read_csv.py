import csv

with open("employee.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print("{:<12} {:<15} {:<12} {:<10}".format(*row))


def read_employees(file_path):
    with open(file_path, newline='') as f:
        return list(csv.DictReader(f))

def avg_salary_by_dept(records):
    dept_data = {}
    for r in records:
        dept = r["Department"]
        salary = float(r["Salary"])
        dept_data.setdefault(dept, []).append(salary)
    return {d: sum(s)/len(s) for d, s in dept_data.items()}

if __name__ == "__main__":
    employees = read_employees("employee.csv")
    avg = avg_salary_by_dept(employees)
    print("Average Salary by Department:")
    for dept, salary in avg.items():
        print(f"{dept}: ₹{salary:.2f}")