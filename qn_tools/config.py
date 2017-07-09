import os
import json

qn_dir = '~/.config/qn_tools'
config_file_name = 'config.json'


def get_qn_path():
    return os.path.expanduser(qn_dir)


def get_file_path():
    return os.path.join(get_qn_path(), config_file_name)


def set_config(ak, sk, bucket, bucket_domain):
    if not os.path.exists(get_qn_path()):
        os.makedirs(get_qn_path(), exist_ok=True)

    config = {
        'access_key': ak,
        'secret_key': sk,
        'bucket': bucket,
        'bucket_domain': bucket_domain
    }
    json_str = json.dumps(config, indent=4)

    with open(get_file_path(), 'wt') as f:
        f.write(json_str)


def get_config():
    with open(get_file_path(), 'r') as f:
        data = f.read()
        config = json.loads(data)
        return config['access_key'], config['secret_key'], config['bucket'], config['bucket_domain']


def show_config():
    with open(get_file_path(), 'r') as f:
        data = f.read()
        return data

#
# set_config('g7LcSFkkYp5GAZ0JEGOKuPApz9inu7wBajwQSgG3', 'XDv9BxZEBUDl78uqZI5jFtl7mi_2qaGaUnCePaHw', 'mweb',
#            'https://o79q42bb0.qnssl.com/')
