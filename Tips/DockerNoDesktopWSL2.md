# Docker on Windows WSL2 without Docker Desktop

## Docker in Windows WSL2

Taken from [dev.to](https://dev.to/felipecrs/simply-run-docker-on-wsl2-3o8)

```bash
sudo apt update
sudo apt dist-upgrade
sudo apt autoclean
sudo apt autoremove
sudo apt install ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo apt autoclean
sudo apt autoremove
sudo apt dist-upgrade
```

**Issue with iptables need the old one**

Now start docker:

```bash
sudo service docker restart
```

Check if it is running:

```bash
sudo service docker status 
```

If it failed, check logs:

```bash
tail -100 /var/log/docker.log
```

I had an issue:

```
failed to start daemon: Error initializing network controller: error obtaining controller instance: failed to register "bridge" driver: unable to add return rule in DOCKER-ISOLATION-STAGE-1 chain:  (iptables failed: iptables --wait -A DOCKER-ISOLATION-STAGE-1 -j RETURN: iptables v1.8.7 (nf_tables):  RULE_APPEND failed (No such file or directory): rule in chain DOCKER-ISOLATION-STAGE-1 (exit status 4))
```

Reference links:

- [Unix Stack Exchange](https://unix.stackexchange.com/questions/767754/launching-docker-daemon-in-ubuntu-22-04-lts-on-wsl-2-fails-because-of-iptables)
- [Crapts](https://crapts.org/2022/05/15/install-docker-in-wsl2-with-ubuntu-22-04-lts/)

Run the following command:

```bash
sudo update-alternatives --config iptables
```

Enter 1 to select iptables-legacy. Now run `sudo service docker start`, and Docker will start as expected!

```bash
sudo service docker restart
sudo service docker status 
```

It should be ok.

## Add group and your user for docker

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

**Important:** Then logout and relogin to have the group for your user.

## Oracle 23 Free Version

### Basic Test

```bash
docker run --name testdb -p 1521:1521 -e ORACLE_PASSWORD="oracle" gvenzl/oracle-free:23-slim
```

It takes a long time.

Then inside another terminal:

```bash
docker exec -it testdb bash
```

Run:

```bash
sqlplus / as sysdba
```

Inside SQLPlus:

```sql
show USER;
SELECT NAME FROM v$database;
```

Exit SQLPlus:

```sql
exit;
```
```
