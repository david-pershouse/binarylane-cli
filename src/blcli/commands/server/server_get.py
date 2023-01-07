from typing import Any, Union

from ...client.api.server.server_get import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.server_response import ServerResponse
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch an Existing Server"""

    def configure(self, parser):
        """Add arguments for server_get"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server to fetch.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails, ServerResponse]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
