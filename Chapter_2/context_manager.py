def read_file(filename: str) -> None:
    """

    Parameters
    ----------
    filename :

    Returns
    -------

    """

    def process_file(fd):
        print(f'read file {fd}')

    # basically way
    # fd = open(filename)
    # try:
    #     process_file(fd)
    # finally:
    #     fd.close()

    # musthave way
    #
    # Context managers consist of two magic methods: __enter__ and __exit__.
    #
    with open(filename) as fd:
        process_file(fd)


# SELF CONTEXT MANAGER:

def run(param):
    print(param)


def stop_database():
    run("systemctl stop postgresql.service")


def start_database():
    run("systemctl start postgresql.service")


class DBHandler:

    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        start_database()


def db_backup():
    run("pg_dump database")
    # raise BaseException('ERROR during backup')


def main():
    with DBHandler():
        db_backup()


# The contextlib module contains a lot of helper functions and objects to either implement
# context managers or use some already provided ones that can help us write more compact
# code


import contextlib


@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    stop_database()

#
# with db_handler():
#     db_backup()



# SELF DECORATOR, MORE POWERFUL


class dbhandler_decorator(contextlib.ContextDecorator):

    def __enter__(self):
        stop_database()


    def __exit__(self, exc_type, exc_val, exc_tb):
        start_database()

    def __repr__(self):
        return 'Something that you need'

@dbhandler_decorator()
def offline_backup():
    db_backup()

# !!!! but
# with offline_backup() as bk:
#     print(bk)
# not working in this case