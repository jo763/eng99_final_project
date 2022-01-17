resource "aws_s3_bucket" "bucket" {
   bucket = "eng99-final-project-s3"
   versioning {
      enabled = true
   }
   tags = {
     Name = "eng99-final-project-s3"
     Environment = "Dev"
   }
}
