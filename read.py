import os

import dotenv
import requests


def exit_if_none(*args):
    for a in args:
        if a is None:
            os._exit(1)


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

    get_octopus_data(
        str(OCTOPUS_BASE_URL), str(OCTOPUS_API_KEY), str(OCTOPUS_ACCOUNT_ID)
    )


def get_octopus_data(base_url: str, key: str, account_id: str):
    url = f"{base_url}/accounts/{account_id}"
    r = requests.get(url, auth=(key, ""))
    print(r.json())


if __name__ == "__main__":
    main()
