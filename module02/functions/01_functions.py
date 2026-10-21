# Without a function the same formula is repeated for every patient:
#   anna_bmi = 62 / (1.68 ** 2)
#   petro_bmi = 95 / (1.80 ** 2)
# A function gives the formula a name and one place to fix bugs.
def calculate_bmi(weight_kg, height_m):
    return round(weight_kg / height_m**2, 1)


print(calculate_bmi(62, 1.68))  # 22.0
print(calculate_bmi(95, 1.80))  # 29.3


# default parameters and named arguments
# Activated charcoal after poisoning: about 1 g per kg of body weight
def calculate_charcoal_dose(weight_kg, g_per_kg=1.0, max_dose_g=50, tablet_mg=250):
    dose_g = float(min(weight_kg * g_per_kg, max_dose_g))
    tablets = round(dose_g * 1000 / tablet_mg)
    return dose_g, tablets


print(calculate_charcoal_dose(20))  # child, defaults -> (20.0, 80)
print(calculate_charcoal_dose(62))  # capped by max_dose_g -> (50.0, 200)
print(calculate_charcoal_dose(20, tablet_mg=500))  # skip middle params, set by name
print(calculate_charcoal_dose(max_dose_g=25, weight_kg=70))  # order is free

# Positional arguments must come before named ones:
# calculate_charcoal_dose(weight_kg=20, 1.0)  -> SyntaxError


# validate input and return early -------------------------------
# Return None (or raise) instead of calculating garbage.
def parse_blood_pressure(text):
    parts = [part.strip() for part in text.split("/")]
    if len(parts) != 2 or not all(part.isdigit() for part in parts):
        return None
    systolic, diastolic = int(parts[0]), int(parts[1])
    if systolic <= diastolic:
        return None
    return systolic, diastolic


print(parse_blood_pressure("120/80"))  # (120, 80)
print(parse_blood_pressure(" 135 / 85 "))  # (135, 85): spaces are tolerated
print(parse_blood_pressure("80/120"))  # None: values swapped
print(parse_blood_pressure("high"))  # None


# return several values
# Python packs them into a tuple; the caller unpacks them.
def classify_blood_pressure(systolic, diastolic):
    if systolic >= 140 or diastolic >= 90:
        return "high", True
    if systolic >= 120 or diastolic >= 80:
        return "elevated", False
    return "normal", False


category, needs_doctor = classify_blood_pressure(150, 95)
print(category, needs_doctor)  # high True
category, needs_doctor = classify_blood_pressure(118, 76)
print(category, needs_doctor)  # normal False


#functions calling functions
# Small single-purpose functions are combined into the real workflow.
def check_in(patient, weight_kg, height_cm, bp_text, on_medication=False):
    bp = parse_blood_pressure(bp_text)
    if bp is None:
        return f"{patient}: invalid blood pressure {bp_text!r}, please re-measure"

    bmi = calculate_bmi(weight_kg, height_cm / 100)
    category, needs_doctor = classify_blood_pressure(*bp)

    report = f"{patient}: BMI {bmi}, blood pressure {category}"
    if needs_doctor:
        report += " -> see a doctor today"
    if on_medication:
        report += " (check medication)"
    return report


print(check_in("Anna", 62, 168, "118/76"))
print(check_in("Petro", 95, 180, "150/95", on_medication=True))
print(check_in("Ivan", 80, 175, "12O/80"))
