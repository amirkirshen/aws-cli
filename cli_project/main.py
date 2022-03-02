import argparse
import boto3
from boto3 import client
from botocore.exceptions import ClientError


s3_client = boto3.client('s3')

def list_bucket():
    """
    Presents all the user's buckets and returns it as a list
    :return: Buckets list
    """
    bucket_template = '{bucket_name}\t\t{bucket_date}'

    bucketList = []
    for i, bucket in enumerate(s3_client.list_buckets()['Buckets']):
        print(bucket_template.format(bucket_name = bucket['Name'], bucket_date = bucket['CreationDate']))
        bucketList.append(bucket)
    return bucketList


def list_object_by_bucket(bucket, flag):
    """
    :param bucket: Bucket's name
    :return: Prints all the objects that in the bucket
    """
    conn = client('s3')  # assumes boto.cfg setup
    list = []
    try:
        buckets_contents = conn.list_objects(Bucket=bucket)['Contents']
    except Exception as e:
        print(e)
        buckets_contents =[]
    for key in buckets_contents:
        if flag:
            print(key['Key'])
        list.append(key['Key'])
    return list


def upload_file_to_bucket(bucket, folder_path, file_name):
    """
    :param bucket: Destination bucket's name
    :param folder_path: Source folder's name
    :param file_name: Upload file's name
    :return: Returns True if Succeeded. Else if not
    """
    local_file_path = folder_path + '/' + file_name
    try:
        response = s3_client.upload_file(local_file_path, bucket, file_name)
        print('upload succeeded\n')
        return response

    except Exception as e:
        print(e)
        return False

def delete_file(bucket, file_name):
    """
    :param bucket: Bucket name
    :param file_name: The file will be deleted
    :return: Returns True if Succeeded. Else if not
    """
    list = list_object_by_bucket(bucket, False)
    if file_name in list:
        try:
            s3_client.delete_object(Bucket=bucket, Key=file_name)
            print('delete succeeded')
            return True
        except Exception as e:
            print(e)
            return False
    else:
        print('file does not exist')


def help():
    """
    :return: Print the app options
    """
    print('each command starts with bucket name and one of the option above:\n')
    print('get list - returns all the object in the list\n')
    print('put object - ask for a file name and insert it to the bucket\n')
    print('delete object - ask for a file name and delete it\n')


class MENU(object):
    def __init__(self):
        self.mode = ''
        self.bucket_name = ''
    def get_mode(self):
        """
        Extract both bucket's name and mode's name
        :return:
        """
        inputs = input().split(' ')
        if inputs[0] == '--help':
            help()
        if len(inputs) < 3:
            self.mode = ' '
            return
        self.mode = ' '.join(inputs[-2:])
        self.bucket_name = ' '.join(inputs[:-2])

    def main_process(self):
        print('Welcome to S3 new CLI!\n')
        while True:
            self.get_mode()
            if self.parse_and_execute():
                break

    def parse_and_execute(self):
        """
        Call the right function by mode
        :return: True for exit. Otherwise False
        """
        if self.mode == 'get list':
            list_object_by_bucket(self.bucket_name, True)
            return False
        elif self.mode == 'put object':
            upload_file_to_bucket(self.bucket_name, input('insert folder path: '), input('\ninsert file name: '))
            return False
        elif self.mode == 'delete object':
            delete_file(self.bucket_name, input('insert file name: '))
            return False
        elif self.mode == 'exit':
            return True
        elif self.mode == ' ':
            return False
        else:
            print('invalid command\n')
            return False


if __name__ == '__main__':
    run_menu = MENU()
    run_menu.main_process()

# "C:\Users\\amirk\s3tutoria"