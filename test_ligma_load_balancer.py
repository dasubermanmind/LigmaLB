import pytest

from ligma_load_balancer import ligma_load_balancer



@pytest.fixture
def client():
    with ligma_load_balancer.test_client() as client:
        yield client

def test_init(client):
    result = client.get('/')
    assert 'Welcome to Ligma' in result.data
    

