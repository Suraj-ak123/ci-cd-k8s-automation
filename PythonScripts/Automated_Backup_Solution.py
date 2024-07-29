# Write a script to automate the backup of a specified directory to a remote server or a cloud storage solution. 
# The script should provide a report on the success or failure of the backup operation. 

import os
import logging
import boto3
from botocore.exceptions import ClientError
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Setup logging
logging.basicConfig(filename='backup.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Initialize S3 client 
s3_client = boto3.client('s3')  

# Inputs
SOURCE_DIR = input("Enter the source directory path: ")
BUCKET_NAME = input("Enter the S3 bucket name: ")
S3_PREFIX = input("Enter the S3 prefix (or press Enter to skip): ")

def upload_file_to_s3(file_path, bucket_name, s3_prefix):
    """Upload a file to an S3 bucket."""
    try:
        relative_path = os.path.relpath(file_path, SOURCE_DIR)
        s3_path = os.path.join(s3_prefix, relative_path)
        s3_client.upload_file(file_path, bucket_name, s3_path)
        logger.info(f"Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
        print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
    except ClientError as e:
        message = f"Error uploading file {file_path}: {e}"
        logger.error(message)
        print(message)
    except Exception as e:
        message = f"Backup failed for {file_path} with exception: {e}"
        logger.error(message)
        print(message)

class Watcher:
    """Class to watch a directory and handle file events."""
    def __init__(self, directory_to_watch, bucket_name, s3_prefix):
        self.observer = Observer()
        self.directory_to_watch = directory_to_watch
        self.bucket_name = bucket_name
        self.s3_prefix = s3_prefix

    def run(self):
        """Start the observer to watch the directory."""
        event_handler = Handler(self.bucket_name, self.s3_prefix)
        self.observer.schedule(event_handler, self.directory_to_watch, recursive=True)
        self.observer.start()
        print(f"Watching directory: {self.directory_to_watch}")
        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.observer.stop()
            print("Stopped by user.")
        self.observer.join()

class Handler(FileSystemEventHandler):
    """Handler to process file system events."""
    def __init__(self, bucket_name, s3_prefix):
        self.bucket_name = bucket_name
        self.s3_prefix = s3_prefix

    def process(self, event):
        """Process the file system event."""
        if event.is_directory:
            return
        upload_file_to_s3(event.src_path, self.bucket_name, self.s3_prefix)

    def on_created(self, event):
        """Handle file creation event."""
        self.process(event)

    def on_modified(self, event):
        """Handle file modification event."""
        self.process(event)

if __name__ == "__main__":
    watcher = Watcher(SOURCE_DIR, BUCKET_NAME, S3_PREFIX)
    watcher.run()
