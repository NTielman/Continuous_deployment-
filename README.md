# Continuous Deployment:

## 3 components and 3 problems I faced:

1. **Setup**: setting up a Github workflow. 
*    How it relates to the other components: It ties all the steps together from a git push to automatic testing and deploying.  
*    A problem I faced with this step: Even after having watched several yaml tutorials, it was unclear to me why certain keys seemed to have a distinct use and expected value within Github actions. It didn't occur to me till later on that "Github workflows" have their own specific syntax. After reading their documentation I became more comfortable writing and practicing with "jobs" and "steps".
2. Test: setting up tests for a flask app. 
*    How it relates to the other components: If this step isn't completed successfully the following component(s) cannot run.
*    A problem I faced with this step: How to write pytests for a flask app, and how to test the output of a variable. Specifically how to combine f'' strings with b'' strings. I was hoping it would be possible to write something like: `assert fb'Tomorrow is {tomorrow.isoformat()}' in response.data` as I needed the string to both contain a variable and be binary at the same time. How I solved it: I didn't, but through reading StackOverflow questions I found out it's possible to combine the two string types like so: `f'{tomorrow.isoformat()}'.encode('utf-8')`
3. Deploy: cloning the modified repository files to the VPS server. 
*    How it relates to the other components: It's the final step and the end result your users get to see and interact with. 
*    A problem I faced with this step: As many co-students faced difficulties dealing with SSH keys not being recognized properly. I researched alternative ways of getting repo files onto a server without having to share sensitive information over Github. A possible solution is through setting up Github action runner from within my VPS. The Github runner automatically places a copy of your repository onto your server. From that point it's only a matter of running ensuing commands to copy/ replace the file being executed by Gunicorn and the server automatically gets updated.  

########

(Edit): The reason I chose to use a github runner in my previous submission instead of logging in on my vps via github actions, was that I was trying to avoid the latter. I saw that plenty of talented students in the vraagbaak were struggling with using github secrets, so I honestly did not even want to try it. After discussing my submission over with Stefan, he challenged me to retry the assignment, this time by logging in to my vps via github (to demonstrate that i understand and grasp how to work with it).

*    Challenges I faced this time: I couldn't figure out how to login to my VPS using a script. I first attempted to write a login.sh file containing the following commands: 
`ssh root@<ip.address>`
`<password>`
`cd path/to/folder`
`git pull `
`systemctl restart mydate.service` 
But this returned an error that `<password>` isn't a command. How could I make the terminal enter the provided password automatically when prompted for it? On stackoverflow I read that i'd have to make use of 'expect' and 'send' commands, by first installing `yum install expect` or make use of a preexisting ssh action on github Marketplace. How I solved it: Other students have mentioned making use of 'appleboy/ssh-action@master' in the vraagbaak, so I decided to read up on how to use it and watch some tutorials on Youtube. By using appleboy's ssh action I was finally able to login to my vps, and run the remaining scripts on my server.