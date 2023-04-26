# PiWebServer

A webserver designed to run on a raspberry pi, providing useful details and capable of hosting other sites.

## Access

Currently designed to use [Serveo](https://serveo.net) to proxy:
 - The webserver (running on port 5000), accessible at [krishnans2006.serveo.net](https://krishnans2006.serveo.net/)
 - An SSH terminal, using `ssh -J serveo.net krishnan@krishnans2006`

## Design

Current webserver routes:
 - `/temp` - monitor the CPU temperature of your pi
