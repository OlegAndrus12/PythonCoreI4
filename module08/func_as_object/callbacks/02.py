employees = [
    {"name": "Alice", "salary": 95000, "department": "Engineering", "tenure": 5},
    {"name": "Bob",   "salary": 72000, "department": "Marketing",   "tenure": 2},
    {"name": "Carol", "salary": 110000,"department": "Engineering", "tenure": 8},
    {"name": "Dan",   "salary": 68000, "department": "HR",          "tenure": 1},
    {"name": "Eve",   "salary": 87000, "department": "Marketing",   "tenure": 6},
]

by_salary = sorted(employees, key=lambda e: e["salary"], reverse=True)
by_tenure = sorted(employees, key=lambda e: e["tenure"])
by_dept_then_salary = sorted(employees, key=lambda e: (e["department"], -e["salary"]))

print("By salary (desc):")
for e in by_salary:
    print(f"  {e['name']:<8} ${e['salary']:,}")

print("\nBy tenure (asc):")
for e in by_tenure:
    print(f"  {e['name']:<8} {e['tenure']} yrs")

print("\nBy department, then salary (desc):")
for e in by_dept_then_salary:
    print(f"  {e['department']:<15} {e['name']:<8} ${e['salary']:,}")
