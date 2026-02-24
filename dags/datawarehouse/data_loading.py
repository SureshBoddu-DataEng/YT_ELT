import json
from datetime import date
import logging

logger = logging.getLogger(__name__)

def load_data():
    file_path = f"./data/YT_Data_{date.today()}.json"
    data = {}
    try:
        logger.info(f"Processing file: YT_Data_{date.today()}.json")

        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        return data
    except FileNotFoundError as e:
        logger.error(f"File not found: YT_Data_{date.today()}.json", e)
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid json: YT_Data_{date.today()}.json", e)
        raise