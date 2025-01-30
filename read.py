import logging
import os
import sys
from datetime import datetime, timedelta

import dotenv
import requests

from models import ConsumptionResponse, Fuel
from utils import exit_if_none


def main():
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(message)s",
    )
    logger = logging.getLogger()

    logger.info("Loading environment variables")
    dotenv.load_dotenv()

    OCTOPUS_BASE_URL = os.getenv("OCTOPUS_BASE_URL")
    OCTOPUS_API_KEY = os.getenv("OCTOPUS_API_KEY")
    OCTOPUS_ELC_MPAN = os.getenv("OCTOPUS_ELC_MPAN")
    OCTOPUS_ELC_SERIAL = os.getenv("OCTOPUS_ELC_SERIAL")
    OCTOPUS_GAS_MPRN = os.getenv("OCTOPUS_GAS_MPRN")
    OCTOPUS_GAS_SERIAL = os.getenv("OCTOPUS_GAS_SERIAL")
    OCTOPUS_ACCOUNT_ID = os.getenv("OCTOPUS_ACCOUNT_ID")

    exit_if_none(
        logger,
        OCTOPUS_BASE_URL=OCTOPUS_BASE_URL,
        OCTOPUS_API_KEY=OCTOPUS_API_KEY,
        OCTOPUS_ELC_MPAN=OCTOPUS_ELC_MPAN,
        OCTOPUS_ELC_SERIAL=OCTOPUS_ELC_SERIAL,
        OCTOPUS_GAS_MPRN=OCTOPUS_GAS_MPRN,
        OCTOPUS_GAS_SERIAL=OCTOPUS_GAS_SERIAL,
        OCTOPUS_ACCOUNT_ID=OCTOPUS_ACCOUNT_ID,
    )


def get_octopus_account(base_url: str, key: str, account_id: str):
    url = f"{base_url}/accounts/{account_id}"
    r = requests.get(url, auth=(key, ""))
    print(r.json())


def get_octopus_meter_point(base_url: str, key: str, mpan: str):
    url = f"{base_url}electricity-meter-points/{mpan}"
    r = requests.get(url, auth=(key, ""))
    print(r.json())


def get_yesterdays_octopus_meter_consumption(
    base_url: str, key: str, mpan: str, serial: str, fuel: Fuel
):
    yesterday = datetime.today() - timedelta(days=1)
    get_dates_octopus_meter_consumption(base_url, key, mpan, serial, fuel, yesterday)


def get_dates_octopus_meter_consumption(
    base_url: str, key: str, mpan: str, serial: str, fuel: Fuel, date: datetime
) -> ConsumptionResponse:
    start_time = f"{date.strftime("%Y-%m-%d")}T00:00:00Z"
    end_time = f"{date.strftime("%Y-%m-%d")}T23:30:00Z"
    url = f"{base_url}{"electricity" if fuel is Fuel.ELECTRICITY else "gas"}-meter-points/{mpan}/meters/{serial}/consumption?period_from={start_time}&period_to={end_time}"
    r = requests.get(url, auth=(key, ""))
    data = ConsumptionResponse(**r.json())
    return data


if __name__ == "__main__":
    main()
