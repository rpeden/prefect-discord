from prefect import flow

from prefect_discord.tasks import (
    goodbye_prefect_discord,
    hello_prefect_discord,
)


def test_hello_prefect_discord():
    @flow
    def test_flow():
        return hello_prefect_discord()

    result = test_flow()
    assert result == "Hello, prefect-discord!"


def goodbye_hello_prefect_discord():
    @flow
    def test_flow():
        return goodbye_prefect_discord()

    result = test_flow()
    assert result == "Goodbye, prefect-discord!"
