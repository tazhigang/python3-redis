from redis_conn import redis_conn_util

if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(1)
    # 控制台输出之前存储的a对应的值
    a_before_value = coon.get("a")
    print("修改之前的a----->%s" %bytes(a_before_value).decode("utf-8"))
    # coon.append("a","addadada") 在key为a的value后面追加 并替换原来的value存入数据库
    coon.append("a", "addadada")
    a_after_value = coon.get("a")
    # 控制台输出修改以后的存储的a对应的值
    print("修改之后的a----->%s" %bytes(a_after_value).decode("utf-8"))
    # coon.substr("a",0,-2) 截取key为a的value
    a_substr_value = coon.substr("a",0,-2)
    print("截取的字符串的a----->%s" % bytes(a_substr_value).decode("utf-8"))