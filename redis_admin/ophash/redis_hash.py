from redis_conn import redis_conn_util
# python3与redis操作hash类型的数据
# 为了做区分下面采用不同的redis的db进行操作
# string db=1
# hash db=2
# list db=3
# set db=4
# zset db=5
if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(2)
    # hset(name, key, value)
    # 向key为name的hash中添加映射 返回映射的个数
    count= coon.hset("user","name","zhangsan")
    print(count)
    print("===" * 20)
    # hsetnx(name, key, value)
    # 向key为name的hash中添加映射，如果映射键名不存在
    count_nx = coon.hsetnx("user", "desc", "playball")
    print(count_nx)
    print("==="*20)
    # hget(name, key)
    # 返回key为name的hash中field对应的value
    age = coon.hget("user","age")
    print(bytes(age).decode("utf-8"))
    print("===" * 20)
    # hmget(name, keys, *args)
    # 返回key为name的hash中各个键对应的value
    user_list = coon.hmget("user","age","name","desc")
    for user_element in user_list:
        print(bytes(user_element).decode("utf-8"))
    print(type(user_list))
    print("===" * 20)
    # hgetall(name)
    # 从key为name的hash中获取所有映射键值对
    user_dict = coon.hgetall("user")
    print(type(user_dict))
    for k,v in user_dict.items():
        print("%s---->%s"%(k,v))
    print("===" * 20)
    # 以下不做演示
    # hmget(name, keys, *args)
    # 向key为name的hash中批量添加映射

    # hincrby(name, key, amount=1)
    # 将key为name的hash中映射的value增加amount

    # hexists(name, key)
    # key为namehash中是否存在键名为key的映射

    # hdel(name, *keys)
    # key为namehash中删除键名为key的映射

    # hlen(name)
    # 从key为name的hash中获取映射个数

    # hkeys(name)
    # 从key为name的hash中获取所有映射键名

    # hvals(name)
    # 从key为name的hash中获取所有映射键值

