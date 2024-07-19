import sys
print("Python executable:", sys.executable)

try:
    from dotenv import load_dotenv
    print("dotenv module is imported successfully!")
except ModuleNotFoundError:
    print("dotenv module is NOT found!")
