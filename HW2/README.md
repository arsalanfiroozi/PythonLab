# HW2

## 1-1

#### How to set [shecan.ir](https://shecan.ir) DNS settings on Linux:

![](images/Screenshot%201401-09-05%20at%2008.35.41.png)

#### Using bash scripting:

First of all, we have to install a package to use `resolv.conf` by default:

```bash
sudo apt install resolvconf
```

And now, we can simply edit `/etc/resolv.conf` using this bash script:

```bash
#!/bin/bash

echo "nameserver 178.22.122.100
nameserver 185.51.200.2" | sudo tee /etc/resolv.conf
echo "Done!"
```

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/VirtualBox_Ubuntu2204_26_11_2022_14_55_35.png)

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/VirtualBox_Ubuntu2204_26_11_2022_14_56_26.png)

## 1-2-1

```bash
#!/bin/bash

walk_dir () {
    shopt -s nullglob dotglob

    for pathname in "$1"/*; do
        if [ -d "$pathname" ]; then
            walk_dir "$pathname"
        else
            sudo chmod a+rw "$pathname"
            echo "$pathname"
        fi
    done
}

DIR=\lib

walk_dir "$DIR"
```

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/VirtualBox_Ubuntu2204_26_11_2022_14_58_46.png)

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/VirtualBox_Ubuntu2204_26_11_2022_15_02_31.png)

## 1-2-2

WTF is the usage of BFS in bash script! I can't find any example...

## 1-3

First of all, we have to install a package to log the network informations:

```bash
sudo apt install iftop
```

And now we need a package to email the logged data to another computer:

```bash
sudo apt-get install mailutils
sudo apt-get install ssmtp
sudo apt-get install mpack
```

Configuring the `ssmtp` package is required, but I don't explain how to do it here, you just need to run the below code and edit the text file that just had been opened:

```bash
nano /etc/ssmtp/ssmtp.conf
```

And we use the `mpack` package to send an attachment more easily.

```bash
#!/bin/bash

while [ 1 -gt 0 ]
do
    echo -e "CPU log:\n\n$(grep 'cpu' /proc/stat)" > ~/Desktop/logs/cpu.txt
    echo -e "Devices log:\n\n$(lspci)" > ~/Desktop/logs/devices.txt
    echo -e "Network log:\n\n$(sudo iftop -t -s 40)" > ~/Desktop/logs/network.txt

    zip ~/Desktop/logs/log.zip ~/Desktop/logs/cpu.txt ~/Desktop/logs/network.txt ~/Desktop/logs/devices.txt

    sudo mpack -s "log" ~/Desktop/logs/log.zip maddahgom@gmail.com
    echo "Wait 1 minute"
    sleep 1m
done
```

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/VirtualBox_Ubuntu2204_26_11_2022_22_35_47.png)

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/VirtualBox_Ubuntu2204_26_11_2022_22_36_17.png)

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/VirtualBox_Ubuntu2204_26_11_2022_22_36_24.png)

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/VirtualBox_Ubuntu2204_26_11_2022_22_36_31.png)

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/VirtualBox_Ubuntu2204_26_11_2022_22_36_40.png)

## 1-4

I have no access to the `ftp`.

## 2-1

There are 3 steps to do this part.

#### Step 1: Installing SSH on the Virtual Machine

On the virtual machine, install SSH using the command:

```bash
sudo apt install openssh-server
```

#### Step 2: Configuring the VirtualBox Network

This step is just some VM settings.

#### Step 3: Start Your SSH Session

From the terminal in your main operating system, run the SSH command in the following format:

```bash
ssh -p [Host port] [Guest OS username]@[Guest IP]
```

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/Screenshot%20(9).png)

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/Screenshot%20(10).png)

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/Screenshot%20(12).png)

![](/Users/moghaddam/Documents/GitHub/PythonLab/HW2/images/Screenshot%20(13).png)

## 2-2

`scp` (secure copy) is a command-line utility that allows you to securely copy files and directories between two locations.

The `scp` command syntax take the following form:

```bash
scp [OPTION] [user@]SRC_HOST:]file1 [user@]DEST_HOST:]file2
```

In our case, we use this command as below:

```bash
scp test.txt mohammad@127.0.0.1:/home/mohammad/Desktop/temp
```

And the output is:

```
mohammad@127.0.0.1's password:
test.txt                             100%    0     0.0KB/s   00:00
```
