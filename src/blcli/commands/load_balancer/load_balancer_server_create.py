from typing import Any, List, Union

from ...client.api.load_balancer.load_balancer_server_create import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.server_ids_request import ServerIdsRequest
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "create"

    @property
    def description(self):
        return """Add Servers to an Existing Load Balancer"""

    def configure(self, parser):
        """Add arguments for load-balancer_server_create"""
        parser.cli_argument(
            "load_balancer_id",
            type=int,
            description="""The ID of the load balancer to which servers should be added.""",
        )

        parser.cli_argument(
            "--server-ids",
            dest="server_ids",
            type=List[int],
            required=True,
            description="""A list of server IDs.""",
        )

    def request(
        self,
        load_balancer_id: int,
        client: Client,
        server_ids: List[int],
    ) -> Union[Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
            json_body=ServerIdsRequest(
                server_ids=server_ids,
            ),
        )
        return page_response.status_code, page_response.parsed
