from redis_conn import redis_conn_util

if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(1)
    coon.move("a",15)