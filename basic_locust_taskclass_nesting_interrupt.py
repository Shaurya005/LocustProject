from locust import User,TaskSet,task,between

# In last lecture we created nested task set classes within main task set class.
# And while running we observe that user was not able to exit out of one particular task set class, whichever it chooses.
#
# And it keeps on running the task of that particular class while what we wanted it to switch to other module as well.
# In this lecture, let's see how we can solve this problem using self.interrupt method.
class UserBehaviour(TaskSet):

   @task(2)
   class Cart_Module(TaskSet):

         @task(4)
         def add_cart(self):
            print("I am add to cart")

         @task(2)
         def delete_cart(self):
            print("I am delete cart")

# Before I explain self.interrupt method, let me add one more task to this each of the module.
#
# So let me name it as stop. You can name it anything and print I'm stopping. I'll copy paste this here in other module as well.
# So with this task addition, we intend to have our module execution stopped when user randomly comes and picks this task while executing within module.
#
# And what will help this to stop is self.interrupt. So within this method we will call self.interrupt method from locust.
#
# It has one argument reschedule which is by default True. So what does that mean? Let me first copy this self.interrupt here also in the other module. And let's first run this script.

# So here we see there is slight change in the logs. Now it is going to cart method as well and it is going to self.interrupt method as well.
#
# So what is happening right now? We have not defined the weightage of these task and therefore each task including a stop task, has equal probability of being picked.
#
# Once this self.interrupt is picked, what happens? The execution of user task stops for that task that is main task is class and it exits out of this for loop and reschedule is equal to true hands over the control to parent
# which reschedules the user which can again choose any task from within these cart_module or product_module and again user picks any of these task within these task.
#
# And if it gets an opportunity to arrive at this task stop task, it stops the execution of this complete task class itself, gives control back to parent and then so on.
#
# We can balance this execution by defining weightage within these tasks. So let's define weightage in cart module and product module. So first I will define the weightage for main tasks i.e. cart_module and product_module.
#
# Let this be two for cart_module and 4 for product_module and within product module I will define the weightage of each task. For stop let it be 1 and for add_product, let it be 2. And for view_product, let it be 4.
#
# And similarly for Cart, I can define stop 1 and for delete_cart 2 and add_cart 4. So effectively each will have its own probability, which is defined by the combination of probability of main task and then sub task.
#
# So let's run this script now. If we observe now, the web tasks are being picked are nearer to the execution ratio which we have defined. For example, view_product is more than add_product, right? And then stopping has only one ratio. Then it moves to add cart.
#
# It could have also moved again to product task. But this moves to add_cart. Then add to cart has more probability. Then it moves to stop cart. Then it moves to product.
#
# So that was all about this lecture. And as we saw, we can design our script nearer to business scenario with the help of task ratio, Nested task set class and self.interrupt method all in conjunction.


         @task(1)
         def stop(self):
            print("I am stopping")
            self.interrupt()

   @task(4)
   class Product_Module(TaskSet):

         @task(4)
         def view_product(self):
            print("I am view product")

         @task(2)
         def add_product(self):
            print("I am add product")

         @task(1)
         def stop(self):
            print("I am stopping")
            self.interrupt()


class MyUser(User):

    wait_time = between(1, 2)

    tasks = [UserBehaviour]

