# coding=utf-8
import falcon
import json


class InitialEndpoint(object):

    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = json.dumps({
            'msg': 'Hello Ribboard'
        }, encoding='utf-8')
        