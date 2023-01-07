from typing import Any, Union

from ...client.api.domain.domain_get import sync_detailed
from ...client.client import Client
from ...client.models.domain_response import DomainResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch an Existing Domain"""

    def configure(self, parser):
        """Add arguments for domain_get"""
        parser.cli_argument(
            "domain_name",
            type=str,
            description="""The name of the domain to fetch.""",
        )

    def request(
        self,
        domain_name: str,
        client: Client,
    ) -> Union[Any, DomainResponse, ProblemDetails]:

        page_response = sync_detailed(
            domain_name=domain_name,
            client=client,
        )
        return page_response.status_code, page_response.parsed
