import logging

def setup_logger(file_name):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=file_name
    )
    return logging.getLogger()
