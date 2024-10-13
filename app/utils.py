from logging import getLogger, getLogger, handlers, Formatter, DEBUG


def get_logger():
    logger = getLogger(__name__)
    logger.setLevel("DEBUG")
    rotating_handler = handlers.RotatingFileHandler(
        r"./logs/app.log",
        mode="a",
        maxBytes=100 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    logger.addHandler(rotating_handler)
    return logger
