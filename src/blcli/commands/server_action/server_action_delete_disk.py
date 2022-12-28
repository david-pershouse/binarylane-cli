from ...client.api.server_action.server_action_delete_disk import sync
from ...client.client import Client
from ...client.models.delete_disk import DeleteDisk
from ...client.models.delete_disk_type import DeleteDiskType
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_delete-disk"

    @property
    def description(self):
        return """Delete an Additional Disk for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_delete-disk"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=DeleteDiskType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--disk-id",
            dest="disk_id",
            type=str,
            required=True,
            description="""The ID of the existing disk. See server.disks for a list of IDs.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: DeleteDiskType,
        disk_id: str,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=DeleteDisk(
                type=type,
                disk_id=disk_id,
            ),
        )