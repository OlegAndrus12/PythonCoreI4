import tempfile
import os
from contextlib import contextmanager

@contextmanager
def create_temporary_file(suffix=".txt", mode="r"):
    fd, path = tempfile.mkstemp(suffix=suffix)
    os.close(fd)
    try:
        with open(path, mode) as f:
            yield f
    finally:
        if os.path.exists(path):
            os.remove(path)


with create_temporary_file(mode="w+") as file:
    file.write("Hello world!!")
    file.seek(0)
    file.read()
    print("Sending file to the cloud")


print("Extra stuff")

        


