from locust import HttpUser, task, between


class LibraryUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_books(self):
        self.client.get("/books/")