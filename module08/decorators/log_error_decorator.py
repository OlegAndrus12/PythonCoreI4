import logging
import os
from functools import wraps

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

GRADEBOOK_FILE = "gradebook.txt"


def log_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            logger.warning("[%s] invalid value: %s", func.__name__, e)
        except TypeError as e:
            logger.error("[%s] wrong type: %s", func.__name__, e)
        except KeyError as e:
            logger.error("[%s] student not found: %s", func.__name__, e)
        except ZeroDivisionError:
            logger.error("[%s] no grades recorded yet (args=%s)", func.__name__, args)
        except Exception as e:
            logger.critical("[%s] unexpected error: %s", func.__name__, e)
            raise

    return wrapper

def get_records():
    if not os.path.exists(GRADEBOOK_FILE):
        raise FileNotFoundError
    
    book = {}

    with open(GRADEBOOK_FILE) as f:
        for line in f:
            name, raw = line.strip().split(":", 1)
            book[name] = [float(g) for g in raw.split(",") if g]
    return book


def save():
    with open(GRADEBOOK_FILE, "w") as f:
        for name, grades in book.items():
            raw = ",".join(str(g) for g in grades)
            f.write(f"{name}:{raw}\n")


try:
    book = get_records()
except FileNotFoundError:
    book = {}


@log_errors
def add_student(name):
    if not isinstance(name, str):
        raise TypeError(f"name must be a string, got {type(name).__name__}")
    if name in book:
        raise ValueError(f"student '{name}' already exists")
    
    book[name] = []
    save()
    logger.info("added student: %s", name)


@log_errors
def add_grade(name, grade):
    grade = float(grade)
    if not (0 <= grade <= 100):
        raise ValueError(f"grade must be 0–100, got {grade}")
    book[name].append(grade)
    save()
    logger.info("added grade %.1f for %s", grade, name)


@log_errors
def get_average(name):
    grades = book[name]
    avg = sum(grades) / len(grades)
    logger.info("%s average: %.2f", name, avg)
    return avg


@log_errors
def get_report():
    print("\n--- Gradebook Report ---")
    for name, grades in book.items():
        avg = sum(grades) / len(grades) if grades else None
        status = "pass" if avg and avg >= 60 else "fail"
        avg_str = f"{avg:.1f}" if avg is not None else "n/a"
        print(f"  {name}: {grades} → avg {avg_str} [{status}]")


@log_errors
def main():
    while True:
        print("\n1. Add student")
        print("2. Add grade")
        print("3. Get average")
        print("4. Report")
        print("0. Exit")

        choice = input("Choice: ").strip()
        
        match choice:
            case "1":
                name = input("  Name: ")
                add_student(name)
            case "2":
                name = input("  Name: ")
                grade = input("  Grade: ")
                add_grade(name, grade)
            case "3":
                name = input("  Name: ")
                avg = get_average(name)
                if avg is not None:
                    print(f"  Average: {avg:.1f}")
            case "4":
                get_report()
            case _:
                raise ValueError(f"invalid option '{choice}', choose 1–4")



        if choice == "0":
            break


main()