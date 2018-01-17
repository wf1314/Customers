from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
from django.conf import settings


class MyStorage(Storage):
    """自定义上传文件类"""

    def _open(self, name, mode='rb'):
        """文件被打开时会调用"""
        pass

    def _save(self, name, content):
        """点击保存时调用"""
        # name为文件名 content为文件内容对象
        # print(conf_file)
        # 创建Fdfs对象,参数为配置文件
        client = Fdfs_client(settings.FDFS_CL_CONF)
        # 读取文件内容
        content = content.read()



        # return dict
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # } if success else None
        # upload_by_buffer的返回值为这个字典

        response = client.upload_by_buffer(content)
        # 如果上传失败抛出异常
        if response is None or response.get('Status') != 'Upload successed.':
            raise Exception('上传失败')
        # 字典的 'Remote file_id'里存储了 文件id
        file_id = response.get('Remote file_id')
        #　返回值会被存储在数据库的图片字段里
        return file_id

    def exists(self, name):
        # 判断文件是否存在
        return False

    def url(self, name):
        # 利用nginx访问图片
        return settings.FDFS_NGINX_CONF + name
