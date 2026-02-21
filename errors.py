print("TRY EXCEPTION:\n")

try:
    int("abc")
except ValueError as e:
    print("Exception:", e)
try:
    int("abc")
except Exception as e:
    print("Default Exception:", e)
finally:
    print("Finally executed")
