````markdown
# 🚀 AWS EC2 Management with Boto3

This project is a hands-on experiment using **Boto3** (AWS SDK for Python) to **create**, **start**, **stop**, and **terminate** an **Amazon EC2 instance** via Python scripts.

## 📌 Objectives

- Understand how to programmatically manage AWS EC2 resources.
- Use Boto3 to perform key EC2 operations.
- Learn best practices for AWS automation.

---

## 🧰 Tech Stack

- **Language**: Python 3.x
- **AWS SDK**: Boto3
- **AWS Services**: EC2
- **Tools**: AWS CLI, IAM Role with proper permissions

---
````

## 📂 Project Structure

```bash
.
├── ec2-create.py       # Script to create a new EC2 instance
├── ec2-start.py        # Script to start an existing instance
├── ec2-stop.py         # Script to stop a running instance
├── ec2-terminate.py    # Script to terminate an EC2 instance
├── .env                # Python dependencies
├── .gitignore          # gitignore to mask the AMI/Instance IDs in .env
└── README.md           # You're here!

````

---

## 🔐 Prerequisites

* An **AWS account**
* AWS CLI configured with `aws configure`
* IAM user with `EC2FullAccess` (or custom policy allowing required actions)
* Python installed

---

## 📦 Installation

```bash
git clone https://github.com/your-username/boto3-ec2-experiment.git
cd boto3-ec2-experiment
pip install -r requirements.txt
```



## 🔐 Security Tip

**Never hardcode AWS credentials.** Use `~/.aws/credentials` or environment variables.

---

## 📖 Learning Outcome

This experiment helped me:

* Understand Boto3’s EC2 API
* Gain comfort with automation of AWS services
* Learn the lifecycle management of cloud resources

---

## 📚 References

* [Boto3 EC2 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html)
* [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)


