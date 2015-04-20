# coding=utf-8
import falcon
import stripe

VALIDATE_FIELDS = (
    'amount',
    'currency',
    'customer',
    'card_token',
    'description'
)

def validate_charge_input(req, res, params):
    data = req.context.get('doc')
    for key in data.keys():
        if not key in VALIDATE_FIELDS:
            raise falcon.HTTPBadRequest(
                'Body error',
                'JSON has fields not supported'
            )

def charge(data):
    return stripe.Charge.create(
        amount=data.get('amount'),
        currency=data.get('currency'),
        source=data.get('card_token'),
        description=data.get('description'),
        api_key='sk_test_zzMfJ9e8K8MPOLQTu9Fu12ix'
    )
