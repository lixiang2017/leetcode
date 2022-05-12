## test for linux namespace, docker
## chroot, namespace, cgroup
## ref
https://www.cnblogs.com/bakari/p/8560437.html


### 1 example for uts namespace
[root@office0 test_namespace]# gcc -o uts 1uts.c
[root@office0 test_namespace]# ./uts
程序开始
在容器进程中！


### 2 example for uts2, change hostname in container
[root@office0 test_namespace]# gcc -o uts2 2uts.c
[root@office0 test_namespace]# ./uts2
程序开始
在容器进程中！
[root@container test_namespace]#

### 3 example for ipc
[root@office0 ~]# ipcmk -Q
Message queue id: 0
[root@office0 ~]# ipcs -q

------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages
0x055b83c9 0          root       644        0            0


[root@office0 test_namespace]# ./ipc
程序开始
在容器进程中！
[root@container test_namespace]# ipcs -q

------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages


### 4 example for pid
[root@container test_namespace]# echo $$
5575
[root@container test_namespace]# ./pid
程序开始
在容器进程中！
[root@container test_namespace]# echo $$
1
[root@container test_namespace]# ps -elf | head -3
F S UID        PID  PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
4 S root         1     0  0  80   0 - 49583 ep_pol  2021 ?        00:23:26 /usr/lib/systemd/systemd --switched-root --system --deserialize 21
1 S root         2     0  0  80   0 -     0 kthrea  2021 ?        00:00:07 [kthreadd]
