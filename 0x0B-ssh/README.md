# 0x0B. SSH

<p align="center">
    <img src="https://assets-global.website-files.com/5ff66329429d880392f6cba2/61c1b963247368113bbeef17_Secure%20Shell%20work.png" size="400">
</p>

## Background Context

<p>
    <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/244/zPVRKhPsUP5lK.gif">
</p>

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of a previous project shared in your intranet profile.

You can access your server information in the my servers section of the intranet, each line with contains the IP and username you should use to connect via ssh.

Note: Your server is configured with an Ubuntu 20.04 LTS environment.

### Resources

**Read or watch:**

- [What is a (physical) server - text]()
- [What is a (physical) server - video]()
- [SSH essentials]()
- [SSH Config File]()
- [Public Key Authentication for SSH]()
- [How Secure Shell Works]()
- [SSH Crash Course]() (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)
- [For reference:]()

**Understanding the SSH Encryption and Connection Process**

- [Secure Shell Wiki]()
- [IETF RFC 4251 (Description of the SSH Protocol)]()
- [Internet Engineering Task Force]()
- [Request for Comments]()

**man or help:**

- ssh
- ssh-keygen
- env

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

### General

- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- he advantage of using #!/usr/bin/env bash instead of /bin/bash
