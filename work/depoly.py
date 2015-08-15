#!/usr/bin/env python
# encoding:utf-8

from fabric.api import env, run, task, roles, cd, put, get


env.roledefs = {
    'wanglibao_data': ['limt@112.124.9.35'],
}


script_name = "replace_old_user_invitecode_2.py"
export_name = "products.xls"

@roles('wanglibao_data')
def export():
    #put("/Users/lizhenjing/workspace/wanglibao_tools/invest_users.py", "/home/limt/invest_users.py")
    put("/Users/jinlong/Desktop/%s" % script_name, "/home/limt/%s" % script_name)
    with cd('~/'):
        run("python %s" % script_name)
        #get("/home/limt/%s" % export_name, "/Users/lizhenjing/workspace/wanglibao_tools/%s" % export_name)
