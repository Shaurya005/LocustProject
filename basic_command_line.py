from locust import HttpUser, task, between


# The way to convert a locust script to HttpLocust script is by using HttpUser which itself has inherited User
class MyUser(HttpUser):
    # pass

    wait_time = between(1, 2)
    host = "http://newtours.demoaut.com/"

    # Command for directly providing host in command line while running locust script - locust -f http_locust.py --host="http://newtours.demoaut.com/"

    @task
    def login_URL(self):
        print("I am logging into URL")


# So far we have been able to create very basic local script and add very basic mandatory attributes to local script.

# Let's see what are the command line parameters available in locust and what is the help available in locust.
# and first I detach terminal and type locust --help. Very straightforward way to know what are the features available in locust and their help.

# And you have a long list of options related to each other and nicely categorized so that you can use them.
# So we will be using many of these options as we move across different sections.

# In next lecture, we will see the use of often use parameters which are as below

# --headless : to run test in non-web mode.
#
# --u, --users      : for defining users
# --r, --hatch-rate : for defining hatch rate,
# --t, --run-time   : for defining runtime and
# --logfile         : for redirecting output to log file.

# And we'll be using these options many times in many of our lectures.



# So far we ran our scripts with web interface. In this lecture, we will learn how to run our script without web interface using command line parameters.
#
# To run our script, we have to enter :
#
#         locust -f basic_command_line.py -u 5 -r 1 -t 10s --headless --logfile logfiles/mylog.log --loglevel DEBUG
#
# To define number of users, we have to give either -u or --users then we give number of users.
#
# To define hatch rate, we have to give -r or --hatch-rate and I can define hatch rate, which is 1 user per second, which implies that every second one user will arrive and hence five users will arrive in five seconds.
#
# To define runtime, we have to give -d or --run-time option and we can define time in seconds, minutes or hours by providing the unit like 60s or 1m and all of these command line options are used in conjunction with --headless mode.
#
# So let me run this script. So my script starts running without going to web interface. Let me stop the script we should have given less time and this time we'll give less time i.e. 10s.
#
# I also want to do one more thing over here. I want to redirect my log file output to some log file and here I have to give --logfile option along with the location where I want to save my log file.
# So I want to save my log file in my directory logfiles, which I just created so I'll give --logfile logfiles/mylog.log. And I can also define the log level by giving --loglevel. By default, which is info and I can set it to DEBUG.
#
# Okay, let me run this again. So this script should end in 10s and which it ends.
#
# And let's have a look at log file. So there is a log file created over here and it has very less content.
# We have to note that stats are not printed in this log file, only the messages, right so if you have any error message or if you have configured any customized message that will be redirected to this log file.
# So these were some of the options which we will be using often. Let's move to our next lecture.
