# coding=utf-8
import falcon

from api.v1.endpoints import InitialEndpoint

app = falcon.API()

app.add_route('/', InitialEndpoint())