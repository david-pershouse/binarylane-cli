from typing import List, Union

from ... import cli
from ...client.api.load_balancer.load_balancer_update import sync
from ...client.client import Client
from ...client.models.algorithm_type import AlgorithmType
from ...client.models.forwarding_rule import ForwardingRule
from ...client.models.health_check import HealthCheck
from ...client.models.sticky_sessions import StickySessions
from ...client.models.update_load_balancer_request import UpdateLoadBalancerRequest
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "load-balancer_update"

    @property
    def description(self):
        return """Update an Existing Load Balancer"""

    def configure(self, parser):
        """Add arguments for load-balancer_update"""
        parser.cli_argument(
            "load_balancer_id",
        )

        parser.cli_argument(
            "--name",
            dest="name",
            type=str,
            required=True,
            description="""The hostname of the load balancer.""",
        )

        parser.cli_argument(
            "--algorithm",
            dest="algorithm",
            type=Union[Unset, None, AlgorithmType],
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| round_robin | Each request will be sent to one of the nominated servers in turn. |
| least_connections | Each request will be sent to the server with the least existing connections. This option is not currently supported. |

""",
        )

        parser.cli_argument(
            "--forwarding-rules",
            dest="forwarding_rules",
            type=Union[Unset, None, List[ForwardingRule]],
            required=False,
            description="""The rules that control which traffic the load balancer will forward to servers in the pool. Leave null to accept a default "HTTP" only forwarding rule.""",
        )

        parser.cli_argument(
            "--health-check",
            dest="health_check",
            type=Union[Unset, None, HealthCheck],
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--sticky-sessions",
            dest="sticky_sessions",
            type=Union[Unset, None, StickySessions],
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--redirect-http-to-https",
            dest="redirect_http_to_https",
            type=Union[Unset, None, bool],
            required=False,
            description="""Redirect HTTP traffic received by the load balancer to HTTPS. This is not currently supported.""",
            action=cli.BooleanOptionalAction,
        )

        parser.cli_argument(
            "--enable-proxy-protocol",
            dest="enable_proxy_protocol",
            type=Union[Unset, None, bool],
            required=False,
            description="""Enable the PROXY protocol on the load balancer. This is not currently supported.""",
            action=cli.BooleanOptionalAction,
        )

        parser.cli_argument(
            "--enable-backend-keepalive",
            dest="enable_backend_keepalive",
            type=Union[Unset, None, bool],
            required=False,
            description="""Use HTTP keepalive connections to servers in the load balancer pool. This is not currently supported.""",
            action=cli.BooleanOptionalAction,
        )

        parser.cli_argument(
            "--server-ids",
            dest="server_ids",
            type=Union[Unset, None, List[int]],
            required=False,
            description="""A list of server IDs to assign to this load balancer. This is mutually exclusive with 'tag'.""",
        )

        parser.cli_argument(
            "--tag",
            dest="tag",
            type=Union[Unset, None, str],
            required=False,
            description="""Tags are not currently supported and attempting to add servers by tag will add no servers. This is mutually exclusive with 'server_ids'.""",
        )

    def request(
        self,
        load_balancer_id: int,
        client: Client,
        name: str,
        algorithm: Union[Unset, None, AlgorithmType] = UNSET,
        forwarding_rules: Union[Unset, None, List[ForwardingRule]] = UNSET,
        health_check: Union[Unset, None, HealthCheck] = UNSET,
        sticky_sessions: Union[Unset, None, StickySessions] = UNSET,
        redirect_http_to_https: Union[Unset, None, bool] = UNSET,
        enable_proxy_protocol: Union[Unset, None, bool] = UNSET,
        enable_backend_keepalive: Union[Unset, None, bool] = UNSET,
        server_ids: Union[Unset, None, List[int]] = UNSET,
        tag: Union[Unset, None, str] = UNSET,
    ):
        return sync(
            load_balancer_id=load_balancer_id,
            client=client,
            json_body=UpdateLoadBalancerRequest(
                name=name,
                algorithm=algorithm,
                forwarding_rules=forwarding_rules,
                health_check=health_check,
                sticky_sessions=sticky_sessions,
                redirect_http_to_https=redirect_http_to_https,
                enable_proxy_protocol=enable_proxy_protocol,
                enable_backend_keepalive=enable_backend_keepalive,
                server_ids=server_ids,
                tag=tag,
            ),
        )