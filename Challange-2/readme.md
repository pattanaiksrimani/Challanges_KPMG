•	Pre-Requisite for the solution :
1)	Create EC2 Instance 
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html 
2)	Install Python and git
3)	Install pipenv
4)	Install project dependencies using  for creating virtual Env        
                                        pipenv install
•	SSH to the ECS instance use the link for details : 
https://www.youtube.com/watch?v=jv-dgOfFN4o
•	Once you are connected to the EC2 instance copy the script to EC2 instance from git :
              https://github.com/pattanaiksrimani/Challanges_UK/blob/main/Challange-2.py
•	Copy the script to EC2 instance and run it :
Sample OutPut :


[ec2-user@ip-172-31-22-154 aws_metadata_in_JSON]$ python3 metadata_to_json.py
{
    "meta-data": {
        "ami-id": "ami-06640050dc3f556bb",
        "ami-launch-index": 0,
        "ami-manifest-path": "(unknown)",
        "block-device-mapping": {
            "ami": "/dev/sda1",
            "root": "/dev/sda1"
        },
        "events": {
            "maintenance": {
                "history": [],
                "scheduled": []
            }
        },
        "hostname": "ip-172-31-22-154.ec2.internal",
        "identity-credentials": {
            "ec2": {
                "info": {
                    "AccountId": "104529772138",
                    "Code": "Success",
                    "LastUpdated": "2022-09-13T12:43:58Z"
                },
                "security-credentials": {
                    "ec2-instance": {
                        "AccessKeyId": "ASIARQVTVXZVA3GMML4C",
                        "Code": "Success",
                        "Expiration": "2022-09-13T19:10:41Z",
                        "LastUpdated": "2022-09-13T12:43:21Z",
                        "SecretAccessKey": "6wmNOepLKEp4OLrM25cExSC3liw97jRTntySiR4P",
                        "Token": "IQoJb3JpZ2luX2VjEA0aCXVzLWVhc3QtMSJHMEUCIFjW0u6eg42z1fq2Q4pt8IReCsExRlpvQ80KnEemwmCJAiEA/KS7tiNTaqpAfM/SF+/pP9mH7n3KBTo4KV/+exWdivoqsQQIpv//////////ARADGgwxMDQ1Mjk3NzIxMzgiDEY/WNZuzGqLIColDCqFBLGUGRhJDnCHcN/xHoUcwhObHwg5rPB4DQFsOY4C0CocwdLOe84TVodkSE6hZdW46PwxWP08HZ623KIikRZlsy/qzAdQiRcDSwLhB9vKIFD/8LIn9t99uEPKNkSrBk8TKLGJ8WCnzO/mrKOBdkHmb7exdro9VpUC3B5DZgn1uMcoLZjhChHxhYH+AN2ptbzF0MmYc+lFZ9JfQ/bFkZesTsS3ojnYxUK5edggtZyobT2xfF+FXo9w4f9U158jQUXgvrocWtoNLOrNbtBO81mDPi1ZeYgjD+TTzrQy4CV8BriHBdDOuHDNsiyaeNq75QYmwxvJVQVEpo7yUiw5anBF3NB4h/n7GuCEU+2pKlYOGtmHJDnXmqlawMLjXSrojnTBZ60ZC9kxM25Q6xT2VHyldJm//BzfFRmBOcd46f7UR/KAZUBEQQFJGPVWJ0m2+VdHzzItxpUGWUQQH1wU4m94Ydx7DpLWVPmVyQKZX1ea4xO5tnuQGEJjLPg8eKeLipeGiBzrWv54iKWY1uMAiO5fETfJJuBe0meKNa4SmFT2cmpKKfNRm04hGDT2Owk/QRP+cweDxxOwSISvVIrS2Zknyx/CHUYTR3AWUc++Ien2wTa0Tr7LuNAB5/WZfAcnkmFfpOs0FcBiYbCt6FU45s8Zf63tIKES/+0XsnPnFZv6vZrtBlbL3uow4vWBmQY6jwKM1lJ03FbBl+kawzOe8qule3/ypusvPIBk16s2gKlnAz295ixyL6/E05lsHmIkKZOIimUjaTjM/2DTFVp5YeUkmI1D9RIF+ogjNER909ePB0BszRwL5SPXiSCNTB+a8VxyywPi22+XIJNwSPh7uBoWmcl/a7KmB7ov1mh9OiBjl/O8zPBadhUfj9hbrFtr89qCyUcFy91tB4bwAO36FuqlpcP2EibZh8HxQMh18D795BBoeaitBytVlRc31DSdi1tfgLr3JAlHB3jmLtH6WRM9f1eGib/n3oF3qnwGs2olTdiKPmqbGOc0mkLjj+zIqeBTku9X8syReLVPNlf7TXTmL9E/mhhDHYFYv8o93WZp",
                        "Type": "AWS-HMAC"
                    }
                }
            }
        },
        "instance-action": "none",
        "instance-id": "i-0928e6d2c01fc8862",
        "instance-life-cycle": "on-demand",
        "instance-type": "t2.micro",
        "local-hostname": "ip-172-31-22-154.ec2.internal",
        "local-ipv4": "172.31.22.154",
        "mac": "0a:94:46:7e:22:4f",
        "metrics": {
            "vhostmd": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        },
        "network": {
            "interfaces": {
                "macs": {
                    "0a:94:46:7e:22:4f": {
                        "device-number": 0,
                        "interface-id": "eni-0b03a02dd31c153c5",
                        "ipv4-associations": {
                            "18.209.51.214": "172.31.22.154"
                        },
                        "local-hostname": "ip-172-31-22-154.ec2.internal",
                        "local-ipv4s": "172.31.22.154",
                        "mac": "0a:94:46:7e:22:4f",
                        "owner-id": 104529772138,
                        "public-hostname": "ec2-18-209-51-214.compute-1.amazonaws.com",
                        "public-ipv4s": "18.209.51.214",
                        "security-group-ids": "sg-0acba04aed3c4b5de",
                        "security-groups": "launch-wizard-1",
                        "subnet-id": "subnet-b58485f8",
                        "subnet-ipv4-cidr-block": "172.31.16.0/20",
                        "vpc-id": "vpc-3a62ef47",
                        "vpc-ipv4-cidr-block": "172.31.0.0/16",
                        "vpc-ipv4-cidr-blocks": "172.31.0.0/16"
                    }
                }
            }
        },
        "placement": {
            "availability-zone": "us-east-1a",
            "availability-zone-id": "use1-az4",
            "region": "us-east-1"
        },
        "profile": "default-hvm",
        "public-hostname": "ec2-18-209-51-214.compute-1.amazonaws.com",
        "public-ipv4": "18.209.51.214",
        "public-keys": {
            "0=myserver07": "<?xml version=\"1.0\" encoding=\"iso-8859-1\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\"\n\t\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\">\n <head>\n  <title>404 - Not Found</title>\n </head>\n <body>\n  <h1>/h1>\n </body>\n</html>\n"
        },
        "reservation-id": "r-053175f06eefaa07b",
        "security-groups": "launch-wizard-1",
        "services": {
            "domain": "amazonaws.com",
            "partition": "aws"
        }
    }
}

What key details you like to view ?

local-ipv4s
['172.31.22.154']
[ec2-user@ip-172-31-22-154 aws_metadata_in_JSON]$

