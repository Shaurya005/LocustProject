from locust import User, task, between

def add_cart(userClass):
    print("I am add to cart")

def view_product(userClass):
    print("I am view product")

class MyUser(User):

    wait_time = between(1, 2)

    # There is no weightage, so my task is called randomly again. In here what user is doing?
    # User is coming and choosing any task out of this list, performing the task, waiting for wait_time and again in second iteration, user is choosing one of the task from this list.

    # tasks = [add_cart, view_product]

    # In this case, how do I give weightage? How do I define the execution ratio?
    #
    # And that can be done by defining task as a dictionary instead of defining it as a list.

    tasks = {add_cart:2, view_product:4}
    # And here I've defined a dictionary and within this dictionary I have two key value pairs.One is the name of task and the other is its weightage.

    # This is how we define task using task attribute and also this is how we give weightage to task when they are defined using task attribute.
    # So far we have worked with only declaring task inside user class. Task can also be declared inside Taskset class.
    # So in our next lecture I'll introduce you to this new class called Taskset Class, which defines the behavior of user in a separate class.

