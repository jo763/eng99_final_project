# Testing 

## Project Diagram 

Project Overview

![](img/project_diagram.svg)

## Aim of the Project
### The aim of this project is to successfully deploy a web app on a browser by building a CI/CD pipeline on Jenkins.
Task:
- Fix bugs on the python app and test using TTD on Pytest 
- Push to Dev branch on github 
- Build a Jenkins server on an EC2 instance on AWS
- Create a webhook and first job in the pipeline is to test the git commit and merge to main branch (pytest has to pass)
- Create an AWS environment to run the app
- Containerise the app and upload image to dockerhub 
- Create an EC2 instance to run the containerised app
- Check app is available on browser
- Generate HAR file to generate Scala script to run gatling tests
- Create a Gatling Instance 
- Monitor using CloudWatch and Grafana 
- Create an S3 bucket with the CSV file for disaster recovery
- Create a webhook trigger to send emails once a docker image is uploaded to the repo

