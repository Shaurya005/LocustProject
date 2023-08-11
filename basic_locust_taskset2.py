from locust import User, task, between, TaskSet


class MyUser(User):

    # Defining task set class in this way is same as basic_locust_taskset.py
    @task
    class UserBehaviour(TaskSet):

        @task
        def add_cart(self):
            print("I am add to cart")

        @task
        def view_product(self):
            print("I am view product")

    wait_time = between(1, 2)

    # tasks = [UserBehaviour]
