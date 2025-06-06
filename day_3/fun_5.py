def connect(**opcje):  # dowolna ilośc argumentów nazwanych
    print(opcje)


connect()  # {}
connect(a=6)  # {'a': 6}


def all_args(*args, **kwargs):
    print(f"{args=}")
    print(f"{kwargs=}")


all_args(1, 2, 3)  # args=(1, 2, 3)
all_args(a=2, b=5, c=9)  # kwargs={'a': 2, 'b': 5, 'c': 9}
