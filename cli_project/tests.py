from main import list_object_by_bucket, delete_file, list_bucket, upload_file_to_bucket

list_bucket()
adr = "C:/Users/amirk/s3tutorial"
list_object_by_bucket('seagate-test-amir-b', True)
upload_file_to_bucket('seagate-test-amir-b', )
list_object_by_bucket('seagate-test-amir-b', adr, 'test.py')
delete_file('seagate-test-amir-b', 'test.txt')
list_object_by_bucket('seagate-test-amir-b', adr, 'test.py')

