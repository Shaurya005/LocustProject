from locust import User, task, between, TaskSet


class UserBehaviour(TaskSet):

    @task
    def add_cart(self):
        print("I am add to cart")

    @task
    def view_product(self):
        print("I am view product")


class MyUser(User):

    wait_time = between(1, 2)

    # tasks = {add_cart:2, view_product:4}
    tasks = [UserBehaviour]
