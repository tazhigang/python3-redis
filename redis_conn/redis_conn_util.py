#conding=utf-8
import redis
from redis_conn import setting

class Redis_Conn(object):
    # 创建windows的redis连接
    @staticmethod
    def get_windows_coon(db=setting.WINDOWS_REDIS_CONF.get("db")):
        coon  = redis.StrictRedis(host=setting.WINDOWS_REDIS_CONF.get("host"),
                                  port=setting.WINDOWS_REDIS_CONF.get("port"),
                                  db=db,
                                  password=setting.WINDOWS_REDIS_CONF.get("password"))
        return coon
    # 创建linux的redis连接
    @staticmethod
    def get_linux_coon(db=setting.LINUX_REDIS_CONF.get("db")):
        coon = redis.StrictRedis(host=setting.LINUX_REDIS_CONF.get("host"),
                                 port=setting.LINUX_REDIS_CONF.get("port"),
                                 db=db,
                                 password=setting.LINUX_REDIS_CONF.get("password"))
        return coon

# 测试方法
if __name__ == '__main__':
    coon = Redis_Conn.get_linux_coon()
    name = coon.get("name")
    print(bytes(name).decode("utf-8"))