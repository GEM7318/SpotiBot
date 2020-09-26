import time
import requests
import json

from spotibot.core.objects import Time as spottime, User as user

from spotibot.core.utils import Hasher as hasher

from spotibot.mongo.utils.Handlers import get_serializable

# TODO: Need to have something here that indicates downstream actions to not
#  even attempt to execute if it returns nothing/playback has gone dormant
# class Response:
#
#     def __init__(self, response):
#
#         self.ok: bool = response.ok
#
#         self.status_code: int = response.status_code
#
#         if self.ok and self.status_code == 200:
#             self.result: dict = response.json()
#         else:
#             self.result: dict = {}
#
#     def __eq__(self, other) -> bool:
#         """Equality comparison to other objects.
#
#         Args:
#             other: Comparison object
#
#         Returns:
#             Boolean value indicating whether or not the attributes and their
#             associated values are equal between the two objects
#         """
#         return vars(self) == vars(other)
#
#     def __getitem__(self, item: str):
#         """Getter method for subscriptability.
#
#         Args:
#             item: Attribute to get the value of
#
#         Returns:
#             Attribute value if exists in object's namespace
#         """
#         return getattr(self, item)
#
#     def get(self, item: str, default=None):
#         """Method for extracting attributes without throwing existence errors.
#
#         Args:
#             item: Attribute to get the value of
#             default: Return value if attribute doesn't exist
#
#         Returns:
#             Attribute value or default if attribute does not exist
#         """
#         return vars(self).get(item, default)
#
#     def to_dict(self) -> dict:
#         """Calling utility serialization method on all attributes.
#
#         Returns:
#             String following valid json structure for mongo serialization.
#         """
#         return {k: get_serializable(v) for k, v in vars(self).items()}
#
#     @property
#     def json(self) -> str:
#         """Jsonified/string attribute for all SpotiBot objects for mongo
#         serialization purposes
#
#         Returns:
#             Serializable 'json' output of SpotiBot object
#         """
#         return json.dumps(self.to_dict())
#
#
# # class Request(user.UserDBO):
# class Request:
#
#     def __init__(self, headers):
#
#         self.headers = headers
#
#         # --------------------------/Request Detail/---------------------------
#
#     def http_get(self, href):
#
#         self.unix_request_tmstmp: spottime.Timestamp = \
#             spottime.Timestamp(time.time(), base='seconds')
#
#         self.response = \
#             Response(requests.get(href, headers=self.headers))
#
#         self.endpoint_id: str = \
#             hasher.quick_hash(
#                 f"{href}{self.unix_request_tmstmp}")
#
#         return self
#
#     def __eq__(self, other) -> bool:
#         """Equality comparison to other objects.
#
#         Args:
#             other: Comparison object
#
#         Returns:
#             Boolean value indicating whether or not the attributes and their
#             associated values are equal between the two objects
#         """
#         return vars(self) == vars(other)
#
#     def __getitem__(self, item: str):
#         """Getter method for subscriptability.
#
#         Args:
#             item: Attribute to get the value of
#
#         Returns:
#             Attribute value if exists in object's namespace
#         """
#         return getattr(self, item)
#
#     def get(self, item: str, default=None):
#         """Method for extracting attributes without throwing existence errors.
#
#         Args:
#             item: Attribute to get the value of
#             default: Return value if attribute doesn't exist
#
#         Returns:
#             Attribute value or default if attribute does not exist
#         """
#         return vars(self).get(item, default)
#
#     def to_dict(self) -> dict:
#         """Calling utility serialization method on all attributes.
#
#         Returns:
#             String following valid json structure for mongo serialization.
#         """
#         return {k: get_serializable(v) for k, v in vars(self).items()}
#
#     @property
#     def json(self) -> str:
#         """Jsonified/string attribute for all SpotiBot objects for mongo
#         serialization purposes
#
#         Returns:
#             Serializable 'json' output of SpotiBot object
#         """
#         return json.dumps(self.to_dict())
