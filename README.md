# 🚀 DevOps Lab - ALB Task 1 & 2

Welcome to my **DevOps Lab Repository!** 🎉 This repo contains my work on **Application Load Balancer (ALB) Tasks 1 & 2**, where I explore deploying scalable and resilient web applications using AWS services. Let's dive in! 🔥

---

## 🌍 Task 1: Deploying an Application with ALB
### **Objective** 🎯
Deploy a web application behind an **Application Load Balancer (ALB)** to distribute traffic efficiently.

### **Steps Taken** 🛠️
1. **Created an EC2 Instance** 🏗️
2. **Installed & Configured Web Server** (Flask-based `app.py` running on port 5000) 🌐
3. **Set Up an Application Load Balancer (ALB)**
   - Created **Target Groups** 🎯
   - Registered EC2 instances with the **ALB** 🔗
   - Configured **Security Groups** & Health Checks ✅
4. **Tested the Application** 📡
   - Verified ALB's DNS name loads the app **smoothly** 🚀

---

## 🏆 Task 2: Scaling with Auto Scaling Group (ASG)
### **Objective** 🎯
Enhance availability and scalability by integrating an **Auto Scaling Group (ASG)** with ALB.

### **Steps Taken** 🔄
1. **Created a Launch Template** 📜
   - Configured AMI, instance type, security groups, and startup scripts 🏗️
2. **Configured an Auto Scaling Group (ASG)** 📈
   - Defined scaling policies (CPU-based scaling) 📊
   - Attached ALB for seamless load balancing 🔄
3. **Simulated Traffic and Observed Scaling** 📡
   - Stress-tested the system with `ab` (Apache Benchmark) 💥
   - Verified **automatic instance provisioning and termination** 🔄

---

## 🛠️ Tech Stack Used
- **AWS EC2** 🏗️
- **Application Load Balancer (ALB)** ⚖️
- **Auto Scaling Group (ASG)** 📈
- **Flask (Python Web App)** 🐍
- **CloudWatch Metrics** 📊

---

## 📜 How to Run Locally?
```bash
# Clone the repository
$ git clone https://github.com/saadhaniftaj/DevOps_lab2_app.git
$ cd DevOps_lab2_app

# Run the Flask App (if testing locally)
$ python3 app.py
```

---

## 🚀 Live Testing
- If deployed on AWS, visit the **ALB DNS name** in your browser:
  ```
  http://your-alb-dns-name
  ```

---

## 🤝 Contributing
Want to improve the repo? Feel free to fork, star ⭐, and submit a PR! Let's learn DevOps together. 🚀

---

## 📢 Connect with Me!
🐦 **Twitter:** [@yourhandle](https://twitter.com/)  
💼 **LinkedIn:** [Your LinkedIn](https://linkedin.com/)  
📧 **Email:** your.email@example.com

Let's build something awesome together! 🚀🔥
