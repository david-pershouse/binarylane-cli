from typing import Union

from ...client.api.server.server_delete import sync
from ...client.client import Client
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_delete"

    @property
    def description(self):
        return """Cancel an Existing Server"""

    def configure(self, parser):
        """Add arguments for server_delete"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--reason",
            dest="reason",
            type=Union[Unset, None, str],
            required=False,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        reason: Union[Unset, None, str] = UNSET,
    ):
        return sync(
            server_id=server_id,
            client=client,
            reason=reason,
        )