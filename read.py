import os

import dotenv
import httpx


def main():
    dotenv.load_dotenv()

    OCTOPUS_BASE_URL = os.getenv("OCTOPUS_BASE_URL")
    if OCTOPUS_BASE_URL is None:
        os._exit(1)

    print(OCTOPUS_BASE_URL)

    r = httpx.get(OCTOPUS_BASE_URL)
    print(r)


if __name__ == "__main__":
    main()
