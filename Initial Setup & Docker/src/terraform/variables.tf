variable "region" {
  type = string
  default = "us-east-2"
}

variable "security_group_id" {
  type = list
  default = ["sg-04bd332e169e1c413"]
}

variable "vpc_id" {
  type = string
  default = "vpc-0e27197f4430ac7c7"
}

variable "ami_id" {
  type = string
  default = "ami-0e820afa569e84cc1"
}

variable "key_pair" {
  type = string
  default = "Thinkpadkey"
}

variable "instance_type" {
  type = string
  default = "t2.medium"
}
