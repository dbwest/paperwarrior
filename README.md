## paperwarrior -- a taskwarrior tasksh for raspberry pi with eink 

https://gm1.ggpht.com/e0QiDjIYJXFnRFBVX1RfuUCJ9tuQSYQNF8ZBDlgtaEKVf8danlP3PvYSsT0MfJidk4nUCvIuYez57BO2F5RqPm04GmAhPbcVVp5qmZVWmuYhMOjYSiV6ZK7_wVjtUzO-RDKvWzVEp3VNhqo7NiZ57edfdcU3fdtFU_nxJzT1VPVnC-Gtgku_jJdUcw4S9vVQQ3pA9fFeWPZIX6BItQ3p6M5N_ZrY4x3cECLlHhN9Ijv5hgv7vXrlTF6S8It11cljEX7xsLrruF39LSEJuBe9cxy2CppkYcu8Acj9nhs3EXW_vqoFgIsCUkkhiYGRNvmoc72bum7mG4tazKELwpB5ahBlBqoklTPzf6WIojBpGP0riAk_WctVbe600eB8NknRoPDalN77l-Fqqgra3w_hDN_MB5wuJjIDV-FxgXvrC9Sh_NdEEG0h46xqSiNTzZAocp7py5SK8MDYtsO7lDNJBsQDnM-t53v_kOztQwY5TKnkAuLQQYSmW6PUn0E_0INIQfS1nyxGz9sL5kdBj1VqWngUF2FbH3zj8xIvQu2I_1LtpGyjARhGgB6PHllzgihXHtJJ8_scYf5EhSG0XqLo_cYDAZvB_gZBaYu2in4lHzRiYyhSmt5fBjgYShwPAKp6Xbpob3WrS-N0iar6dmaH3oTWq0RYEqVdVgwXsy3WzxpGSLip7WCZJbsRMLYUJhMzUpr0aR9ikV96BHp_RUOk2IauEw8LFyYkFRikcorv10PC5VPagCblbHydXUh9qgXhUw=s0-l75-ft-l75-ft

1. Make a new project in balena called 'paperwarrior'
2. Install balena cli using instructions on balena site
3. login with balena cli using `balena login`
4. from this directory `balena push paperwarrior --source .`
5. add devices using balena dashboard for app
6. burn microsds or appropriate media for all devices with balena etcher to deploy

### on startup

You can just plug in a keyboard...

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
