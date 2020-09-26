
import json
from spotibot.mongo.utils.Handlers import object_handler, get_serializable


class Timestamp:

    def __init__(self, raw, base='seconds'):

        self.raw = raw
        self.base = base

        if base == 'seconds':
            self.adj_ms = 1_000
            self.adj_ns = 1_000_000_000
            self.adj_sec = (1 / 1)

        elif base == 'milliseconds':
            self.adj_ms = (1 / 1)
            self.adj_ns = 1_000_000
            self.adj_sec = (1 / 1_000)

        elif base == 'nanoseconds':
            self.adj_ms = (1 / 1_000_000)
            self.adj_ns = (1 / 1)
            self.adj_sec = (1 / 1_000_000_000)

        self.seconds: int = \
            int(self.adj_sec * self.raw)

        self.milliseconds: int = \
            int(self.adj_ms * self.raw)

        self.nanoseconds: int = \
            int(self.adj_ns * self.raw)

        self.minutes: int = \
            int(self.seconds / 60)

        self.is_positive: bool = \
            self.raw > 0

        self.is_negative: bool = \
            self.raw < 0

        self.is_zero: bool = \
            self.raw == 0

    def __int__(self):
        return int(self.raw)

    def __add__(self, other):
        other_secs = other.seconds
        total_secs = self.seconds + other_secs
        return Timestamp(total_secs, base='seconds')

    def __sub__(self, other):
        other_secs = other.seconds
        total_secs = self.seconds - other_secs
        return Timestamp(total_secs, base='seconds')

    def __lt__(self, other) -> bool:
        return self.seconds < other.seconds

    def __gt__(self, other) -> bool:
        return self.seconds > other.seconds

    def __eq__(self, other) -> bool:
        return self.seconds == other.seconds

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
