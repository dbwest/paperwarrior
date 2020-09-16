## paperwarrior -- a taskwarrior tasksh for raspberry pi with eink 

1. Make a new project in balena called 'paperwarrior'
2. Install balena cli using instructions on balena site
3. login with balena cli using `balena login`
4. from this directory `balena push paperwarrior --source .`
5. add devices using balena dashboard for app
6. burn microsds or appropriate media for all devices with balena etcher to deploy

This is tested and made to work with raspberry pis and the waveshare 2 color 2.13" v2 eink hat

YMMV with other setups and you will likely need to change the CMD in the Dockerfile to use another driver if using another setup.

This project borrows heavily from the papertty Python library. Look at it (recommended). 

[balena-link]:https://balena.io/
[signup-page]:https://dashboard.balena-cloud.com/signup
[gettingStarted-link]:http://balena.io/docs/learn/getting-started/
