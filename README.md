<!--# LyveCloud solutions samples

<img src="images/LyveCloud-logo.png?raw=true" width="700">

[LyveCloud](https://www.seagate.com/gb/en/services/cloud/storage/) by [Seagate](https://www.seagate.com) is an S3-compatible storage-as-a-service platform designed as a simple, trusted, and efficient service allowing enterprises to unlock the value of their massive unstructured datasets and enabling them to store more for longer.

This repository holds integrations and solutions written by LyveCloud users who contributed them for the benefit of the LyveCloud users` community. We are happy to see you here and encourage you to take part in this community. 

Notice the solutions are not part of the LyveCloud product.  

## Getting Started
- Browse our repository to find usefull tools for your needs (as listed below) or to get inspiration for building your integration.
- Have a question? Let's have a [discussion](https://github.com/barviv-seagate/git_samples/discussions) (don't be shy). 
- Want to crate and contribute your own solution? Read our [Contribution Guide](CONTRIBUTING.md).

The repository is licensed under the [Apache 2.0 License](LICENSE).

## Your task
Create CLI tool for S3 operations:
1. Open a [Free account in AWS](https://aws.amazon.com/free).
1. Create a help menu (--help flag).
1. List objects by bucket name (optional: path).
1. Put object by bucket name & object path.
1. Delete object by bucket name & object path.
1. Create short documentation to explain your code.
1. Create a pull request for your changes.
1. **Note:** You can write in any code language you choose.
-->
# Integration Subject

[Video Link](your-link)

## Introduction
<!--Write an introduction on the subject of integration you have chosen-->
*CLI app*
This program is an imitation of "AWS CLI" with limited capabilities.
This CLI allows basic commands in s3 - AWS storage.

## Requirements
<!--Details of your work environment: operating system, versions, installations to be performed for the integration, etc.-->
- Operating system: WINDOWS\IOS\LINUX
- Installing PyCharm 2020 or above
- Installing Boto3 (AWS package)
- AWS user
- Installing CLI
- AWS configure (set up installation)

**Tutorial**


## Include and Not-Included
#### Include
This CLI allows the follow commands:

1. See all files that are stored in the s3 by bucket's name : 'bucket name' get list
For example:
![image](https://user-images.githubusercontent.com/88038376/154974991-3d1b0e0f-8b3c-4f38-bc94-e7a3274c7c13.png)
Here you can see one file named 'check.txt' in bucked named 'seagate-test-amir-b'.

2. Put a new file by a bucket name: 'bucket name' put object
For example:
![image](https://user-images.githubusercontent.com/88038376/154975553-32e64bdf-7086-4142-8cef-708e0d3e8b77.png)
The file is located at 'C:\Users\amirk\s3tutorial' and the file named 'test.txt'.

3. Delete a file by a bucket name: 'bucket name' delete object
For example:
![image](https://user-images.githubusercontent.com/88038376/154976002-aa90ca77-0102-4117-93db-7638af843991.png)
'test.txt' deleted from 'seagate-test-amir-b' bucket.

4. Help menu: --help
![image](https://user-images.githubusercontent.com/88038376/154973085-e510e7fc-706d-4df0-8c1b-b981d9fdf14f.png)
result:
![image](https://user-images.githubusercontent.com/88038376/154973213-7eac8c02-f008-4d95-b99c-0d6d61cc135b.png)

#### Not-Included
<!--* Please describe what features are not-included. -->

##### Key areas to address during the challenge:
* Security - there are no memory leak therefore external code cannot be entered easily. using boto 3 should be secure link.
<!--* Performance - -->
* Resiliency - most errors are addressed
<!--* Scalability -->
<!--* Recovery -->

## Running Steps
<!--**Step 1:** Get your Lyve Cloud bucket credentials.   
Here's what you'll need:
* Access Key
* Secret key
* Endpoint URL

**Step 2:** 
Complite the following steps in detail and explained, including execution commands. It is recommended to add pictures that simulate the steps if necessary.-->
To use this CLI, follow these steps:
1. Create an [AWSaccount ](https://aws.amazon.com/s3/?c=s&sec=srv).

2. Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

3. Install [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html)

4. Open CMD by typing in the search box "cmd":
![image](https://user-images.githubusercontent.com/88038376/154863221-e74949d7-fc6e-4536-a051-1c2d01d7d7b4.png)

5.[Set up installation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html)

6. Install boto3 package by typing the following command -  python -m pip install boto3
![image](https://user-images.githubusercontent.com/88038376/155021311-42db6b92-e79f-4fcf-b950-47f37be65361.png)

7. Set the folder address by typing the following command - cd "file address"
![image](https://user-images.githubusercontent.com/88038376/154862865-3c7f67cf-7768-4442-b97d-b39634f7c89c.png)
In this example, "C:\Users\amirk\pythonProject1" is the file address.

8. Open the script by typing the following command - python "file name".py
![image](https://user-images.githubusercontent.com/88038376/154863031-1df9a1ed-854f-4dde-9230-9ab181123277.png)
In this example, main is the name of the file and ".py" refers to the file type.

## Results 
<!--show the results in pictures or in a short paragraph.-->

## Tested by:
<!--* August 22, 2021: Bari Arviv (bari.arviv@seagate.com) on Ubuntu 20.4
* month day, year: full_name (email) on your_environment-->

## **Note:** All files should be uploaded (all the files you used for the integration) under one folder, including the README.md file. 
### Project Structure

<!--This section will describe the representation of each of the folders or files in the structure.-->
```
.
├── README.md
├── code - cli_home_task
│   └── main.py
│	└── tests.py
├── documentation
│   └── introduction.pptx
└── images
    └── <image-name>
```

### `/code`
This folder contains:<!--, all the code files.-->
1. main.py - program
2. tests.py - tests sample

### `/documentation`
This folder contains:<!--, the demo video and presentation file.-->
1. introduction

### `/images`
<!--This folder contains, all the images.-->

