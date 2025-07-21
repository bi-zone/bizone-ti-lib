import logging


def init_logging() -> None:
    log = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)

    log.setLevel(logging.INFO)
    log.addHandler(handler)
