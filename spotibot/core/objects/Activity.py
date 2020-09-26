# !/usr/bin/env python
# coding: utf-8

import json
import sys
import os
from typing import Generator
import time
import requests

from mongoengine import *

project_dir = r"/home/gem7318/Github/SpotiBot"
sys.path.append(project_dir)
os.chdir(project_dir)

from spotibot.mongo.conn import Connector

from spotibot.core.objects import (
    Music as music,
    Podcasts as podcast,
    User as user,
    Context as context,
    Device as device,
    Time as spottime,
)

from spotibot.core.utils import Hasher

from spotibot.mongo.utils.Handlers import get_serializable

from spotibot.mongo.core.objects import Activity as ActivityDoc


class Request:
    def __init__(self, href, headers):

        # :: Request Detail ---------------------------------------------------
        self.unix_request_tmstmp: spottime.Timestamp = spottime.Timestamp(
            time.time(), base="seconds"
        )

        response = requests.get(href, headers=headers)

        self.ok: bool = response.ok

        self.status_code: int = response.status_code

        if self.ok and self.status_code == 200:
            self.result: dict = response.json()
        else:
            self.result: dict = {}

        self.endpoint_id: str = Hasher.quick_hash(f"{href}{self.unix_request_tmstmp}")

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


class Current(Request):
    def __init__(self, user_id, headers, href):
        super().__init__(href, headers)

        self.user_id = user_id

        self.href = href

        # :: Track or Show Instantiation --------------------------------------
        if self.result.get("currently_playing_type") == "track":

            self.playback: music.Track = music.Track(self.result.get("item"))

        elif self.result.get("currently_playing_type") == "episode":

            self.playback: podcast.Episode = podcast.Episode(self.result.get("item"))

        else:

            self.playback = None

        if self.playback:
            # :: Context ------------------------------------------------------
            self.context: context.Context = context.Context(self.result.get("context"))

            # :: Device -------------------------------------------------------
            self.device: list = [device.Device(self.result.get("device"))]

            # :: Freestanding Contextual Playback Information -----------------
            self.currently_playing_type = self.result.get("currently_playing_type")

            self.shuffle_state = self.result.get("shuffle_state")

            self.repeat_state = self.result.get("repeat_state")

            self.actions = self.result.get("actions")

            self.is_playing = self.result.get("is_playing")

            # :: Numeric Contextual Playback Information ----------------------
            self.progress = spottime.Timestamp(
                self.result.get("progress_ms"), base="milliseconds"
            )

            self.unix_request_tmstmp = self.unix_request_tmstmp

            self.unix_refresh_tmstmp = spottime.Timestamp(
                self.result.get("timestamp"), base="milliseconds"
            )

            # :: Newly Formatted Playback Information -------------------------
            self.time_remaining = self.playback.duration.__sub__(self.progress)

            self.unix_start_tmstmp = self.unix_request_tmstmp.__sub__(self.progress)

            self.unix_expected_end_tmstmp = self.unix_request_tmstmp.__add__(
                self.time_remaining
            )

            # :: Current Specific Attributes ----------------------------------
            self._time_listened: spottime.Timestamp = self.progress

            self.activity_id = Hasher.quick_hash(
                f"{self.playback.id}"
                f"-{self.unix_start_tmstmp.seconds}"
                f"-{self.user_id}"
            )

            self._id = f"{self.user_id}~{self.unix_request_tmstmp.seconds}~v1"

            self._request_cnt: int = 1

    def now(self, headers):
        return Current(headers=headers, user_id=self.user_id, href=self.href)

    @property
    def time_listened(self):
        return self._time_listened

    @time_listened.setter
    def time_listened(self, time_listened: spottime.Timestamp):
        self._time_listened = time_listened

    @property
    def request_cnt(self):
        return self._request_cnt

    @request_cnt.setter
    def request_cnt(self, prior=1):
        self._request_cnt = self._request_cnt + prior

    # @property
    # def uid(self):
    #     return self._id
    #
    # @uid.setter
    # def uid(self, uid: str):
    #     self._id = uid

    # def __copy__(self):
    #     return self.__copy__()

    def __repr__(self):
        return f"Current('{self.user_id}')"

    def __str__(self):
        return f"'Current' Object for UserDBO: {self.user_id}"

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

    def pop(self, item):
        return vars(self).pop(item)


