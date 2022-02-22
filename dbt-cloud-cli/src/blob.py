import logging
from azure.storage.blob import BlobServiceClient, ContainerClient, __version__
import datetime
import json

def get_now_dt():
    """
    Returns a datetime object in UTC of the current time
    """
    return datetime.datetime.now(datetime.timezone.utc)

class Blob:
    def __init__(self, connection_string, container_name):
        self.client = BlobServiceClient.from_connection_string(connection_string)  # driver for azure data storage first screen (THIS NEEDS TO BE A KEY/PAIR NOT CONN STRING)
        self.container = container_name                                            # name of the top directory
        self.container_client = self.client.get_container_client(container_name)   # driver to interact with folder (upload file, delete file)
        self.now = get_now_dt()
        print(f"Azure Storage Blob container connected with container path: {self.container}")

    def create_container(self, container: str = None) -> ContainerClient:
        """
        Creates a container after checking if the container exists or not.

        :params:
        container (str) - the string name of a container to create. If no container is provided,
        the container name provided upon class initialization will be the container to create.
        Note: if the container exists, this will not recreate the container.

        :returns:
        An azure container client.
        """
        if not container:
            container = self.container
        try:
            # If container exists return None
            if not self.container_exists(container):
                print(f"Creating container: {container}")
                new_container = self.client.create_container(container)
                return new_container
        except:
            logging.error(f"Container {self.container} exists already")
            return None

    def generate_date_partition(self) -> str:
        """
        This generates a time stamp partitioned (to the hour) of the current time

        :returns:
        a str object of the current timestamp in utc. If the time is 2020-01-01 2:34pm
        the output would be -> '2020/01/01/14/'
        """
        return str(self.now.year) + '/' + '{:02d}'.format(self.now.month) + '/' + '{:02d}'.format(self.now.day) + '/' + '{:02d}'.format(self.now.hour) + '/'

    def write_to_blob(self, file_name: str, data, extension: str = 'json', overwrite: bool = False) -> bool:
        """
        Using the container client created at initialization, this will dump a file
        in the corresponding time partitioned location within the blob container.

        :params:
        file_name (str) - the name of the file within the partition
        data (any) - the data to write into the file
        extension (str) - the suffix for the file name
        overwrite (bool) - should overwrite the data if the file exists. Default is false

        :returns:
        A boolean value pending success or failure of upload
        """
        if overwrite:
            logging.info('Overwrite is set to true, this might delete existing data from blob')
        date_partition = self.generate_date_partition()
        blob_name = date_partition + file_name + '.' + extension
        blob_client = self.client.get_blob_client(container = self.container, blob = blob_name)
        logging.info(f"Blob name: {blob_name}")
        logging.info(f"Blob client: {blob_client}")
        try:
            blob_client.upload_blob(json.dumps(data), overwrite = overwrite)
            return True
        except Exception as e:
            logging.error(e)
            return False

    def container_exists(self, name: str) -> bool:
        """
        Checks if a container exists

        :params:
        name (str) - name of the container to check for
        :returns:
        boolean value
        """
        containers = tuple(self.client.list_containers())
        return any([container for container in containers
            if container["name"].lower() == name.lower()])