
provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "terraform_sg" {
  name_prefix = "terraform-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] 
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web" {
  ami           = "ami-0e86e20dae9224db8" 
  instance_type = "t2.micro"

  key_name        = "vockey"
  security_groups = [aws_security_group.terraform_sg.name]

  tags = {
    Name = "Terraform-EC2"
  }
}

output "instance_public_ip" {
  value = aws_instance.web.public_ip
}