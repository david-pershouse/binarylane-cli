from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server.server_neighbors_list import sync_detailed
from binarylane.client import Client
from binarylane.models.neighbors_response import NeighborsResponse

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "list"

    @property
    def description(self):
        return """List All Servers That Share a Host"""

    def configure(self, parser):
        """Add arguments for server_neighbors_list"""

    @property
    def ok_response_type(self) -> Type:
        return NeighborsResponse

    def request(
        self,
        client: Client,
    ) -> Union[Any, NeighborsResponse]:

        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed