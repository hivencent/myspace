#!/usr/bin/env python
# encoding:utf-8

#将邀请码修改为6位

import htlloworld

#db = web.database(host="192.168.1.242", port=3306, dbn='mysql', user='wanglibao', pw='wanglibank', db='wanglibao')
#db = web.database(host="127.0.0.1", port=3306, dbn='mysql', user='root', pw='dh6svp132e', db='wanglibao')
db = htlloworld.database(host='rdsamqnzeamqnze.mysql.rds.aliyuncs.com', port=3306, dbn='mysql', user='wanglibao', pw='wanglibank', db='wanglibao')


def main():
    sql = "select user_id from wanglibao_profile_wanglibaouserprofile where user_id not in (select user_id from marketing_promotiontoken)"
    users = list(db.query(sql))
    print(len(users))
    for user in users:
        sql1 = "select * from marketing_invitecode where is_used=0 limit 1"
        token = list(db.query(sql1))[0]
        sql2 = "INSERT INTO marketing_promotiontoken(user_id,token) VALUES('%s','%s')" % (user['user_id'],token['code'])
        db.query(sql2)
        sql3 = "update marketing_invitecode set is_used=1 where id='%s'" % token['id']
        db.query(sql3)


if __name__ == "__main__":
    main()
