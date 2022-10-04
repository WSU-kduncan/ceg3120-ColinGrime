## Part 1 - Build a VPC

1. **VPC**  
![vpc](https://github.com/WSU-kduncan/ceg3120-ColinGrime/blob/main/Project2/screenshots/vpc.png)   
- A VPC (Virtual Private Cloud) allows you to create a virtual network so that you can launch AWS resources that you define.
  
2. **Subnet**  
![subnet](https://github.com/WSU-kduncan/ceg3120-ColinGrime/blob/main/Project2/screenshots/subnet.png)
- A subnet is a range of IP addresses in your VPC.
  
3. **Internet Gateway**   
![internet gateway](https://github.com/WSU-kduncan/ceg3120-ColinGrime/blob/main/Project2/screenshots/gateway.png)
- An Internet Gateway allow resources in your public subnets to connect to the internet. It supports both IPv4 and IPv6 traffic.
  
4. **Routing Table**  
![route table](https://github.com/WSU-kduncan/ceg3120-ColinGrime/blob/main/Project2/screenshots/route-table.png)
- A Routing Table defines a set of rules (or routes) that determine where network traffic from your subnet or gateway is directed.
  
5. **Security Group**  
![security group](https://github.com/WSU-kduncan/ceg3120-ColinGrime/blob/main/Project2/screenshots/security-group.png)   
- A Security Group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic.
  
## Part 2 - EC2 instances

1. AMI
  - Name: `ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20220912` 
  - Description: `Canonical, Ubuntu, 22.04 LTS, amd64 jammy image build on 2022-09-12`
  - Platform: `Linux/UNIX`
  - Architecture: `x86_64`
  - Default username: `ubuntu`
  - Type: `t2.micro`
    
2. In order to attach the instance to my VPC, I clicked on the "Configure Instance Details" tab, went to Network, and clicked on my created VPC.

3. Since we are going to request/associate an Elastic IP to the instance, you do not have to auto-assign a Public IPv4 address.

4. I went with the `General Purpose SSD` Volume with `16 GB`.

5. To tag my instance with a name, I changed the key name to `GRIMES-instance`.

6. To associate my security group, I clicked on the "Choose an Existing Security Group" tab, and clicked on `GRIMES-SG`.

7. To reserve an Elastic IP address, I went to the "Actions" tab, clicked on `Associate Elastic IP address`, and selected my instance/IP address.

8. ![ec2](https://github.com/WSU-kduncan/ceg3120-ColinGrime/blob/main/Project2/screenshots/ec2.png)   

9. To change my hostname to "GRIMES-AMI", I ran the command `sudo hostnamectl set-hostname GRIMES-AMI --static` and restarted the connection.
  
10. ![host-name](https://github.com/WSU-kduncan/ceg3120-ColinGrime/blob/main/Project2/screenshots/host-name.png)
