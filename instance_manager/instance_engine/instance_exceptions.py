

class InstanceEngineException(Exception):
    pass


class NoProfileFoundException(InstanceEngineException):
    message = 'No profile was found'


class SettingLoadException(InstanceEngineException):
    message = 'There was an error loading instance settings'


class MissingSettingException(InstanceEngineException):
    message = 'A setting is missing. Cannot continue.'
