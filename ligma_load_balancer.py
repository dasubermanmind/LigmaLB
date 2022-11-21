from flask import Flask


ligma_load_balancer = Flask(__name__)

@ligma_load_balancer.route('/')
def router():
    return 'Welcome to Ligma'