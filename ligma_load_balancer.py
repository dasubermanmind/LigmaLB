from flask import Flask, request
import random 
import requests

ligma_load_balancer = Flask(__name__)

@ligma_load_balancer.route('/')
def router():
    host_header = request.headers['Host']
    if host_header == 'test':
        # THis is for testing and not for an actual impl
        response = requests.get('')

