from locust import User, task, between, events

# Previously, we saw two special and useful methods from Locust, which were on_start and on_stop.
# In this lecture we will see further two more special methods which are test_start and test_stop.

# When we run our locust test, we might want to do certain activities like setting up connection with database, opening any file for reading.
# And then finally, we may want to do conjunction activities like disconnecting database or closing any file or any other task, like reading data from any configuration file.
#
# So in that case, what we have to do, we don't want to do these things at user level. These are not tasks at all, right?
#
# These are methods which we want to execute before and after our test run. And these are achieved with the help of Locust methods which are test_start and test_stop.
# Let's implement these in our Locust script. So we need to define these methods at module level and we can name them anything.
#
# For example, script_start, print I'm starting test or maybe "I'm connecting to DB"" just as an example.
# And similarly we can define script_stop which prints "I'm disconnecting from DB". So we can we need to define methods at module level, not inside user class.
#
# And these are normal methods so far, right? And they won't be executed if we run this script because they are not being called anywhere.
# And how do we convert them into test_start and test_stop method by using events. So let's use @events and for that we have to import events from locust.
# @events.test_start and we have to add listener for this. Similarly, we can use @events.test_stop and we have to add listener to that.
#
# So what does this mean that as soon as this test_start event occurs, a listener is listening to this and this script_start method is executed.
#
# And similarly, when this event test_stop occurs, listener reports that and this script_stop method is executed.
# Effectively any method below this @events.test_start line is test_start and any method below this @events.test_stop line is test_stop method.
#
# So one additional thing which we have to do in these special methods is we have to pass keyword argument i.e. **kwargs.
#
# So that means it can accept any argument. These methods can accept any argument. So in later sections I will tell you more about events, keyword argument and listener.
#
# And let's just run our script and let's understand how these test_start and stop method will behave.
#
# So let's run this script test_start_stop with two users and in headless mode. And let's stop this run and let's see what has happened this time.
#
# So as you start test, you get "I'm connecting to DB" and at this point of time, user has not started or hatched.
#
# And once users hatch in each of their, since there are two users, they do 2 logins I am logging into URL one user and I am logging into URL the other user and then these users go on their way to repeat this - I am doing my work.
#
# And finally, when the test ends, both of these users log out and finally the test stops - DB is disconnected i.e. test_stop method is executed.
# So we can see that for each user, on_start and on_stop is getting executed separately so there are 2 logins printed and 2 logouts printed but test_start and test_stop is executed only once irrespective of whatever number of users are passed.
#
# So this is how all of these methods work in conjunction test_start, test_stop, on_start and on_stop.
#
# So the important point to note over here is these special methods on_start and on_stop need to be named like this and within user class.
#
# And the other two methods test_start and test_stop can be named anything. They should accept keyword argument and they should be decorated by @events.test_stop.add_listener.

@events.test_start.add_listener
def script_start(**kwargs):
    print("I am connecting to DB")

@events.test_stop.add_listener
def script_stop(**kwargs):
    print("I am disconnecting from DB")


class MyUser(User):
    # pass

    wait_time = between(1, 2)

    # @task
    def on_start(self):
        print("I am logging into URL")

    @task
    def doing_work(self):
        print("I am doing my work")

    # @task
    def on_stop(self):
        print("I am logging out")
