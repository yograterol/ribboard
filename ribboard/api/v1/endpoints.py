# coding=utf-8
import falcon
import json
import stripe

from engine.stripe_charge import ChargeUtilities, validate_charge_input


class Charge(object):

    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = json.dumps({
            'msg': 'Hello Ribboard'
        }, encoding='utf-8')

    @falcon.before(validate_charge_input)
    def on_post(self, req, res):
        data = req.context.get('doc')
        try:
            result = ChargeUtilities.charge(data)
        except (stripe.InvalidRequestError) as e:
            raise falcon.HTTPBadRequest(
                'Stripe error.',
                e.message
            )
        res.status = falcon.HTTP_200
        res.body = json.dumps(result, encoding='utf-8')