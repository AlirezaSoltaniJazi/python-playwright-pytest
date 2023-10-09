from os import path
from os.path import pardir

from utils.logger_formatter import LOGGER


def get_project_directory() -> str:
    """
    This function trys to find the project root
    :return: project directory
    """
    test_dir = path.dirname(path.abspath(__file__))
    LOGGER.info('test_dir: %s', test_dir)
    project_dir = path.abspath(path.join(test_dir, pardir))
    LOGGER.info('project_dir: %s', project_dir)
    return project_dir
