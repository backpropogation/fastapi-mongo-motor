from loguru import logger


def configure_logging():
    logger.add(
        "logs/main.log",
        format="{time:YYYY-MM-DD at HH:mm:ss} | {name} | {level} | {message}",
        rotation="1 week",
        level="DEBUG"
    )
