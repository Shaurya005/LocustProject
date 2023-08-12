from locust import User, task, between, SequentialTaskSet


class UserBehaviour(SequentialTaskSet):

    def on_start(self):
        print("I will login")

    @task
    def flight_finder(self):
        print("I will find flight by entering criteria")

    @task
    def select_flight(self):
        print("select_flight")

    @task
    def book_flight(self):
        print("book_flight")

# So now we already know that Every task has got equal probability of being picked so any task is being picked by user randomly.
#
# But what we really wanted, we wanted above tasks to proceed in order, right? We don't want user to book flight and then go to find flight.
#
# We want user to proceed in a loop where it goes to find flight, select flight, book flight, and then it starts again.
#
# Maybe if we would have added login, we would have added aon_start over here. Right? We can do that. Define on_start method and then print I will log in.
#
# Maybe I will fetch some details, some key which will be used in these flights. But eventually what we want, we want these tasks to proceed in sequential order.
#
# Even if on start will always execute for the one time, as we know, we want other methods to execute in sequence and for that we have SequentialTaskSet class.
#
# So instead of TaskSet class, what we will import is SequentialTaskSet class and the other things remain same and in UserBehaviour class we will inherit SequentialTaskSet class.
#
# And now let's run this script again and see what how it makes the difference. I'll run this script again. I will login, I will find flight, Select flight, Book Flight. I will find flight select.
#
# So it seems to be very much ordered now. So what is happening right now over here?
#
# So as we have added on_start method user will log in first and only for one time and then it will start by first task, which is find flight.
#
# Then it will proceed to second task, select flight and book flight. And then again will user will proceed.
#
# So user is executing one iteration and then second iteration and third. And then so user is in general executing in the way it is supposed to execute i.e. performing in loop and choosing task, but which task it will choose the one which
#
# is next to the task which has already chosen. And this is how SequentialTaskSet work and makes our script closer to our actual business scenario.
#
# So when we will work with Http, we will replace these print statement with real Http calls and then we will see the difference.

class MyUser(User):

    wait_time = between(1, 2)

    # tasks = {add_cart:2, view_product:4}
    tasks = [UserBehaviour]
