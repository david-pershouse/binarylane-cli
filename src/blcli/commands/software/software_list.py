from typing import Union

from ...client.api.software.software_list import sync
from ...client.client import Client
from ...client.types import Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "software_list"

    @property
    def description(self):
        return """List All Available Software"""

    def configure(self, parser):
        """Add arguments for software_list"""

        parser.cli_argument(
            "--page",
            dest="page",
            type=Union[Unset, None, int],
            required=False,
            description="""The selected page. Page numbering starts at 1""",
        )
        parser.cli_argument(
            "--per-page",
            dest="per_page",
            type=Union[Unset, None, int],
            required=False,
            description="""The number of results to show per page.""",
        )

    def request(
        self,
        client: Client,
        page: Union[Unset, None, int] = 1,
        per_page: Union[Unset, None, int] = 20,
    ):
        return sync(
            client=client,
            page=page,
            per_page=per_page,
        )