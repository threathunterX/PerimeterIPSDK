class Config(object):
    """
    全局配置信息
    """
    @property
    def mongodb(self):
        """
        mongodb 配置
        :return: {"uri": "", "db": "", "collection": ""}
        """
        return {
            "uri": "mongodb://{user}:{password}@{host}:{port}",
            "db": "blackip",
            "collection": "blackip"
        }

    @property
    def mysql(self):
        """
        mysql 配置
        :return: dict()
        """
        return {
            "host": "******",
            "port": 3306,
            "user": "******",
            "password": "******",
            "db": "blackip",
            "table": "blackip",
            "charset": "utf8"
        }

    @property
    def redis(self):
        """
        redis 配置
        :return: dict()
        """
        return {
            "host": "******",
            "port": 6379,
            "password": "******",
            "db": 0,
        }

    @property
    def user(self):
        """
        th_user 永安在线官网控制台查看配置 //https:www.yazx.com
        :return: {"snuser": "", "snkey": ""}
        """
        return {
            "snuser": "******",
            "snkey": "******"
        }

    @property
    def host(self):
        """
        host 配置 永安在线IP画像服务端域名, 联系工作人员获取
        :return: "hostname"
        """
        return "******"


G_CONFIG = Config()
