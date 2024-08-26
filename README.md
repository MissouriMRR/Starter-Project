# Welcome  --Start Here--
This is a Github repo for starter projects for new members.

To get started coding make sure you have a access to Linux, ubunto 22 is recommended, but others will most likely work. This is most likely through a virtual machine on your windows device. If you don't have a Virtual machine set up pelase navigate [here](https://missourimrr.github.io/docs/virtual_machines/).

### First steps before you start coding
Before getting the code your device needs to be setup. If you have ran these commands feel free to skip them.

First thing you need to do is ensure python 3.10 is installed open a terminal in Linux and type in
```
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
```
This installs python 3.10 and ensures it will be used when running our code.
You can verify with
```
python3.10 -V
```
It should return with python3.10.4 or above if not try running
```
sudo apt update
```

Next is installing git. Run
```
sudo apt install git
```
if you haven't already

Next ssh needs to be setup. In a terminal in your hame directory Run this command but replace the email with the email you used for your github account.
```
ssh-keygen -t rsa -C "you@example.com"
```
hit enter when prompted with a location. Next run
```
cd .ssh
cat id_rsa.pub
```
and copy the output. Then navigate to Github click on your profile pic in the top right and navigate to settings then ssh and gpg keys. add a new ssh key give it a title and paste what you copied in the key section.

### Finally starting on coding
This repo needs to be cloned to your device. That means that the copies of the files are downloaded on your computer to be edited that you can then later upload back up to the repo to share with others. The repo means repository it is just the centralized location where we store and share our code.
Next is cloning the repo. Select the green <>Code button for this repo, and choose clone with ssh and copy it. Then in a terminal run the following command with what you copied.
```
git clone [what you copied (remove the square braces)]
```

Next you need to create a branch. This just separates your code from the original branch, so whatever you push doesn't overwrite anything that you or anyone else pushes to the repo. Run
```
git checkout -b [Your Name]-[Software subteam]-StarterProjects
```

Now you are all setup, make sure to follow your subteams installation guide. If you don't know what that is navigate to your subteams docs from [here](https://missourimrr.github.io/docs/flight/). Feel free to try out or change subteams as you like no pressure to stick with a certain one.

Get to coding!!!!

### Once Complete
When you have finished the starter projects and tested to confirm they work. THe work you have done needs to be added, committed, and pushed. Run
```
git status
```
This shows all of the files you have changed. For the files you want added to commit Run
```
Git add [file]
```
For the files you don't want added
```
Git restore [file]
```

Next the files need to be committed. Run
```
Git commit -m "[add in a nice little message about what you changed]"
```
Then run
```
Git push
```
If you haven't pushed with this branch yet it will give you a command to run instead go ahead and type that in and run it.

Congratulations Your code is now pushed to your own branch on the repo.

## Useful Links
[Multirotor Docs](https://missourimrr.github.io/docs/) Has a lot of info on all software teams and technologies we use, reference there if you have any questions.
[Multirotor Github](https://github.com/MissouriMRR) even though you are already here it has lots of examples of how to use python and the libraries we use in many of the repos. Often times something similar may have been done before.
