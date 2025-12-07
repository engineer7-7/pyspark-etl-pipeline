import os


def set_up_env():
    os.environ["PYSPARK_PYTHON"] = r"C:\Users\NIKOLA~1\Desktop\data_engineer_udemy_codes\.venv\Scripts\python.exe"
    os.environ[
        "PYSPARK_DRIVER_PYTHON"] = r"C:\Users\NIKOLA~1\Desktop\data_engineer_udemy_codes\.venv\Scripts\python.exe"

    return os.environ['PYSPARK_PYTHON'], os.environ["PYSPARK_DRIVER_PYTHON"]
