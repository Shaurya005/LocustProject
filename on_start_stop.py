from locust import User, task, between

# In this lecture, we will understand two special methods from locust, which are on_start and on_stop.
# So in our previous lectures, we saw that when we ran our script, we got this print "I am logging into URL" repeatedly.
#
# And what does that mean is that when each user comes, performs that task in loop again and again, and every user runs in its own loop during load test, there can be certain activities where task is
#
# supposed to be performed only once in the beginning or the end. For example, when we are testing an application, we need to login into application and log out of the application and between that
# log in and log out, we want to do certain activities repeatedly during load time, but we do not want to repeat, log in and log out.
#
# In that case, We can make use of these special methods on_start and on_stop.
# Let's understand with the help of this script, we will modify this script and we will add two more tasks over here.
#
# Suppose in normal scenario, if we add task, we will add it like this.
# Let me rename this task login_URL, a new task doing_work prints "I'm doing my work" and other task logout prints I'm logging out.
#
# And let's run this script in headless mode, to run this script in headless mode I will use - locust -f on_start_stop.py -u 1 -r 1 --headless --only-summary
# I will just use 1 user this time hatch rate 1 and I also use only_summary.
#
# That means all the summary of run that is request data which is not relevant in this case at the end of the run. And what we will do, we'll only get the printouts.
#
# So let's run this script. So you get on terminal - I'm logging, I'm doing work and I'm logging out multiple times
#
# Let's understand what's happening. So every time user comes, it can pick any task from these randomly, okay, within its loop.
#
# So when the user comes for the first time, it can pick any of these three task. And when it comes for second time in second iteration, again it can pick any of these tasks.
#
# So each task is having equal probability of getting picked right now. And so in this case, user can pick login task multiple times, pick logout task multiple times.
#
# And to solve this issue, what we have to do instead of using @task annotation on method name, we have to define these methods with name "on_start" and "on_stop".
#
# So we will not use @task decorator in loggin and logout methods with name "on_stop" and "on_start". So let me run this script and see the difference.
#
# So as we run start our test, it executes first task and prints "I am logging into URL" only once and as you can see, it is repeatedly doing this. "I'm doing my work" task, but it is not repeating "I'm logging into URL".
# It is just executed only one time. And let me just stop this script by pressing Ctrl + C. And You see, I get I'm logging out and as soon as the test stops or gets interrupted.
# This on_stop method is executed and it gives - I'm logging out in temrinal and also since we have used only summary, we can see that stats are printed. Only summary stats are printed at the end of the test run.
#
#
# And as we will proceed in the next lectures, we will find it really useful because we will be definitely logging into an application, retrieving the authentication code.
# And finally, we need to log out and we don't want to repeat these login and log out. So let's move to our next lecture, which will again talk about two more special methods in locust, which are test_start and test_stop.
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
