import os
from fcache.cache import FileCache
import json


class ConfigFinder:
    def __init__(self, config_file: str = "SpotiBot.json") -> None:
        """Instantiates instances of environment configuration from .ini file.

        Args:
            config_file: Name of .ini configuration file following the
                format of SpotiBot_SAMPLE.ini
        """
        self.cache = FileCache(config_file.split(r".")[0], flag="cs")
        self.config_file = config_file
        self.path_to_config = self.cache.get(r"path_to_config")

    def clear_cache(self) -> object:
        """Clears cached path to configuration file."""
        self.cache.clear()
        return self

    @property
    def cache_exists(self) -> bool:
        """Checks to see if a cached file path exists to a valid file."""
        try:
            return os.path.isfile(self.path_to_config)
        except:
            return False

    @property
    def cache_is_valid(self) -> bool:
        """Checks to see if the valid file path contains the config file."""
        try:
            return self.config_file == os.path.basename(self.path_to_config)
        except:
            return False

    def locate_config(self):
        """Traverse file system from bottom up to locate config file."""
        for dirpath, dirnames, files in os.walk(os.path.expanduser("~"), topdown=False):

            if self.config_file in files:
                self.path_to_config = os.path.join(dirpath, self.config_file)
                break

            else:
                self.path_to_config = None

        return self.path_to_config

    def get_path(self) -> str:
        """Checks for cache existence and validates - traverses OS if not."""
        print("Locating configuration...")

        print("\t<1 of 2> Checking for cached path...")

        if self.cache_exists and self.cache_is_valid:
            print(f"\t<2 of 2> Found cached path: {self.path_to_config}")

        else:
            print("\t<2 of 2> Cached path not found")
            print(f"\nLooking for {self.config_file} in local file system..")

            self.path_to_config = self.locate_config()

            if self.path_to_config:
                print(
                    f"\t<1 of 1> '{self.config_file}' found at: "
                    f"{self.path_to_config}"
                )
            else:
                print(
                    f"\t<1 of 1> Could not find config file"
                    f" {self.config_file} please double check the name of "
                    f"your configuration file or value passed in the"
                    f"'config_file' argument"
                )

        return self.path_to_config

    def read_file(self) -> object:
        """Locates creds file and caches location.

        Returns:
            Dictionary containing SpotiBot configuration params

        """
        self.path_to_config = self.get_path()
        self.cache["path_to_config"] = self.path_to_config

        try:
            with open(self.path_to_config, "r") as r:
                self.cfg = json.load(r)

        except IOError as e:
            print(e)

        return self


class Config(ConfigFinder):
    def __init__(self, config_file: str = "SpotiBot.json"):

        super().__init__(config_file)

        self.path_to_config = self.get_path()
        self.cache["path_to_config"] = self.path_to_config

        try:
            with open(self.path_to_config, "r") as r:
                self.cfg = json.load(r)

        except IOError as e:
            self.cfg = None
            print(e)

    def get_configs(self, keys_to_traverse: list):

        sub = {k: v for k, v in self.cfg.items()}

        for k in keys_to_traverse:
            sub = sub[k]

        return sub

    @property
    def played_all_time(self):

        sub = self.get_configs(["PLAYLISTS", "ACTIVITY"])

        all_timers = {}

        for play_type, attrs in sub.items():
            playlist_name, playlist_description = list(attrs.values())
            all_timers[playlist_name] = playlist_description

        return all_timers
