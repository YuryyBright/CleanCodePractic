from functools import wraps
from threading import Thread
from venv import logger


class ControlledException(Exception):
    """A generic exception on the program's domain."""


def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):

        last_raised = None

        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return operation(*args, **kwargs)
            except ControlledException as e:
                logger.info("retrying %s", operation.__qualname__)
                last_raised = e
        raise last_raised

    return wrapped


@retry
def run_operation(task):
    """Run a particular task, simulating some failures on its execution."""
    return task.run()
