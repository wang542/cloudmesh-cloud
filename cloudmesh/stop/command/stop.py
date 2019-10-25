from cloudmesh.mongo.MongoDBController import MongoDBController
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
from cloudmesh.common.console import Console
from cloudmesh.configuration.Config import Config

class StopCommand(PluginCommand):

    # noinspection PyUnusedLocal,PyBroadException
    @command
    def do_stop(self, args, arguments):
        """
        ::

            Usage:
                stop

            Description:

                stops cloudmesh

        """


        print("MongoDB stop")

        status = False

        config=Config()
        data = config["cloudmesh.data.mongo"]

        mode = data['MODE']

        if mode == 'docker':
            from cloudmesh.mongo.MongoDocker import MongoDocker
            mongo = MongoDocker()

            status = mongo.status(auth=True)
            if status['status'] == 'ok':

                id = mongo.id()

                mongo.stop()

        else:


            if MongoDBController().service_is_running():
                MongoDBController().stop()
            else:
                Console.ok("MongoDB service is already stopped")

        return ""
