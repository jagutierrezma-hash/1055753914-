from locust import HttpUser, task, between


class FakeStoreUser(HttpUser):
    host = "https://fakestoreapi.com"
    wait_time = between(1, 3)

    @task
    def get_products(self):
        self.client.get("/products")

