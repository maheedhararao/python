import requests, os, json, subprocess, sys


def commit_details():
    proxies = {'http': 'http://proxy-chain.intel.com:911',
               'https': 'http://proxy-chain.intel.com:912'}
    url = 'https://api.github.com/repos/maheedhararao/python/commits'
    data = requests.get(url=url, proxies=proxies)
    latest_commit_url = data.json()[0]['url']
    latest_data = requests.get(url=latest_commit_url, proxies=proxies)
    files = latest_data.json()['files']
    directories = []
    for each in files:
        names = each['filename'].strip().split('/')
        if 'source_directory' in names:
            if names[-2] not in directories:
                directories.append(names[-2])
    return directories


def trigger_tests():
    directories = commit_details()
    print directories
    if len(directories) == 0:
        print('The changes are not made to Source directory. Hence doing nothing.')
        sys.exit()

    path = os.getcwd()
    test_files_path = path + '\\test_files.json'
    f = open(test_files_path)
    data = json.load(f)
    print(data)
    unit_test_folders_to_run = []
    for dir in directories:
        if dir in data['source_directories']:
            unit_test_folders_to_run.append(data['test_directories']['{}'.format(dir)])
    print unit_test_folders_to_run

    unit_test_path = os.getcwd() + "\\unit_test\\"
    cmd = 'python ' + unit_test_path
    for test_dir in unit_test_folders_to_run:
        files = os.listdir(unit_test_path+test_dir)
        for each in files:
            output = subprocess.check_output(cmd + test_dir + '\\' + each, shell=True)
            print(output)


trigger_tests()
