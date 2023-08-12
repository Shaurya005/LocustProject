from locust import User,TaskSet,task,between

# So in our last lecture we created task set class. We defined it outside user class and we also defined it within user class.
# And in this lecture we will define multiple task set classes within task set class. And this is also called nesting of task sets.

# So we have a task set class which is called UserBehavior and right now in this TaskSet class, we have task defined.
# Last lecture we saw the need to have categorically designed TaskSet classes right so we can define
# the TaskSet classes according to module and what we will do for that. We will have a main user behavior class and we can have inline task classes,
class UserBehaviour(TaskSet):

# Okay, So effectively we have user class which is calling user behavior class, which is main TaskSet class over here. And within this TaskSet class, I have two TaskSet classes.
#
# And these task set classes are defined as task with the help of @task decorator. For this user behavior class, I have two tasks defined effectively - One is class cart_module and one is class product_module.
# And within these task we have further tasks defined for that module. Like in Cart module, we have two task. We can have any number of tasks over here.
#
# And similarly for product module, I have two product test cases defined or two product tasks defined and you can also add any number of modules in this, any number of task set classes within this user behavior class.

# Now let's see how it works by running this script. What we are observing here is that we are only getting task of cart_module class executed Like I'm add to cart, I'm delete cart.
#
# I cannot find a single task where task of product_modules are being picked by user. So what is happening over here?
#
# Let's see this script again as a user comes as we run the test.
#
# Main UserBehavior class is called i.e. main TaskSet class. As task starts running and the user gets instantiated, main TaskSet class is called and this TaskSet class.
#
# And within this task set class user can pick any task, it can pick task for cart_module or it can pick task for product_module.
#
# So in this case, what happened? User picked a task for cart module and once user picks this cart_module task it stays within this task.
#
# And it randomly picks any task belonging to this Cart_Module and it never gets the opportunity to get out of Cart module. And this is the default behavior of nested task set classes.
#
# That is when a user picks main module task, it infinitely goes into that loops and it doesn't find a way to get out of this module and execute other module test cases.
#
# So how do we solve this problem? We solve this problem with the help of interrupt.
#
# So in our next lecture we will understand what is interrupt and how we can implement them in this current script to solve this problem of infinite looping.
#
# Finally, I have also updated the name of the argument from UserClass to self so that we clearly show that we are referring to TaskSet class, not user class.

   @task()
   class Cart_Module(TaskSet):

         @task()
         def add_cart(self):
            print("I am add to cart")

         @task()
         def delete_cart(self):
           print("I am delete cart")

   @task()
   class Product_Module(TaskSet):

         @task()
         def view_product(self):
            print("I am view product")

         @task()
         def add_product(self):
            print("I am add product")


class MyUser(User):

    wait_time = between(1, 2)

    tasks = [UserBehaviour]

