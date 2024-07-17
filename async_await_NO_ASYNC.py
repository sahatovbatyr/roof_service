import time


def make_request(count):
    print("making DB request", count)
    time.sleep(0.1)

for i in range(10_000):
    make_request(i)
