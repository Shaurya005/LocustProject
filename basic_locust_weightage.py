from locust import User, task, between

# Here we will understand how to add multiple user classes to see Lucast script and also weight attribute to define which user class should get more weightage and which should get less.
class MyWebUser(User):

    wait_time = between(1, 2)
    weight = 3

    @task
    def login_URL(self):
        print("I am logging into web URL")

    # So right now this script has only one user class. We can add more user classes to the same Locust script.
    #
    # But why would I like to have more user classes, for example, same performance script I want to run on both web user and mobile user.
    #
    # So I will name my users accordingly. Of course, we can convert it into http user, but that does not that focal point right now.


class MyMobileUser(User):

    wait_time = between(1, 2)
    weight = 1

    @task
    def login_URL(self):
        print("I am logging into mobile URL")


# Let's try our new test, this time I at least need 2 users to create two users, one Web and one mobile. I'll give 2 users on UI and I don't need host because I have not created it as http user script.
#
# OK, let us check that log. So you see All users spawned/hatched: {"MyMobileUser": 1, "MyWebUser": 1} (2 total users). If we have entered 1 on User box in UI then only only 1 user would have been hatched/spawned.


# We can choose which type of user we want to run in case we want to choose. Let's see how.
# While running this script from command line, we can specify the class itself, for example I may want to run only WebUser and let's run this script - "locust -f basic_locust_weightage.py MyWebUser"
#
# So it runs only webUser, now when I don't give any option what it will do, it will divide my users equally. For example, if I give 4 users on UI when the script runs, it will create 2 Web users and it will create 2 mobile users.
#
# But what if I want to distribute load in the manner that One gets more user and the other gets less user which is like realtime business scenario.
# In that case, I have to use weight attribute and as the name suggest, it gives weightage. For example, if I provide weight in WebUser as 3 and in mobile user as 1.
#
# So that defines the likelihood of users coming and picking web user is to mobile user in the ratio 3:1. So let me run this script again and refresh browser
# Now this time, I'll define 4 users with hatch rate 1 and let's see what happens. So if you see in logs three times, I'm getting WebURL and one time I'm getting mobile URL
# Next time, the user is coming, It gives two times webURL, one times mobile URL and again 4 times WebURL.
# So Ideal scenario would have been the first ones, that 3 times WebURL and 1 time MobileURL.

# But the only thing which we are doing with the help of weightage is we're increasing the probability of the class to be picked by giving it more weightage. So that's all about the weightage attribute.
