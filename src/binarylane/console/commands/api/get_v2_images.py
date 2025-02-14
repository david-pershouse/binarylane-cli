from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from binarylane.api.images.get_v2_images import sync_detailed
from binarylane.models.image_query_type import ImageQueryType
from binarylane.models.images_response import ImagesResponse
from binarylane.models.links import Links
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    type: Union[Unset, None, ImageQueryType] = UNSET
    private: Union[Unset, None, bool] = UNSET


class Command(ListRunner):
    def response(self, status_code: int, received: Any) -> None:
        if not isinstance(received, ImagesResponse):
            return super().response(status_code, received)

        return self._printer.print(received.images, self._format)

    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "slug",
            "distribution",
            "name",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this image.""",
            "name": """If this is an operating system image, this is the name of the operating system version. If this is a backup image, this is the label of the backup if it exists, otherwise it is the UTC timestamp of the creation of the image.""",
            "type": """
| Value | Description |
| ----- | ----------- |
| custom | An image uploaded by a user. |
| snapshot | A snapshot. Snapshot creation is not currently supported so only distribution images will have this value. |
| backup | A backup of a server. |

""",
            "public": """A public image is available to all users. A private image is available only to the account that created the image.""",
            "regions": """The slugs of the regions where the image is available for use.""",
            "min_disk_size": """For a distribution image this is the minimum disk size in GB required to install the operating system. For a backup image this is the minimum total disk size in GB required to restore the backup.""",
            "size_gigabytes": """For a distribution image this is the disk size used in GB by the operating system on initial install. For a backup image this is the size of the compressed backup image in GB.""",
            "status": """
| Value | Description |
| ----- | ----------- |
| NEW | The image is new. |
| available | The image is available for use. |
| pending | The image is pending and is not yet available for use. |
| deleted | The image has been deleted and is no longer available for use. |

""",
            "distribution_info": """This object may provide further information about the distribution.""",
            "distribution": """If this is an operating system image, this is the name of the distribution. If this is a backup image, this is the name of the distribution the server is using.""",
            "full_name": """If this is an operating system image, this is the name and version of the distribution. If this is a backup image, this is the server hostname and label of the backup if it exists, otherwise it is the server hostname and UTC timestamp of the creation of the image.""",
            "slug": """If this is an operating system image this is a slug which may be used as an alternative to the ID as a reference.""",
            "created_at": """If this is a backup image this is the date and time in ISO8601 format when the image was created.""",
            "description": """A description that may provide further details or warnings about the image.""",
            "error_message": """If the image creation failed this may provide further information.""",
            "min_memory_megabytes": """This is minimum memory in MB necessary to support this operating system (or the base operating system for a backup image).""",
            "distribution_surcharges": """If this is not null the use of this image may incur surcharges above the base cost of the server. All costs are in AU$.""",
            "backup_info": """If this image is a backup, this object will provide further information.""",
        }

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Images/paths/~1v2~1images/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add(
            PrimitiveAttribute(
                "type",
                Union[Unset, None, ImageQueryType],
                required=False,
                option_name="type",
                description="""Queries for distribution will include images that have pre-installed applications.""",
            )
        )
        mapping.add(
            PrimitiveAttribute(
                "private",
                Union[Unset, None, bool],
                required=False,
                option_name="private",
                description="""Provide 'true' to only list private images. 'false' has no effect.""",
            )
        )
        return mapping

    @property
    def ok_response_type(self) -> type:
        return ImagesResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ImagesResponse, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ImagesResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[ImagesResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                type=request.type,
                private=request.private,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, ImagesResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.images += page_response.parsed.images

        return status_code, response
