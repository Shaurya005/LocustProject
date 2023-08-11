from locust import User, task, between


# There are two ways to define tasks in Locust script. One is @task Decorator, and this is the way which we have been using so far in our locust script and this is the way which is preferred and the other way to do is using tasks attribute.
#
# We will discuss more about tasks attribute in our next chapter. Let's formally learn @task decorator. Let's declare a couple of more tasks in script using @task decorator.
#
# And also within this lecture, let's learn to use weight argument to define task execution ratio. Okay, so we have two tasks over here login_URL and logout_URL.
#
# Now what happens when user arrives? User creates an instance of class MyUser with this wait_time attribute value and then it executes task.
#
# It can randomly pick any task out of the task inside these in current way, it can randomly pick any task out of these list of task and then it executes that task.
#
# It waits for the time defined and then again it picks any task out of these tasks. That's how it works so effectively there is equal probability of task being chosen by user.
#
# In case we want to increase the probability of a particular task being chosen, we have to define it using weightage.
#
# So instead of login_URL and logout_URL if suppose method names are "add_cart" and "view_product".
#
# So in real life scenario, if we see probability of viewing product is more than adding to cart so we can define this probability as per our business scenario in the that particular ratio.
#
# Again, the point to note over here is that it is likelihood and it's not the guarantee that this ratio will be adhered to.
#
# But yes, there will be double chances of add_cart task getting picked as compared to view_product task. So let's run this script and see. So let's run this script.
#
# I will run this script in headless mode with user 1 and hatch rate one and say only-summary. Okay, so we will have this result summary at the end of run.
#
# So let's have a closer look on the print outs. So as I said, we are defining the likelihood of this task occurring more than this task, but there
#
# is no guarantee but Locust tries to pick according to the weightage defined in the task.
#
# So that was all about task decorator. In our next lecture we will have a look at another way of declaring task. That is with the help of tasks attribute.

class MyUser(User):

    wait_time = between(1, 2)

    @task(2)
    def add_cart(self):
        print("I am add to cart")

    @task(4)
    def view_product(self):
        print("I am view product")
