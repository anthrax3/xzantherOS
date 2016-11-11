
from instance_manager.instance_engine import instance_config
from instance_manager.instance_engine.instance_exceptions import NoProfileFoundException, SettingLoadException

from base.models import Profile, ProfileSetting, Setting


class InstanceManager(object):
    """
    Manages ALL saved instances for a given (single) profile.
    """

    running = True
    profile = None

    instance_map = {
        instance_config.AWS: AWSInstanceManager,
    }

    def __init__(self, profile_id):
        #
        # Look up profile
        # Load up all saved instances and start pinging them
        # Save statuses to an in-memory structure for display

        try:
            self.profile = Profile.objects.get(pk=profile_id)
        except:
            raise NoProfileFoundException()

        try:
            self.load_settings()
        except:
            raise SettingLoadException()

        self.run()

    def load_settings(self):
        pass

    def run(self):
        """
        Ping all of the ping servers in the instance list to get their statuses
        :return:
        """
        pass

    def stop(self):
        self.running = False


class GenericInstanceManager(object):
    """
    This is the general instance manager class -- it is meant to be overwritten
    """

    def set_settings(self, settings, *args, **kwargs):
        """
        Used to set any permissions or other settings required to connect to the instance.
        This includes the address of the instance, etc.
        NOTE: TO BE OVERWRITTEN!
        NOTE: Can also use __init__()
        """
        pass

    def connect(self, *args, **kwargs):
        """
        Connect to the instance using the settings provided in set_settings
        """
        pass

    def disconnect(self, *args, **kwargs):
        """
        Safely terminate the connection to the instance
        """
        pass

    def install_pingserver(self, *args, **kwargs):
        """
        Tells the manager to install the ping server on this instance
        """
        pass

    def provision_new_instance(self, *args, **kwargs):
        """
        provision a new instance
        """
        pass

    def destroy_instance(self, *args, **kwargs):
        """
        Destroy a given instance that is currently provisioned.
        """
        pass


class AWSInstanceManager(GenericInstanceManager):
    """
    Connect to the list of AWS instances with the given permissions.
    Check to see if the instancemanager directory is set in the home directory (of the instance)
    If not, create it
    Check to see if the ping server is running - if not, start it
    """





