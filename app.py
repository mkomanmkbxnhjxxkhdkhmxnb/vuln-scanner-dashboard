#!/usr/bin/env python3
"""
Automated Vulnerability Scanner Dashboard
A web-based security scanning tool that integrates multiple vulnerability assessment tools
Author: Ishrat Jahan Naina
GitHub: https://github.com/nainaisrat
"""

from flask import Flask, render_template, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import subprocess
import json
import os
import re
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vulnerabilities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
db = SQLAlchemy(app)

# Database Models
class Scan(db.Model):
    """Model for storing scan information"""
    id = db.Column(db.Integer, primary_key=True)
    target = db.Column(db.String(200), nullable=False)
    scan_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='pending')
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)
    results = db.relationship('Vulnerability', backref='scan', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'target': self.target,
            'scan_type': self.scan_type,
            'status': self.status,
            'started_at': self.started_at.strftime('%Y-%m-%d %H:%M:%S'),
            'completed_at': self.completed_at.strftime('%Y-%m-%d %H:%M:%S') if self.completed_at else None
        }

class Vulnerability(db.Model):
    """Model for storing discovered vulnerabilities"""
    id = db.Column(db.Integer, primary_key=True)
    scan_id = db.Column(db.Integer, db.ForeignKey('scan.id'), nullable=False)
    severity = db.Column(db.String(20))  # critical, high, medium, low, info
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    recommendation = db.Column(db.Text)
    discovered_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'severity': self.severity,
            'title': self.title,
            'description': self.description,
            'recommendation': self.recommendation,
            'discovered_at': self.discovered_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# Create database tables
with app.app_context():
    db.create_all()

# Security Scanner Functions
def run_nmap_scan(target):
    """
    Runs Nmap port scan and service detection
    Returns: List of vulnerabilities found
    """
    vulnerabilities = []
    
    try:
        # Basic Nmap scan (safe, non-intrusive)
        # In production, use actual nmap. For demo, we simulate results
        cmd = f"nmap -sV -T4 --top-ports 100 {target}"
        
        # DEMO MODE: Simulated results for GitHub demonstration
        # Replace this with actual subprocess.run() when deploying
        demo_results = simulate_nmap_scan(target)
        
        for result in demo_results:
            vulnerabilities.append(result)
            
    except Exception as e:
        vulnerabilities.append({
            'severity': 'info',
            'title': 'Scan Error',
            'description': f'Error during Nmap scan: {str(e)}',
            'recommendation': 'Check network connectivity and target availability'
        })
    
    return vulnerabilities

def simulate_nmap_scan(target):
    """Simulates Nmap scan results for demonstration purposes"""
    results = []
    
    # Common open ports simulation
    open_ports = [
        {'port': 22, 'service': 'SSH', 'version': 'OpenSSH 7.4'},
        {'port': 80, 'service': 'HTTP', 'version': 'Apache 2.4.6'},
        {'port': 443, 'service': 'HTTPS', 'version': 'Apache 2.4.6'},
        {'port': 3306, 'service': 'MySQL', 'version': '5.7.33'}
    ]
    
    for port_info in open_ports:
        # Check for outdated versions
        if 'Apache 2.4.6' in port_info['version']:
            results.append({
                'severity': 'medium',
                'title': f'Outdated {port_info["service"]} Version Detected',
                'description': f'Port {port_info["port"]}: {port_info["service"]} version {port_info["version"]} is outdated and may contain known vulnerabilities.',
                'recommendation': 'Update to the latest stable version of Apache web server'
            })
        
        # Check for database exposure
        if port_info['port'] == 3306:
            results.append({
                'severity': 'high',
                'title': 'MySQL Database Publicly Accessible',
                'description': f'MySQL database (port {port_info["port"]}) is accessible from external networks.',
                'recommendation': 'Restrict MySQL access to localhost or trusted IP addresses only. Use firewall rules to block external access.'
            })
    
    # Add SSL/TLS check
    results.append({
        'severity': 'info',
        'title': 'SSL/TLS Certificate Detected',
        'description': 'HTTPS service is using SSL/TLS encryption.',
        'recommendation': 'Ensure certificate is valid and not expired. Consider using strong cipher suites.'
    })
    
    return results

