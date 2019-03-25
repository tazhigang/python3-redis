# set(name, value)	给name赋值为value	redis.set('name', 'Bob')	True
# get(name)	返回数据库中key为name的string的value	redis.get('name')	b'Bob'
# getset(name, value)	给数据库中key为name的string赋予值value并返回上次的value	redis.getset('name', 'Mike')	b'Bob'
# mget(keys, *args)	返回多个key对应的value	redis.mget(['name', 'nickname'])	[b'Mike', b'Miker']
# setnx(name, value)	如果key不存在才设置value	redis.setnx('newname', 'James')	第一次运行True，第二次False
# setex(name, time, value)	设置可以对应的值为string类型的value，并指定此键值对应的有效期	redis.setex('name', 1, 'James')	True
# setrange(name, offset, value)	设置指定key的value值的子字符串	redis.set('name', 'Hello') redis.setrange('name', 6, 'World')	11，修改后的字符串长度
# mset(mapping)	批量赋值	redis.mset({'name1': 'Durant', 'name2': 'James'})	True
# msetnx(mapping)	key均不存在时才批量赋值	redis.msetnx({'name3': 'Smith', 'name4': 'Curry'})	True
# incr(name, amount=1)	key为name的value增值操作，默认1，key不存在则被创建并设为amount	redis.incr('age', 1)	1，即修改后的值
# decr(name, amount=1)	key为name的value减值操作，默认1，key不存在则被创建并设置为-amount	redis.decr('age', 1)	-1，即修改后的值
# append(key, value)	key为name的string的值附加value	redis.append('nickname', 'OK')	13，即修改后的字符串长度
# substr(name, start, end=-1)	返回key为name的string的value的子串	redis.substr('name', 1, 4)	b'ello'
# getrange(key, start, end)	获取key的value值从start到end的子字符串	redis.getrange('name', 1, 4)	b'ello'