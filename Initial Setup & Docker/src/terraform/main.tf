resource "aws_instance" "ec2_dev" {
  instance_type          = var.instance_type
  ami                    = var.ami_id
  vpc_security_group_ids = var.security_group_id
  key_name               = var.key_pair

  root_block_device {
    volume_size = 20
  }
  tags = {
    Name = "terraform_test"
  }

  user_data = <<-EOL
  #!/bin/bash -xe

  sudo su
  yum update -y
  yum install docker -y
  systemctl start docker
  yum install git
  EOL
}