class Delta:
    def __init__(self, latest: Current, prior: Current):

        # :: Comparison (numeric) ---------------------------------------------
        self.progress: spottime.Timestamp = latest.progress - prior.progress

        self.duration: spottime.Timestamp = latest.playback.duration - prior.playback.duration

        self.time_remaining: spottime.Timestamp = latest.time_remaining - prior.time_remaining

        self.unix_start_tmstmp: spottime.Timestamp = latest.unix_start_tmstmp - prior.unix_start_tmstmp

        self.unix_request_tmstmp: spottime.Timestamp = latest.unix_request_tmstmp - prior.unix_request_tmstmp

        self.unix_refresh_tmstmp: spottime.Timestamp = latest.unix_refresh_tmstmp - prior.unix_refresh_tmstmp

        self.prior_request_to_latest_start: spottime.Timestamp = latest.unix_start_tmstmp - prior.unix_request_tmstmp

        self.progress_exceeds_request: bool = latest.progress > self.unix_request_tmstmp
        # __________________________________________________________________ ::

        # :: Comparison (boolean) ---------------------------------------------
        self.is_same_type: bool = isinstance(latest.playback, type(prior.playback))

        self.is_same_id: bool = latest.playback.id == prior.playback.id

        self.is_same_device: bool = latest.device[0].name == prior.device[0].name

        if (
            not self.is_same_id
            and latest.unix_start_tmstmp < prior.unix_expected_end_tmstmp
        ):

            self.cutoff_prior: bool = True

        else:

            self.cutoff_prior: bool = False
        # __________________________________________________________________ ::

        # :: 'Current ID' Decision Tree ---------------------------------------
        self.activity5 = (
            self.progress_exceeds_request,
            {
                True: (False, False, "Rewound track"),
                False: (False, True, "Restarted Track"),
            },
        )

        self.activity4 = (
            self.progress.is_zero,
            {
                True: (False, False, "Playback paused"),
                False: (True, None, self.activity5),
            },
        )

        self.activity3 = (
            self.progress.is_positive,
            {
                True: (False, False, "Continued playback"),
                False: (True, None, self.activity4),
            },
        )

        self.activity2 = (
            self.is_same_id,
            {
                True: (True, None, self.activity3),
                False: (False, True, "New activity instance started"),
            },
        )

        self.activity1 = (
            latest.playback,
            {
                True: (True, False, self.activity2),
                False: (False, False, "No activity - sleep"),
            },
        )

        self.activity_zipped = (
            val
            for val in [
                self.activity1,
                self.activity2,
                self.activity3,
                self.activity4,
                self.activity5,
            ]
        )
        # __________________________________________________________________ ::

        # :: Listened Time if Latest ID [does] equal Prior ID -----------------
        if self.is_same_id:

            self.listened1 = (
                self.progress_exceeds_request,
                {
                    True: (False, prior.time_listened + self.unix_request_tmstmp, None),
                    False: (
                        False,
                        prior.time_listened + self.prior_request_to_latest_start,
                        None,
                    ),
                },
            )

            self.zipped_listened = (val for val in [self.listened1])

        # :: Listened Time if Latest ID does [not] equal Prior ID -------------
        else:

            self.listened2 = (
                self.unix_request_tmstmp < prior.time_remaining,
                {
                    True: (False, prior.time_listened + self.unix_request_tmstmp, None),
                    False: (
                        False,
                        prior.time_listened
                        - (latest.unix_start_tmstmp.__sub__(prior.unix_request_tmstmp)),
                        None,
                    ),
                },
            )

            self.listened1 = (
                self.cutoff_prior,
                {
                    True: (True, self.listened2, None),
                    False: (False, prior.playback.duration, None),
                },
            )

            self.zipped_listened = (val for val in [self.listened1, self.listened2])
        # __________________________________________________________________ ::
        # __________________________________________________________________ ::

    @staticmethod
    def validate(condition):
        return True if condition else False

    @staticmethod
    def eval_zipper(zipper: Generator):

        condition, test = next(zipper)
        desc1 = test.get(Delta.validate(condition))
        cont, outcome, desc = desc1

        while cont:
            condition, test = next(zipper)
            desc1 = test.get(Delta.validate(condition))
            cont, outcome, desc = desc1

        return outcome, desc

    @property
    def activity_comparison(self):
        return self.eval_zipper(self.activity_zipped)

    @property
    def prior_listened_detail(self):
        return self.eval_zipper(self.zipped_listened)

    def compare(self):
        is_new, desc = self.activity_comparison
        prior_listened, _ = self.prior_listened_detail
        return is_new, prior_listened, desc

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


