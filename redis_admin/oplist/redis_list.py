from redis_conn import redis_conn_util
# python3与redis操作list类型的数据
# 为了做区分下面采用不同的redis的db进行操作
# string db=1
# hash db=2
# list db=3
# set db=4
# zset db=5
if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(3)