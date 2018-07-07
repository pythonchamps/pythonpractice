class MyException(Exception):
    def __init__(self):
        pass


try:
    x=10
    assert (x>10)
    raise MyException

except MyException:
    print("Handled My Exception")



