import logging

def con_logging():
    logging.basicConfig(
            level=logging.INFO,
            format= "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
            filename="logs_con_logging.log",
            encoding='utf-8'
        )
