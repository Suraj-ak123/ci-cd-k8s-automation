## This Folder contains two Python automation scripts one named as Automated_Backup_Solution.py and other named as Automated_System_Health_checker.py files.

#### > Automated_System_Health_checker.py ---> This script monitors the systems health i.e of server where this file is executed and gives CPU usage, memory usage, Disk usage, number of running process and system health check.

#### > Automated_Backup_Solution.py ---> This script creates backup in aws s3 bucket by taking data from user specified directory in his/her local machine. For this I am using aws lambda function which will run this script when triggered initially. But here we have to authenticate our system with AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY so that our systems directory can be accessed by lambda fn. In this code aws sdk boto3 is used to interact with the local system.  

 
