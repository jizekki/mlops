from locust import HttpUser, between, task
from string import ascii_lowercase
import random


class LocustUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def intent(self):
        sentence = "".join(random.choice(ascii_lowercase) for _ in range(20))
        self.client.get(f"api/intent?sentence={sentence}")
