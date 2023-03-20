import os
print('Working on multi jobs')

print('Running job1 from branch local_1')
os.popen("hostname")

print('Running job2 on local branch2')
os.popen('hostname')

