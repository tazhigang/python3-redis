# coding=utf-8
from redis_conn import redis_conn_util
# python3与redis操作set类型的数据
# 为了做区分下面采用不同的redis的db进行操作
# string db=1
# hash db=2
# list db=3
# set db=4
# zset db=5
if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(4)


    # 以下方法不做演示
    # spop(name)
    # 随机返回并删除key为name的set中一个元素


    # smove(src, dst, value)
    # 从src对应的set中移除元素并添加到dst对应的set中

    # scard(name)
    # 返回key为name的set的元素个数

    # sismember(name, value)
    # 测试member是否是key为name的set的元素

    # sinter(keys, *args)
    # 返回所有给定key的set的交集

    # sinterstore(dest, keys, *args)
    # 求交集并将交集保存到dest的集合

    # sunion(keys, *args)
    # 返回所有给定key的set的并集

    # sunionstore(dest, keys, *args)
    # 求并集并将并集保存到dest的集合

    # sdiff(keys, *args)
    # 返回所有给定key的set的差集

    # sdiffstore(dest, keys, *args)
    # 求差集并将差集保存到dest的集合

    # smembers(name)
    # 返回key为name的set的所有元素

    # srandmember(name)
    # 随机返回key为name的set的一个元素，但不删除元素