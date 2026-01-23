# 🛡️ Automated Vulnerability Scanner Dashboard

A modern, web-based vulnerability scanning platform that integrates multiple security assessment tools into a beautiful, easy-to-use dashboard. Built for cybersecurity professionals, penetration testers, and security enthusiasts.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)

## 📸 Screenshots

### Dashboard Overview
Beautiful, modern interface with real-time statistics and vulnerability tracking.

### Scan Results
Detailed vulnerability reports with severity classification and remediation guidance.

## ✨ Features

### 🔍 Multi-Tool Integration
- **Port Scanning**: Integrated Nmap for comprehensive port and service detection
- **Web Vulnerability Scanning**: Nikto integration for web server security assessment
- **SSL/TLS Analysis**: Automated SSL certificate and configuration checking
- **Modular Design**: Easy to add more security tools

### 📊 Beautiful Visualizations
- **Real-time Dashboard**: Live statistics and vulnerability counts
- **Interactive Charts**: Severity distribution using Chart.js
- **Color-coded Results**: Easy-to-understand severity indicators
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile

### 📈 Comprehensive Reporting
- **PDF Export**: Professional PDF reports for each scan
- **Detailed Findings**: Complete vulnerability descriptions and remediation steps
- **Historical Tracking**: Keep track of all your scans over time
- **Severity Classification**: Critical, High, Medium, Low, and Info categories

### 🎯 User-Friendly Interface
- **Bootstrap 5**: Modern, responsive UI components
- **Font Awesome Icons**: Beautiful, professional iconography
- **Gradient Backgrounds**: Eye-catching design elements
- **Intuitive Navigation**: Easy to use, even for beginners

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/nainaisrat/vuln-scanner-dashboard.git
cd vuln-scanner-dashboard
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Access the dashboard**
Open your browser and navigate to:
```
http://localhost:5000
```

## 💻 Usage

### Starting a New Scan

1. Enter the target domain or IP address
2. Select scan type:
   - **Quick Scan**: Port and service detection
   - **Web Scan**: Web application vulnerabilities
   - **Full Scan**: Comprehensive assessment
3. Click "Start Scanning"
4. View results in real-time

### Viewing Results

- Click on any scan in the history table to view detailed vulnerabilities
- Each vulnerability includes:
  - Severity level (Critical/High/Medium/Low/Info)
  - Detailed description
  - Remediation recommendations
  - Discovery timestamp

### Exporting Reports

- Click the PDF icon next to any scan in the history
- Professional PDF report will be generated and downloaded
- Share reports with team members or clients

## 📋 Project Structure

```
vuln-scanner-dashboard/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # MIT License
├── .gitignore            # Git ignore rules
│
├── templates/
│   └── index.html        # Main dashboard template
│
├── static/               # (Auto-created)
│   ├── css/
│   ├── js/
│   └── images/
│
└── instance/             # (Auto-created)
    └── vulnerabilities.db  # SQLite database
```

## 🔧 Configuration

### Database

The application uses SQLite by default. To use a different database:

```python
# In app.py, modify the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:pass@localhost/dbname'
# or
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/dbname'
```

### Security

**Important**: Change the secret key in production:

```python
# In app.py
app.config['SECRET_KEY'] = 'your-unique-secret-key-here'
```

### Adding Custom Scanners

To integrate additional security tools:

1. Create a new scanner function in `app.py`:
```python
def run_custom_scanner(target):
    vulnerabilities = []
    # Your scanning logic here
    return vulnerabilities
```

2. Call it in the scan endpoint:
```python
custom_vulns = run_custom_scanner(target)
all_vulnerabilities.extend(custom_vulns)
```

## 🎓 Educational Purpose

This project was developed as part of:
- **VAPT & Ethical Hacking Course**
- **Cybersecurity Research**
- **Portfolio Development**

### Learning Outcomes

