# Assignment_Repo14
Execution Steps :

Pre-Requisite :
================
1)Terraform 
2)AWS CLI 
3)AWS Account 
4)Any IDE( Used VS)


Execution Steps :
==================

1)
Clone this repository
git clone [https://github.com/pattanaiksrimani/Challanges_UK](https://github.com/pattanaiksrimani/Challanges_UK.git)

2) Go to the folder Challange-1 
3) In the provider.tf change the value of the access_key and secret_key as per you aws account 
4) Initialise terraform using :  terraform init
5) terraform validate (to check any syntax )
6) terraform plan 
7) terraform apply 

Testing : 
============
1)After your infrastructure has been created there should be an Output displayed on your terminal for the Application Load Balancer DNS Name.
output "lb_dns_name" {
  description = "The DNS name of the load balancer"
  value       = aws_lb.external-elb.dns_name
}

2)Copy and paste (without quotations) into a new browser tab. Refresh the page to see the load balancer switch between the two instances.
