#!/usr/bin/python3
import boto3
import subprocess
import time
import getpass


user = "root"
password = "123123123"
database = "Intern"


#AWS configuration
AWS_ACCESS_KEY_ID = 'AKIA52BEGI3BCCP6PEYC'
AWS_SECRET_ACCESS_KEY = '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'
S3_BUCKET = 'prajesh-bucket'

def get_dump():
    filestamp = time.strftime('%Y-%m-%d-%I')
    p = subprocess.run("mysqldump -u %s -p%s -c %s >  %s.sql" % (user, password,                                                                                                             database,"make_public_"+filestamp),shell=True)
    data_dump = "make_public_"+filestamp+".sql"
    data = open(data_dump, 'rb')
    s3 = boto3.resource('s3',
         aws_access_key_id=AWS_ACCESS_KEY_ID,
         aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    try:
        s3.Bucket(S3_BUCKET).put_object(Key= data_dump, Body=data)
    except e:
        pr
    else:
           subprocess.run(["rm", "-rf" , data_dump])
if __name__=="__main__":
 get_dump()
