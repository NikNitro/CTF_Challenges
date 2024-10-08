# -*- coding: utf-8 -*-

from flask import Blueprint, request, Response, jsonify, redirect, url_for
from application.util import is_from_localhost, proxy_req, FLAG
import random, os

SITE_NAME = 'hackerdreams.org'

proxy_dec = Blueprint('proxy_dec', __name__)
flag_dec = Blueprint('flag_dec', __name__)

@proxy_dec.route('/', methods=['GET', 'POST'])
def proxy():
    print(request.remote_addr)
    url = request.args.get('url')

    if not url:
        return redirect(url_for('.proxy', url="/"))
    
    target_url = f'http://{SITE_NAME}{url}'
    print(target_url)
    response, headers = proxy_req(target_url)
    print(response,headers)

    return Response(response.content, response.status_code, headers.items())

@flag_dec.route('/', methods=['GET'])
@is_from_localhost
def debug_environment():
    return FLAG