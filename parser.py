import time

import requests, os, json, subprocess, sys


def commit_details():
    proxies = {'http': 'http://proxy-chain.intel.com:911',
               'https': 'http://proxy-chain.intel.com:912'}
    url = 'https://api.github.com/repos/maheedhararao/python/commits'
    data = requests.get(url=url, proxies=proxies)
    latest_commit_url = data.json()[0]['url']
    latest_data = requests.get(url=latest_commit_url, proxies=proxies)
    files = latest_data.json()['files']
    # directories = []
    # files_changed = []
    info = {}
    for each in files:
        names = each['filename'].strip().split('/')
        if 'source_directory' in names:
            if names[-2] not in info.keys():
                info[names[-2]] = [names[-1].split('.')[0]]
            else:
                info[names[-2]].append(names[-1].split('.')[0])

    return info


def trigger_tests():
    info = commit_details()
    print info
    if len(info.keys()) == 0:
        print('The changes are not made to Source directory. Hence doing nothing.')
        sys.exit()

    path = os.getcwd()
    test_files_path = path + '//test_files.json'
    f = open(test_files_path)
    data = json.load(f)
    print(data)
    unit_test_folders_to_run = {}

    for key in info.keys():
        if key in data['source_directories']:
            if data['test_directories'][key] not in unit_test_folders_to_run:
                unit_test_folders_to_run[data['test_directories'][key]] = info[key]
            else:
                unit_test_folders_to_run[data['test_directories'][key]].extend(info[key])

    print(unit_test_folders_to_run)

    unit_test_path = os.getcwd() + "\\unit_test\\"
    print unit_test_path

    for key in unit_test_folders_to_run.keys():
        for each in unit_test_folders_to_run[key]:
            cmd = 'pytest ' + unit_test_path + key + '\\' + ' -s -m {}'.format(each)
            print cmd
            time.sleep(3)
            subprocess.Popen(args=cmd, shell=True).communicate()


trigger_tests()
