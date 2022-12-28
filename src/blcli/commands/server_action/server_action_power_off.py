from ...client.api.server_action.server_action_power_off import sync
from ...client.client import Client
from ...client.models.power_off import PowerOff
from ...client.models.power_off_type import PowerOffType
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_power-off"

    @property
    def description(self):
        return """Power a Server Off"""

    def configure(self, parser):
        """Add arguments for server-action_power-off"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=PowerOffType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: PowerOffType,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=PowerOff(
                type=type,
            ),
        )