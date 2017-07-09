# -*- coding: utf-8 -*-
import argparse
import queue
from qn_tools import upload
from qn_tools import config

__version__ = "0.1.0"


def version():
    return "version:" + __version__


# 添加子命令函数
def upload_func(args):
    print(upload.upload_file(args.localfile, rename=args.rename))


def pull_func(args):
    print("pull")


def push_func(args):
    print("push")


def config_func(args):
    print("config")
    config.set_config(args.ak, args.sk, args.bucket, args.bucket_domain)


def info_func(args):
    print(config.show_config())


def main():
    # 创建最上层解析器
    parser = argparse.ArgumentParser(add_help=True)
    subparsers = parser.add_subparsers(title='七牛工具',
                                       description='利用七牛API的上传，下载工具',
                                       help='additional help',
                                       dest='subparser_name')
    # 创建子解析器 'upload'
    parser_upload = subparsers.add_parser('upload', aliases='u')
    parser_upload.add_argument('localfile', type=str, help='本地文件路径')
    parser_upload.add_argument('-n', '--rename', type=str, help='远程文件名')
    parser_upload.set_defaults(func=upload_func)  # 将函数foo 与子解析器foo绑定
    # 创建子解析器 'pull'
    parser_pull = subparsers.add_parser('pull')
    parser_pull.set_defaults(func=pull_func)  # 将函数bar与子解析器bar绑定
    # 创建子解析器 'push'
    parser_push = subparsers.add_parser('push')
    parser_push.set_defaults(func=push_func)
    # 创建子解析器 'conf'
    parser_conf = subparsers.add_parser('config')
    parser_conf.add_argument('ak', type=str)
    parser_conf.add_argument('sk', type=str)
    parser_conf.add_argument('bucket', type=str)
    parser_conf.add_argument('bucket_domain', type=str)
    parser_conf.set_defaults(func=config_func)
    # 创建子解析器 'info'
    parser_conf = subparsers.add_parser('info')
    parser_conf.set_defaults(func=info_func)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