def run_nikto_scan(target):
    """
    Runs Nikto web server scanner
    Returns: List of web vulnerabilities found
    """
    vulnerabilities = []
    
    try:
        # DEMO MODE: Simulated Nikto results
        demo_results = simulate_nikto_scan(target)
        
        for result in demo_results:
            vulnerabilities.append(result)
            
    except Exception as e:
        vulnerabilities.append({
            'severity': 'info',
            'title': 'Scan Error',
            'description': f'Error during Nikto scan: {str(e)}',
            'recommendation': 'Verify web server is running and accessible'
        })
    
    return vulnerabilities

def simulate_nikto_scan(target):
    """Simulates Nikto web vulnerability scan results"""
    results = []
    
    # Common web vulnerabilities
    web_vulns = [
        {
            'severity': 'medium',
            'title': 'Missing Security Headers',
            'description': 'The web server is missing important security headers: X-Frame-Options, X-Content-Type-Options, Content-Security-Policy',
            'recommendation': 'Configure web server to send security headers. Add X-Frame-Options: DENY, X-Content-Type-Options: nosniff, and implement a Content Security Policy.'
        },
        {
            'severity': 'low',
            'title': 'Server Version Disclosure',
            'description': 'Web server is disclosing version information in HTTP headers, which could help attackers identify known vulnerabilities.',
            'recommendation': 'Configure server to hide version information in headers. For Apache, use "ServerTokens Prod" directive.'
        },
        {
            'severity': 'medium',
            'title': 'Directory Listing Enabled',
            'description': 'Directory listing is enabled on some directories, exposing file structure.',
            'recommendation': 'Disable directory listing in web server configuration. For Apache, use "Options -Indexes".'
        },
        {
            'severity': 'info',
            'title': 'robots.txt Found',
            'description': 'robots.txt file exists and may reveal sensitive directories.',
            'recommendation': 'Review robots.txt to ensure no sensitive paths are disclosed. Consider using authentication instead of relying on robots.txt.'
        }
    ]
    
    return web_vulns

def run_ssl_check(target):
    """
    Checks SSL/TLS configuration
    Returns: List of SSL-related vulnerabilities
    """
    vulnerabilities = []
    
    try:
        # DEMO MODE: Simulated SSL checks
        demo_results = simulate_ssl_check(target)
        
        for result in demo_results:
            vulnerabilities.append(result)
            
    except Exception as e:
        vulnerabilities.append({
            'severity': 'info',
            'title': 'SSL Check Error',
            'description': f'Error during SSL check: {str(e)}',
            'recommendation': 'Verify HTTPS is configured on target'
        })
    
    return vulnerabilities

def simulate_ssl_check(target):
    """Simulates SSL/TLS security checks"""
    results = []
    
    ssl_issues = [
        {
            'severity': 'low',
            'title': 'Weak SSL Cipher Suites Supported',
            'description': 'Server supports weak cipher suites that use RC4 or 3DES encryption.',
            'recommendation': 'Disable weak cipher suites. Configure server to use only strong ciphers (AES-GCM, ChaCha20-Poly1305).'
        },
        {
            'severity': 'medium',
            'title': 'TLS 1.0 and 1.1 Enabled',
            'description': 'Server supports deprecated TLS versions 1.0 and 1.1.',
            'recommendation': 'Disable TLS 1.0 and 1.1. Configure server to support only TLS 1.2 and TLS 1.3.'
        },
        {
            'severity': 'info',
            'title': 'Certificate Valid',
            'description': 'SSL certificate is valid and properly configured.',
            'recommendation': 'Monitor certificate expiration date and renew before expiry.'
        }
    ]
    
    return ssl_issues

