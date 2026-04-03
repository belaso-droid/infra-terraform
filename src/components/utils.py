import os
import json
import logging
from typing import Dict, List

class Utils:
    @staticmethod
    def get_logger(name: str, level: str = 'DEBUG') -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, level))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_file_handler = logging.FileHandler('log.log')
        log_file_handler.setFormatter(formatter)
        logger.addHandler(log_file_handler)
        return logger

    @staticmethod
    def load_json(file_path: str) -> Dict:
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_json(file_path: str, data: Dict) -> None:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def get_file_list(directory: str) -> List[str]:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    @staticmethod
    def get_dir_list(directory: str) -> List[str]:
        return [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]