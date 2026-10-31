import os

from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    print(os.environ.get("GOOGLE_API_KEY"))


main()
