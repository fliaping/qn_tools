# -*- coding: utf-8 -*-
import os

from qiniu import Auth, put_file
from qiniu import BucketManager

from qn_tools import config


def upload_file(localfile, key_prefix=None, rename=None, hash_name=False):
    """
    上传文件
    :param localfile: 本地文件路径
    :param key_prefix: 远程文件前缀
    :param rename: 重命名远程文件名
    :param hash_name: 远程文件是否使用hash name
    :return: null
    """
    if not os.path.isfile(localfile):
        print('不是文件或者文件不存在：', localfile)
        return

    access_key, secret_key, bucket_name, bucket_domain = config.get_config()
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    file_dir, file_name = os.path.split(localfile)
    # 上传到七牛后保存的文件名
    if rename:
        file_name = rename
    key = file_name
    if key_prefix:
        key = key_prefix + '/' + file_name
    else:
        key = 'blog' + '/' + file_name
    bucket = BucketManager(q)
    bk_ret, bk_info = bucket.stat(bucket_name, key)
    if bk_ret:
        return '七牛已存在该文件,请修改文件名'

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    # 上传文件
    ret, info = put_file(token, key, localfile)
    return bucket_domain + ret['key']


# url = upload_file('/home/payne/Downloads/1.jpg', rename='me.jpg', key_prefix='test')
# print(url)
