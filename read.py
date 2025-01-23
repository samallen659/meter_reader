import os
from enum import Enum

import dotenv
import requests


def exit_if_none(*args):
    for a in args:
        if a is None:
            os._exit(1)


class Fuel(Enum):
    GAS = 1
    ELECTRICITY = 2


def main():
    dotenv.load_dotenv()

    OCTOPUS_BASE_URL = os.getenv("OCTOPUS_BASE_URL")
    OCTOPUS_API_KEY = os.getenv("OCTOPUS_API_KEY")
    OCTOPUS_ELC_MPAN = os.getenv("OCTOPUS_ELC_MPAN")
    OCTOPUS_ELC_SERIAL = os.getenv("OCTOPUS_ELC_SERIAL")
    OCTOPUS_GAS_MPRN = os.getenv("OCTOPUS_GAS_MPRN")
    OCTOPUS_GAS_SERIAL = os.getenv("OCTOPUS_GAS_SERIAL")
    OCTOPUS_ACCOUNT_ID = os.getenv("OCTOPUS_ACCOUNT_ID")

    exit_if_none(
        OCTOPUS_BASE_URL,
        OCTOPUS_API_KEY,
        OCTOPUS_ELC_MPAN,
        OCTOPUS_ELC_SERIAL,
        OCTOPUS_GAS_MPRN,
        OCTOPUS_GAS_SERIAL,
        OCTOPUS_ACCOUNT_ID,
    )

    # get_octopus_account(
    #     str(OCTOPUS_BASE_URL), str(OCTOPUS_API_KEY), str(OCTOPUS_ACCOUNT_ID)
    # )

    # get_octopus_meter_point(
    #     str(OCTOPUS_BASE_URL), str(OCTOPUS_API_KEY), str(OCTOPUS_ELC_MPAN)
    # )
    #
    # get_octopus_meter_consumption(
    #     str(OCTOPUS_BASE_URL),
    #     str(OCTOPUS_API_KEY),
    #     str(OCTOPUS_ELC_MPAN),
    #     str(OCTOPUS_ELC_SERIAL),
    #     Fuel.ELECTRICITY,
    # )
    get_octopus_meter_consumption(
        str(OCTOPUS_BASE_URL),
        str(OCTOPUS_API_KEY),
        str(OCTOPUS_GAS_MPRN),
        str(OCTOPUS_GAS_SERIAL),
        Fuel.GAS,
    )


def get_octopus_account(base_url: str, key: str, account_id: str):
    url = f"{base_url}/accounts/{account_id}"
    r = requests.get(url, auth=(key, ""))
    print(r.json())


def get_octopus_meter_point(base_url: str, key: str, mpan: str):
    url = f"{base_url}electricity-meter-points/{mpan}"
    r = requests.get(url, auth=(key, ""))
    print(r.json())


def get_octopus_meter_consumption(
    base_url: str, key: str, mpan: str, serial: str, fuel: Fuel
):
    print(fuel)
    url = f"{base_url}{"electricity" if fuel is Fuel.ELECTRICITY else "gas"}-meter-points/{mpan}/meters/{serial}/consumption"
    r = requests.get(url, auth=(key, ""))
    print(r.json())


if __name__ == "__main__":
    main()
