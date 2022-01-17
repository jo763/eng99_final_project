provider "aws"{
  region = "eu-west-1"
}

resource "aws_instance" "app_instance" {
  ami = var.app_ami_id
  instance_type = "t2.micro"
  
  associate_public_ip_address = true

  subnet_id = aws_subnet.eng99_final_project_SN.id
  vpc_security_group_ids = [aws_security_group.eng99_final_project_sg.id]

  key_name = var.aws_key_name
  tags = {
    Name = "eng99_final_project_app"
  }
}

resource "aws_vpc" "eng99_final_project_VPC"{
  cidr_block = var.cidr_block

  tags = {
    Name = "eng99_final_project_VPC"
  }
}

resource "aws_subnet" "eng99_final_project_SN" {
  vpc_id     = aws_vpc.eng99_final_project_VPC.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone = "eu-west-1a"

  tags = {
    Name = "eng99_final_project_SN"
  }
}

resource "aws_internet_gateway" "eng99_final_project_igw" {
  vpc_id = aws_vpc.eng99_final_project_VPC.id

  tags = {
    Name = "eng99_final_project_igw"
  }
}

resource "aws_route_table" "eng99_final_project_rt" {
  vpc_id = aws_vpc.eng99_final_project_VPC.id

  route  {
      cidr_block = "0.0.0.0/0"
      gateway_id = aws_internet_gateway.eng99_final_project_igw.id
    }

  tags = {
    Name = "eng99_final_project_rt"
  }
}

resource "aws_route_table_association" "eng99_final_project_associate" {
  route_table_id = aws_route_table.eng99_final_project_rt.id
  subnet_id = aws_subnet.eng99_final_project_SN.id
}


resource "aws_security_group" "eng99_final_project_sg" {
  name        = "eng99_final_project_sg"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.eng99_final_project_VPC.id

  ingress {
    description      = "Allow public access"
    from_port        = 3000
    to_port          = 3000
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "ssh public access"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "All traffic"
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1" 
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "eng99_final_project_sg"
  }
}