class Activity(user.UserDBO):
    def __init__(self, username: str):
        super().__init__(username)

        self.username: str = self.user_id

        self.current = Current(
            user_id=username, headers=self.headers(), href=self.current_playback
        )
        # TODO: Add a setter to Current class containing

        self.last_added: dict = {"track": "", "episode": ""}

        self.play = self.current.now(self.headers())

        if self.play.playback:
            self.cached: list = [self.play]
        else:
            self.cached: list = []

        self.exceptions: list = []

    def write(self, cache_maximum: int = 10):

        # TODO, create a '.batch()' method in the Activity class or make it
        #  a parent/sub-class that's instantiated with a list of instances
        #  on which a 'save()' method can be immediately called
        if len(self.cached) >= cache_maximum:

            remainder = self.cached.pop(-1)

            connect(host=Connector.get_creds(collection="activity"), alias="activity")

            for val in self.cached:

                try:
                    ActivityDoc.Activity(val).save()
                #     TODO: Add an insert_many() method instead of
                #      repeatedly calling .save()
                except:
                    self.exceptions.append(val)

            disconnect("activity")

            self.cached = [remainder]

        return self

    @property
    def resumed_playback(self):
        return (
            self.play.playback.id == self.last_added[self.play.currently_playing_type]
        )

    def add_to_all_time_played(self) -> object:

        self.last_added[self.play.currently_playing_type] = self.play.playback.id

        self.play.playback.add_to_playlist(
            playlist_href=self.activity_playlist_hrefs.get(
                self.play.currently_playing_type
            ),
            headers=self.headers(post=True),
        )

        return self

    def run(
        self,
        active_req_rate: int = 25,
        dormant_req_rate: int = 300,
        cache_maximum: int = 10,
    ) -> object:

        self.play = self.current.now(self.headers())

        if self.play.playback:
            self.cached.append(self.play)

        while self.play.status_code not in [
            400,  # Bad / Malformed Request
            401,  # Unauthorized
            403,  # Forbidden
        ]:

            # print(f"Tokens expiring in: {self.tokens.expires_in.minutes}")

            self.play = self.current.now(self.headers())

            if self.play.playback and not self.cached:

                self.cached.append(self.play)

            elif self.play.playback:

                delta = Delta(self.play, self.cached[-1])
                is_new, time_listened, desc = delta.compare()

                # TODO: Figure out why time listened continues to accumulate
                #  even after pausing has occurred
                # print(time_listened.seconds)
                print(
                    f"Outcome:\n\t{desc}\n"
                    f"New Play:\n\t{is_new}\n"
                    f"Resumed Playback:\n\t{self.resumed_playback}"
                )

                if not is_new:
                    # self.play.request_cnt = delta.prior.request_cnt
                    self.play.request_cnt = self.cached[-1].request_cnt
                    self.play.time_listened = time_listened
                    self.cached.pop(-1)

                # elif not delta.is_same_id:
                elif self.resumed_playback:
                    print(f"< no current activity - {dormant_req_rate}s sleep>")
                    time.sleep(dormant_req_rate)

                # elif not self.resumed_playback:
                else:

                    print(f"< adding to activity playlist >\n")

                    self.last_added[
                        self.play.currently_playing_type
                    ] = self.play.playback.id

                    self.add_to_all_time_played()

                self.cached.append(self.play)
                self.write(cache_maximum=cache_maximum)
                time.sleep(active_req_rate)

                # else:
                print(f"< no current activity - {dormant_req_rate}s sleep>")
                time.sleep(dormant_req_rate)

        return self


# TODO: Add something that always checks the last track added to the podcast
#  all time played playlist to make sure not repeatedly adding pods -
#  alternatively could just have it always store that last track and last
#  podcast added to each playlist and only add new tracks that aren't equal
#  to those
