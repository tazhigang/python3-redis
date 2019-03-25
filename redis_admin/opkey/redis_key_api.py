# exists(name)	判断一个key是否存在	redis.exists('name')	True
# delete(name)	删除一个key	redis.delete('name')	1
# type(name)	判断key类型	redis.type('name')	b'string'
# keys(pattern)	获取所有符合规则的key	redis.keys('n*')	[b'name']
# randomkey()	获取随机的一个key	randomkey()	b'name'
# rename(src, dst)	将key重命名	redis.rename('name', 'nickname')	True
# dbsize()	获取当前数据库中key的数目	dbsize()	100
# expire(name, time)	设定key的过期时间，单位秒	redis.expire('name', 2)	True
# ttl(name)	获取key的过期时间，单位秒，-1为永久不过期	redis.ttl('name')	-1
# move(name, db)	将key移动到其他数据库	move('name', 2)	True
# flushdb()	删除当前选择数据库中的所有key	flushdb()	True
# flushall()	删除所有数据库中的所有key	flushall()	True