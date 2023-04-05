from locust import HttpUser, task, between

class TestUser(HttpUser):
    timer = between(1,10)

    @task
    def auth(self):
        self.client.post(
                "/login",
                auth=None,
                headers={"authorization": "Basic Z2Vvcmdpb0BlbWFpbC5jb206QWRtaW4xMjM="}
                )
        
