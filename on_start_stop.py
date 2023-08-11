from locust import User, task, between

# This class MyUser inherit one class named User which is coming from lucust, we have to import from locust User.

# To create local script, you have to create a class which inherits user class from locust and user represents one user which you are going to simulate.
# So this is what we are creating is a blueprint of our user simulated user.

# To run any local script I have to give locust command. and first thing it will look into it is whether this class, my user, which is inheriting user class, is existing or not.
# So with this it starts web interface. Let's go to web interface and try to run any test case.

# So here it says, My status is running and let me go back to PyCharm. But here I see the errors. One error is cannot choose from an empty sequence.

# And the other error is you must define a wait time on either the %s or %s class.
class MyUser(User):
    # pass

    wait_time = between(1, 2)

# In order to make this script fully functional, we have to mandatorily add few attributes to our user class. And the first attribute is task.
# We can add task to user class with the help of @task decorator for which we have to import this from locust. And below under @task decorator. We have to define method.
    @task
    def login_URL(self):
        print("I am logging into URL")

    # So you see I have defined below @task decorator one method which is representing the task which user will do. And it can be any task. Right now I'm just printing a statement.
    # Let's run this script again and see if we are able to fix error. So here, I'll refresh browser.
    # It is running and now go to terminal to see if our first error is fixed. So we are not getting a first error, which was empty test sequence. In order to run Locust class, we must define a task within the script.
    # We should make sure that we are indenting it right. So in case I will not do indentation, it will again throw me empty task sequence error. So indentation is important,
    # but still we are getting one error which is you must define a wait_time method. So the other important attribute which we should define in our Locust script to make it functional is wait_time.

    # So let's stop this script and add wait time. I just define a wait_time with the help of between method and the arguments I passed are 1 and 2. First, this method between needs to be imported from locust.

    # Now let's understand what is wait time. So when a simulated user, single simulated user runs, it performs iteration and within each iteration it performs task and then it performs next iteration where it again performs task.

    # And between these iteration we have to give some pacing that is called wait_time. We can define wait time in different ways, which we will understand in later chapter.

    # For now, let's define this wait time between 1 to where 1 is representing the minimum time for which user should wait for next iteration,
    # and 2 is the maximum time for which user should wait. And the time wait time can range between minimum value and maximum value. So now let's run this script again.



    # So now script is running. What is happening over here? I have created a class MyUser and I have defined mandatory attributes within this class.
    #
    # One attribute is task where I'm defining a method for the task which the user wants to do or user has to do. And the other is wait time, the time for which user should wait for between each iterations.
    #
    # Let's run this script with multiple users. Say number of users to simulate is actual load which you want to put on your performance test.


    # And hatch rate is a rate at which users will come linearly. And when we will start running it, you see now 5 users are running this test. And what does that mean in terms of locust script?
    # That implies that we have created five instances of this class and each instance is behaving in this manner. So our each simulated user is representing one instance of this class, and each instance is using this method and wait time.
    #
    # So in this lecture, we have created a functional script and we got the meaning of what do we have to add when we have to create a locust script? But is this Locust script really usable? I don't think so, because there is no system on which performance testing is being done.
    #
    # In our next lecture, we will do two things. One, we will add a system to this Lucast script on which testing is to be done and to indicate what kind of testing we will make use of Http protocol for which we will make this script as Http locust script.
