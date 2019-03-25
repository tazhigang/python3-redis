# coding=utf-8
from redis_conn import redis_conn_util
if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(4)
    # sadd(name, *values) 	向key为name的set中添加元素 返回插入的个数
    # 由于set是无序的且不重复的数据结构，所以返回的插入个数不一定是你写的个数
    count = coon.sadd("student", "wangerxiao","张三","张四","张五","张六","张三","张三")
    print(count)
    # srem(name, *values) 	从key为name的set中删除元素	 返回删除的个数
    del_count = coon.srem("student","张三")
    print(del_count)

