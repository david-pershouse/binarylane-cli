from ... import cli
from ...client.api.server_action.server_action_change_ipv6 import sync
from ...client.client import Client
from ...client.models.change_ipv_6 import ChangeIpv6
from ...client.models.change_ipv_6_type import ChangeIpv6Type
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_change-ipv6"

    @property
    def description(self):
        return """Enable or Disable IPv6 for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-ipv6"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeIpv6Type,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--enabled",
            dest="enabled",
            type=bool,
            required=True,
            description="""None""",
            action=cli.BooleanOptionalAction,
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeIpv6Type,
        enabled: bool,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=ChangeIpv6(
                type=type,
                enabled=enabled,
            ),
        )