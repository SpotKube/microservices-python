from locust import HttpUser, task, between

class TestUser(HttpUser):
    timer = between(1,10)

    @task
    def auth(self):
        self.client.get(
                "/primes/19319?algorithm=bruteForce"
                )
        
