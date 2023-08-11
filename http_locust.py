from locust import HttpUser, task, between

# The way to convert a locust script to HttpLocust script is by using HttpUser which itself has inherited User
class MyUser(HttpUser):
    # pass

    wait_time = between(1, 2)
    # host = "http://newtours.demoaut.com/"

    # Command for directly providing host in command line while running locust script - locust -f http_locust.py --host="http://newtours.demoaut.com/"

    # We must have to define a host whether in host attribute in the User class of locust script or via command line or passing host via UI when we're inheriting a HttpUser class otherwise locust will throw an error

    @task
    def login_URL(self):
        print("I am logging into URL")


