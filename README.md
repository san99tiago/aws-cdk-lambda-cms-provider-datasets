# :white_check_mark: AWS CDK LAMBDA CMS PROVIDER DATASETS DOWNLOAD :white_check_mark:

<img src="assets/CDK_Lambda_CMS_Provider_files_download.png" width=90%> <br>

The initial challenge can be found at: [`CMS_providers_data_download_instructions.pdf`](CMS_providers_data_download_instructions.pdf). <br>

This is a custom cloud-native solution deployed on AWS with the following specifications:

- Infrastructure as Code with [AWS CDK](https://aws.amazon.com/cdk/)
- Source Code with [AWS Lambda Functions](https://aws.amazon.com/lambda/) built with [Python Runtime](https://www.python.org)
- Deployment Strategies: CDK commands (please read the [`important_commands.sh`](important_commands.sh) script).

The information of this repository is based on many online resources, so feel free to use it as a guide for your future projects!. <br>

## AWS CDK :cloud:

[AWS Cloud Development Kit](https://aws.amazon.com/cdk/) is an amazing open-source software development framework to programmatically define cloud-based applications with familiar languages. <br>

My personal opinion is that you should learn about CDK when you feel comfortable with cloud-based solutions with IaC on top of [AWS Cloudformation](https://aws.amazon.com/cloudformation/). At that moment, I suggest that if you need to enhance your architectures, it's a good moment to use these advanced approaches. <br>

The best way to start is from the [Official AWS Cloud Development Kit (AWS CDK) v2 Documentation](https://docs.aws.amazon.com/cdk/v2/guide/home.html). <br>

## Dependencies :vertical_traffic_light:

The dependencies are explained in detail for each project, but the most important ones are Python and AWS-CDK. <br>

My advice is to primary understand the basics on how CDK works, and then, develop amazing projects with this incredible AWS tool!. <br>

### Software dependencies (based on project)

- [Visual Studio Code](https://code.visualstudio.com/) <br>
  Visual Studio Code is my main code editor for high-level programming. This is not absolutely necessary, but from my experience, it gives us a great performance and we can link it with Git and GitHub easily. <br>

- [Docker](https://www.docker.com/) <br>
  Docker is a platform designed to help developers build, share, and run modern applications. It uses OS-level virtualization techniques to deliver software packages known as "containers". It is used in this project as one of the building tools for creating the Lambda-function Docker images that will run the automation.<br>

- [Python](https://www.python.org/) <br>
  Python is an amazing dynamic programming language that let us work fast, with easy and powerful integration of different software solutions. <br>

### Libraries and Package dependencies (based on project)

- [CDK CLI (Toolkit)](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) <br>
  To work with the CDK, it is important to install the main toolkit as a NodeJs global dependency. Then, feel free to install the specific language AWS-CDK library (for example: [aws-cdk.core](https://pypi.org/project/aws-cdk.core/). <br>

- [Selenium (Python-based)](https://pypi.org/project/selenium/) <br>
  The selenium package is used to automate web browser interaction from Python. It is one of the core components for Web-Scrapping tools. My advice is to only use Selenium if it is really needed (e.g. advanced web interactions).<br>

## Usage :dizzy:

All projects are well commented/documented and most of them have specifications and remarks for their purpose and I/O. <br>

I will be uploading most of the files, and try to keep it as clean as possible. <br>

## Special thanks :gift:

- Thanks to all contributors of the great OpenSource projects that I am using. <br>

## Author :musical_keyboard:

### Santiago Garcia Arango

<table border="1">
    <tr>
        <td>
            <p align="center">Senior DevOps Engineer passionate about advanced cloud-based solutions and deployments in AWS. I am convinced that today's greatest challenges must be solved by people that love what they do.</p>
        </td>
        <td>
            <p align="center"><img src="assets/SantiagoGarciaArangoCDK.png" width=60%></p>
        </td>
    </tr>
</table>
