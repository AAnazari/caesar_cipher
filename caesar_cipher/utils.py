#Ensures the shift value is an Integer and also is between 0 and 25.
def validate_shift(shift):
    if not isinstance(shift, int):
        raise ValueError("Shift must be an integer.")
    if shift < 0 or shift > 25:
        raise ValueError("Shift must be between 0 and 25.")
    return shift
