# -*- coding: UTF-8 -*-
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
import os, time, random
class ImageStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
    # 初始化
        super(ImageStorage, self).__init__(location, base_url)

    # 重写 _save方法
    def _save(self, name, content):
        # 文件扩展名
        ext = os.path.splitext(name)[1] #[0] 为文件名称
        #上传的文件原名
        source_name = os.path.splitext(name)[0]
        # 文件目录
        d = os.path.dirname(name)
        # 定义文件名，年月日时分秒随机数,也可以使用MD5加密方式等等。。
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0,100)
        #定义文件名，md5加密方式
        import hashlib
        hash = hashlib.md5()
        hash.update(source_name.encode('utf-8'))
        fn1 = hash.hexdigest()
        # 重写合成文件名
        name = os.path.join(d, fn + ext) #若文件名以md5方式换成fn1即可
        # 调用父类方法
        return super(ImageStorage, self)._save(name, content)