# Routes
@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/api/scan', methods=['POST'])
def start_scan():
    """API endpoint to start a new vulnerability scan"""
    data = request.get_json()
    target = data.get('target', '').strip()
    scan_type = data.get('scan_type', 'quick')
    
    # Basic validation
    if not target:
        return jsonify({'error': 'Target is required'}), 400
    
    # Validate target format (basic check)
    if not re.match(r'^[a-zA-Z0-9.-]+$', target):
        return jsonify({'error': 'Invalid target format'}), 400
    
    # Create new scan record
    scan = Scan(target=target, scan_type=scan_type, status='running')
    db.session.add(scan)
    db.session.commit()
    
    # Run scans based on scan type
    try:
        all_vulnerabilities = []
        
        if scan_type in ['quick', 'full']:
            # Run Nmap scan
            nmap_vulns = run_nmap_scan(target)
            all_vulnerabilities.extend(nmap_vulns)
        
        if scan_type in ['web', 'full']:
            # Run Nikto scan
            nikto_vulns = run_nikto_scan(target)
            all_vulnerabilities.extend(nikto_vulns)
            
            # Run SSL check
            ssl_vulns = run_ssl_check(target)
            all_vulnerabilities.extend(ssl_vulns)
        
        # Save vulnerabilities to database
        for vuln_data in all_vulnerabilities:
            vulnerability = Vulnerability(
                scan_id=scan.id,
                severity=vuln_data.get('severity', 'info'),
                title=vuln_data.get('title', 'Unknown'),
                description=vuln_data.get('description', ''),
                recommendation=vuln_data.get('recommendation', '')
            )
            db.session.add(vulnerability)
        
        # Update scan status
        scan.status = 'completed'
        scan.completed_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'success': True,
            'scan_id': scan.id,
            'vulnerabilities_found': len(all_vulnerabilities)
        })
        
    except Exception as e:
        scan.status = 'failed'
        db.session.commit()
        return jsonify({'error': str(e)}), 500

@app.route('/api/scans')
def get_scans():
    """API endpoint to get all scans"""
    scans = Scan.query.order_by(Scan.started_at.desc()).all()
    return jsonify([scan.to_dict() for scan in scans])

@app.route('/api/scan/<int:scan_id>')
def get_scan(scan_id):
    """API endpoint to get specific scan details"""
    scan = Scan.query.get_or_404(scan_id)
    vulnerabilities = [vuln.to_dict() for vuln in scan.results]
    
    return jsonify({
        'scan': scan.to_dict(),
        'vulnerabilities': vulnerabilities
    })

@app.route('/api/scan/<int:scan_id>/delete', methods=['DELETE'])
def delete_scan(scan_id):
    """API endpoint to delete a scan"""
    scan = Scan.query.get_or_404(scan_id)
    db.session.delete(scan)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/api/statistics')
def get_statistics():
    """API endpoint to get dashboard statistics"""
    total_scans = Scan.query.count()
    total_vulns = Vulnerability.query.count()
    
    # Count by severity
    critical = Vulnerability.query.filter_by(severity='critical').count()
    high = Vulnerability.query.filter_by(severity='high').count()
    medium = Vulnerability.query.filter_by(severity='medium').count()
    low = Vulnerability.query.filter_by(severity='low').count()
    info = Vulnerability.query.filter_by(severity='info').count()
    
    return jsonify({
        'total_scans': total_scans,
        'total_vulnerabilities': total_vulns,
        'severity_distribution': {
            'critical': critical,
            'high': high,
            'medium': medium,
            'low': low,
            'info': info
        }
    })

@app.route('/api/scan/<int:scan_id>/export')
def export_pdf(scan_id):
    """Export scan results as PDF"""
    scan = Scan.query.get_or_404(scan_id)
    vulnerabilities = scan.results
    
    # Create PDF in memory
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Title
    title = Paragraph(f"Vulnerability Scan Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    # Scan Information
    info_data = [
        ['Target:', scan.target],
        ['Scan Type:', scan.scan_type],
        ['Started:', scan.started_at.strftime('%Y-%m-%d %H:%M:%S')],
        ['Completed:', scan.completed_at.strftime('%Y-%m-%d %H:%M:%S') if scan.completed_at else 'N/A'],
        ['Total Vulnerabilities:', str(len(vulnerabilities))]
    ]
    
    info_table = Table(info_data, colWidths=[150, 300])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.grey),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(info_table)
    elements.append(Spacer(1, 20))
    
    # Vulnerabilities
    vuln_title = Paragraph("Discovered Vulnerabilities", styles['Heading2'])
    elements.append(vuln_title)
    elements.append(Spacer(1, 12))
    
    for i, vuln in enumerate(vulnerabilities, 1):
        vuln_data = [
            [f"#{i} - {vuln.title}"],
            [f"Severity: {vuln.severity.upper()}"],
            [f"Description: {vuln.description}"],
            [f"Recommendation: {vuln.recommendation}"]
        ]
        
        vuln_table = Table(vuln_data, colWidths=[450])
        vuln_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'TOP')
        ]))
        
        elements.append(vuln_table)
        elements.append(Spacer(1, 12))
    
    # Build PDF
    doc.build(elements)
    buffer.seek(0)
    
    return send_file(
        buffer,
        as_attachment=True,
        download_name=f'scan_report_{scan_id}.pdf',
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