- Understanding of web application security
- Integration of multiple security tools
- Full-stack development (Python + Flask + JavaScript)
- Database design and management
- Report generation and data visualization
- RESTful API development

## ⚠️ Legal Disclaimer

**IMPORTANT**: Only use this tool on systems you own or have explicit permission to test.

- Unauthorized scanning is illegal and unethical
- Always obtain written permission before scanning
- Follow responsible disclosure practices
- Respect privacy and security of others

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- [ ] Add more security scanners (Metasploit, OpenVAS, etc.)
- [ ] Implement user authentication
- [ ] Add scheduled scanning
- [ ] Create API endpoints for automation
- [ ] Improve PDF report design
- [ ] Add email notifications
- [ ] Implement multi-threading for faster scans
- [ ] Add Docker support

## 📝 To-Do List

- [x] Basic port scanning
- [x] Web vulnerability scanning
- [x] SSL/TLS analysis
- [x] PDF report generation
- [x] Beautiful dashboard UI
- [x] Scan history tracking
- [ ] User authentication
- [ ] Scheduled scans
- [ ] Email notifications
- [ ] API documentation
- [ ] Docker containerization
- [ ] CI/CD pipeline

## 🛠️ Technologies Used

### Backend
- **Flask 3.0**: Web framework
- **SQLAlchemy**: Database ORM
- **ReportLab**: PDF generation
- **Python 3.8+**: Programming language

### Frontend
- **Bootstrap 5**: UI framework
- **Chart.js**: Data visualization
- **Font Awesome**: Icons
- **Vanilla JavaScript**: Interactivity

### Security Tools (Simulated in Demo)
- **Nmap**: Port scanning
- **Nikto**: Web vulnerability scanning
- **OpenSSL**: SSL/TLS testing

## 📊 Database Schema

### Scans Table
```sql
- id (Primary Key)
- target (String)
- scan_type (String)
- status (String)
- started_at (DateTime)
- completed_at (DateTime)
```

### Vulnerabilities Table
```sql
- id (Primary Key)
- scan_id (Foreign Key)
- severity (String)
- title (String)
- description (Text)
- recommendation (Text)
- discovered_at (DateTime)
```

## 🔐 Security Considerations

- Input validation for target addresses
- SQL injection prevention through ORM
- XSS protection in template rendering
- CSRF protection for forms
- Secure session management
- Rate limiting (recommended for production)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Ishrat Jahan Naina**
- 🎓 B.Sc. Computer Science & Engineering, IIUC (2021)
- 💼 ICT Educator | Cybersecurity Enthusiast
- 📧 Email: isratnaina1995@gmail.com
- 🔗 LinkedIn: [linkedin.com/in/ishrat-jahan-275a70194](https://linkedin.com/in/ishrat-jahan-275a70194)
- 💻 GitHub: [@nainaisrat](https://github.com/nainaisrat)

### Portfolio Projects
- 🛡️ **Vulnerability Scanner Dashboard** (This project)
- 🤖 **APT Detection System** (90% accuracy, ML-based)
- 📧 **PhishGuard BD** (IIUC Tech Fair 2023 Winner)

## 🙏 Acknowledgments

- **IIUC CSE Department** for foundational computer science education
- **VAPT & Ethical Hacking Course** for practical security skills
- **Open Source Community** for amazing tools and libraries
- **Bootstrap Team** for the excellent UI framework
- **Chart.js** for beautiful data visualizations

## 📞 Support

If you have any questions or need help:

1. Check the [Issues](https://github.com/nainaisrat/vuln-scanner-dashboard/issues) page
2. Open a new issue if yours isn't already listed
3. Contact me via email or LinkedIn

## ⭐ Star This Repository

If you find this project helpful, please consider giving it a star! It helps others discover the project and motivates further development.

---

**Made with ❤️ for the Cybersecurity Community**

*Remember: Use your powers for good, always get permission, and stay ethical!*
