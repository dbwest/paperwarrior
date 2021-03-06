## paperwarrior -- a taskwarrior tasksh for raspberry pi with eink 

Why? Run taskwarrior/tasksh with an eink interface to get a little more screen minimal and still GTD (get things done)

Haven't seen the light on taskwarrior/tasksh yet? See the following
- [taskwarrior.org](https://taskwarrior.org)
- [Taskwarrior, where have you been all my life?](https://blog.djy.io/taskwarrior-where-have-you-been-all-my-life/)

BOM (Bill of Materials):
- raspberry pi zero w with headers (~$30)
- waveshare v2 2.13" eink hat (~$25)
- usb keyboard

![Picture](./assets/paperwarrior.jpg?raw=true)

1. Make a new project in balena called 'paperwarrior'
2. Install balena cli using instructions on balena site
3. Login with balena cli using `balena login`
4. From this directory `balena push paperwarrior --source .` The project will build and you should see a unicorn
5. Add devices using balena dashboard for app
6. Burn microsds or appropriate media for all devices with balena etcher to deploy

### on startup

After inserting burned media from the balena project and plugging the power in for the pi you will need to wait several minutes for balenaOS to start up and sync the application.

You can just plug in a keyboard to get input, but then you have to...

Currently this starts up in balenaOS, not the container that has tasksh (need to figure that out next)

You will need to
1. type 'root' to login as root (no pass needed)
2. type balena ps and find the id of the main service container
3. type `balena exec -it <id> bash` (get a bash shell in the container)
4. type `tasksh` to get the task shell for taskwarrior :)
5. GTD ( Get things done ;) )

This is tested and made to work with raspberry pis and the waveshare 2 color 2.13" v2 eink hat

YMMV with other setups and you will likely need to change the CMD in the Dockerfile to use another driver if using another setup.

This project borrows heavily from the papertty Python library. Look at it (recommended). 

[balena-link]:https://balena.io/
[signup-page]:https://dashboard.balena-cloud.com/signup
[gettingStarted-link]:http://balena.io/docs/learn/getting-started/
