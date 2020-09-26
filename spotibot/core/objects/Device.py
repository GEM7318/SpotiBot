import json
from spotibot.mongo.utils.Handlers import object_handler, get_serializable


class Device:
    """Auto-generated attribute instantiation docstring for Device
    Object

    Note: Parameter description in below docstring is populated based
    on the  descriptions at the following link:
    https://developer.spotify.com/documentation/web-
    api/reference/object-model

    Please consult their official documentation for more in-depth
    information & full-linking across pages.

    Attributes:
        id (str): The device ID. This may be null.
        is_active (bool): If this device is the currently active device.
        is_private_session (bool): If this device is currently in a
            private session.
        is_restricted (bool): Whether controlling this device is
            restricted.  At present if this is true then no Web API
            commands will be accepted by this device.
        name (str): The name of the device.
        type (str): Device type, such as Computer, Smartphone or
            Speaker.
        volume_percent (int): The current volume in percent.  This may
            be null.
    """

    def __init__(self, device: dict):
        self.id: str = object_handler(device, "id")

        # self.id.accepted_values = \
        #     [None, 'Computer', 'Speaker', 'Smartphone']

        self.is_active: bool = object_handler(device, "is_active")

        self.is_private_session: bool = object_handler(device, "is_private_session")

        self.is_restricted: bool = object_handler(device, "is_restricted")

        self.name: str = object_handler(device, "name")

        self.type: str = object_handler(device, "type")

        self.volume_percent: int = object_handler(device, "volume_percent")

    # def validate(self):
    #     validation_dict = {}
    #     for k, v in vars(self).items():
    #         sub = {
    #             'type': type(v),
    #             'null_possible': False,
    #             'accepted_vals': []
    #         }
    #         validation_dict[k] = sub
    #     return validation_dict
    def __eq__(self, other) -> bool:
        """Equality comparison to other objects.

        Args:
            other: Comparison object

        Returns:
            Boolean value indicating whether or not the attributes and their
            associated values are equal between the two objects
        """
        return vars(self) == vars(other)

    def __getitem__(self, item: str):
        """Getter method for subscriptability.

        Args:
            item: Attribute to get the value of

        Returns:
            Attribute value if exists in object's namespace
        """
        return getattr(self, item)

    def get(self, item: str, default=None):
        """Method for extracting attributes without throwing existence errors.

        Args:
            item: Attribute to get the value of
            default: Return value if attribute doesn't exist

        Returns:
            Attribute value or default if attribute does not exist
        """
        return vars(self).get(item, default)

    def to_dict(self) -> dict:
        """Calling utility serialization method on all attributes.

        Returns:
            String following valid json structure for mongo serialization.
        """
        return {k: get_serializable(v) for k, v in vars(self).items()}

    @property
    def json(self) -> str:
        """Jsonified/string attribute for all SpotiBot objects for mongo
        serialization purposes

        Returns:
            Serializable 'json' output of SpotiBot object
        """
        return json.dumps(self.to_dict())
