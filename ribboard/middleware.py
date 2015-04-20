# coding=utf-8
import json
import falcon


class JSONRequired(object):

    def process_request(self, req, res):
        error = falcon.HTTPNotAcceptable(
            'This API only supports responses encoded as JSON.'
        )

        if not req.client_accepts_json:
            raise error

        if req.method in ('POST', 'PUT'):
            if not req.content_type:
                raise error

            if 'application/json' not in req.content_type:
                raise error


class JSONDecoder(object):

    def process_request(self, req, res):
        if not req.method in ('POST', 'PUT') or \
                not req.content_length:
            return

        if not req.content_length:
            return

        body = req.stream.read()

        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')

        try:
            req.context['doc'] = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')
