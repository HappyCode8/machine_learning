__author__ = 'zl'
# coding=utf-8

import numpy as np
def replace_proType(cont):
    temp = cont.split(',')
    if temp[1].lower() == 'tcp':
        temp[1] = '0,0,1'
    elif temp[1].lower() == 'udp':
        temp[1] = '0,1,0'
    elif temp[1].lower() == 'icmp':
        temp[1] = '1,0,0'
    else:
        temp[1] = 0
    temp[2] = replace_service(temp[2])
    temp[3] = replace_flag(temp[3])
    temp[41] = temp[41].rstrip('.')
    if replace_lable(temp[41]) == 0:
        temp[41] = '0'
    else:
        temp[41] = '1'
    return temp

def replace_flag(flag):
    flag_list = ['OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'S0', 'S1', 'S2', 'S3',
                 'SF', 'SH']
    if flag.upper() in flag_list:
        num = flag_list.index(flag.upper())
        temp = ['0'] * len(flag_list)
        temp[num] = '1'
        str = ",".join(temp)
        return str
    else:
        return 'ERROR'

def replace_service(service):
    ser_list = ['aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime',
                'discard', 'domain', 'domain_u', 'echo', 'eco_i', 'ecr_i',
                'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'harvest',
                'hostnames', 'http', 'http_2784', 'http_443', 'http_8001',
                'imap4', 'IRC', 'iso_tsap', 'klogin', 'kshell', 'ldap', 'link',
                'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns',
                'netbios_ssn', 'netstat', 'nnsp', 'nntp', 'ntp_u', 'other',
                'pm_dump', 'pop_2', 'pop_3', 'printer', 'private', 'red_i',
                'remote_job', 'rje', 'shell', 'smtp', 'sql_net', 'ssh',
                'sunrpc', 'supdup', 'systat', 'telnet', 'tftp_u', 'tim_i',
                'time', 'urh_i', 'urp_i', 'uucp', 'uucp_path', 'vmnet', 'whois',
                'X11', 'Z39_50']

    if service.lower() in ser_list:
        num = ser_list.index(service.lower())
        temp = ['0'] * len(ser_list)
        temp[num] = '1'
        str = ",".join(temp)
        return str
    else:
        return 'ERROR'

def replace_lable(lable):
    lable_list = ['normal', 'back', 'land', 'neptune', 'pod', 'smurf',
                  'teardrop', 'ipsweep', 'nmap', 'portsweep', 'satan',
                  'ftp_write', 'guess_passwd', 'imap', 'multihop', 'phf', 'spy',
                  'warezclient', 'warezmaster', 'buffer_overflow', 'loadmodule',
                  'perl', 'rootkit']

    if lable.lower()=="normal":
        return 0
    else:
        return 1

def file2arr(file_path):
    with open(file_path) as file_object3:
        lines = file_object3.readlines()
        line_cnums = lines[0].split(',').__len__()
        line_rnums = len(lines)
        result_mat = np.zeros((line_rnums, line_cnums))
        class_lable = []
        for i in range(line_rnums):
            line = lines[i].strip()
            item_mat = line.split(',')
            if item_mat.__len__() == line_cnums:
                result_mat[i, :] = item_mat[0:line_cnums]
                class_lable.append(item_mat[-1])
        return np.array(result_mat), np.array(class_lable)

def file_wash(file_path, file_out):
    with open(file_path) as file_object:
        with open(file_out, 'a') as file_object2:
            lines = file_object.readlines()
            for i in range(0, lines.__len__()):
                content = lines[i]
                replaced = replace_proType(content.rstrip())
                #print(replaced)
                str = ",".join(replaced)
                file_object2.write(str + "\n")

def normalized(data_mat):
    datamin, datamax = data_mat.min(0), data_mat.max(0)
    data_shape = data_mat.shape
    data_rows = data_shape[0]
    data_cols = data_shape[1]

    for i in range(0, data_rows, 1):
        for j in range(0, data_cols - 1, 1):
            if (datamax[j] - datamin[j]) > 0:
                data_mat[i][j] = (data_mat[i][j] - datamin[j]) / (
                        datamax[j] - datamin[j])
    return data_mat

file_path = './data/newfile'
file_out = './data/datafinal'
file_wash(file_path, file_out)
print("finish cleaning")