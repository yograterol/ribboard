# coding=utf-8
import falcon

from middleware import JSONDecoder, JSONRequired
from api.v1.endpoints import Charge


app = falcon.API(middleware=[
    JSONRequired(),
    JSONDecoder()
])

app.add_route('/', Charge())