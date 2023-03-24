import os
slave_hostname = os.popen("hostname").read()
print('Slave hostname is: {}'.format(slave_hostname))
for i in range(1, 10):
	print(i)
print('ubuntu_agent_added')