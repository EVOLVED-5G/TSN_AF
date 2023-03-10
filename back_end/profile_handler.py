import yaml
from typing import Dict, List, Tuple
from os.path import join, abspath, dirname, exists, isfile, splitext
from os import makedirs, listdir

class ProfileHandler:
    profiles: Dict[str, Dict] = None
    baseFolder = abspath(join(dirname(__file__), '..', 'Profiles'))

    @classmethod
    def reload(cls) -> None:
        def _getFiles(path) -> List[Tuple[str, str]]:
            return [(join(path, f), f) for f in listdir(path) if isfile(join(path, f))]

        if not exists(cls.baseFolder):
            makedirs(cls.baseFolder, exist_ok=True)

        cls.profiles = {}

        files = _getFiles(cls.baseFolder)
        for path, file in files:
            try:
                filename, extension = splitext(file)
                if extension in ['.yml', '.yaml']:
                    with open(path, 'r', encoding='utf-8') as stream:
                        data = yaml.safe_load(stream)
                        cls.profiles[filename] = data
            except Exception as e:
                print(f"Unable to load profile '{file}': {e}")

        cls.profiles['best_effort'] = {}

    @classmethod
    def GetProfileNames(cls) -> List[str]:
        if cls.profiles is None: cls.reload()
        return list(cls.profiles.keys())

    @classmethod
    def GetProfileData(cls, name: str) -> Dict:
        if cls.profiles is None: cls.reload()
        return cls.profiles.get(name, {})
