from redis_conn import redis_conn_util
# python3与redis操作zset类型的数据
# 为了做区分下面采用不同的redis的db进行操作
# string db=1
# hash db=2
# list db=3
# set db=4
# zset db=5
# zset也可以称为Sorted Set
if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(5)

    # 以下不做演示
    # zincrby(name, value, amount=1)
    # 如果在key为name的zset中已经存在元素value，则该元素的score增加amount，否则向该集合中添加该元素，其score的值为amount


    # zrank(name, value)
    # 返回key为name的zset中元素的排名（按score从小到大排序）即下标


    # zrevrank(name, value)
    # 返回key为name的zset中元素的倒数排名（按score从大到小排序）即下标


    # zrevrange(name, start, end, withscores=False)
    # 返回key为name的zset（按score从大到小排序）中的index从start到end的所有元素

    # zrangebyscore(name, min, max, start=None, num=None, withscores=False)
    # 返回key为name的zset中score在给定区间的元素

    # zcount(name, min, max)
    # 返回key为name的zset中score在给定区间的数量

    # zcard(name)
    # 返回key为name的zset的元素个数

    # zremrangebyrank(name, min, max)
    # 删除key为name的zset中排名在给定区间的元素

    # zremrangebyscore(name, min, max)
    # 删除key为name的zset中score在给定区间的元素
