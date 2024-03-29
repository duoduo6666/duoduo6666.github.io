# 安装 SSH 服务端 (OpenSSH)
<python-script>{state}</python-script>

## 安装

### Ubuntu
在 Ubuntu 终端运行: 
```bash
sudo apt -y install openssh-server
```

---

## 连接
在终端运行: 
```bash
# -q 可选 大多数警告将被屏蔽
# username 替换为登录时的用户名
# ip 替换为服务端 ip 或域名
ssh -q username@ip
```
输入 exit 或者 <kbd>Ctrl</kbd>+<kbd>D</kbd> 关闭 SSH 链接

### 使用私钥登录
在服务端生成公钥和私钥文件: 
```bash
ssh-keygen -q -N -P -f ~/.ssh/id_rsa -b 4096 -t rsa
```

安装公钥到服务端: 
```bash
mv ~/.ssh/id_rsa.pub ~/.ssh/authorized_key
service sshd restart
```

下载私钥文件:
```bash
# username 替换为登录时的用户名
# ip 替换为服务端 ip 或域名
# 在 .ssh/ 末尾添加文件名可以指定文件名
# 如果 scp 弹出 Enter passphrase for key xxx 直接回车即可
cd ~
scp username@ip:~/.ssh/id_rsa .ssh/
```

使用刚才下载的私钥登录: 
```bash
# passphrase 替换为刚才下载的私钥文件默认为.ssh/id_rsa
# username 替换为登录时的用户名
# ip 替换为服务端 ip 或域名
ssh -i passphrase username@ip
```

### 保存连接信息
在.ssh目录新建config文件  
Windows:
```PowerShell
echo "" > ~/.ssh/config
```
linux:
```bash
touch ~/.ssh/config
```

添加服务端到config文件
Host 服务端名称
  HostName ip或域名
  Port 端口
  User 用户名
  IdentityFile 私钥文件  

示例: 
```
Host server1
  HostName 10.0.0.2
  User root
  IdentityFile ~/.ssh/develop.rsa
Host server2
  HostName 10.0.0.3
  User root
  IdentityFile ~/.ssh/develop.rsa
```

测试示例: 
```bash
ssh server1
```
输入 exit 或者 <kbd>Ctrl</kbd>+<kbd>D</kbd> 关闭 SSH 链接

---
## 管理
开启 SSH 服务:
```bash
service ssh start
```
停止 SSH 服务:
```bash
service ssh start
```
重启 SSH 服务: 
```bash
service ssh restart
```
查看 SSH 服务状态: 
```bash
service ssh status
```