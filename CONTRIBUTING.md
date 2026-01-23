# 🤝 Contributing to Vulnerability Scanner Dashboard

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 📋 Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
3. [Development Setup](#development-setup)
4. [Pull Request Process](#pull-request-process)
5. [Coding Standards](#coding-standards)

## 📜 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards others

## 🎯 How Can I Contribute?

### Reporting Bugs

Before submitting a bug report:
- Check existing issues to avoid duplicates
- Gather information (OS, Python version, error messages)

Submit bug reports with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Your environment details

### Suggesting Features

Feature suggestions are welcome! Include:
- Clear description of the feature
- Why it would be useful
- Potential implementation approach

### Code Contributions

Areas where you can contribute:

**Security Scanners:**
- [ ] Integration with Metasploit
- [ ] OpenVAS integration
- [ ] Burp Suite integration
- [ ] Custom vulnerability checks

**Features:**
- [ ] User authentication system
- [ ] Scheduled scanning
- [ ] Email notifications
- [ ] API endpoints
- [ ] Multi-threading
- [ ] Scan profiles/templates

**UI/UX:**
- [ ] Dark mode
- [ ] Customizable themes
- [ ] Mobile app companion
- [ ] Better charts and visualizations

**Documentation:**
- [ ] Video tutorials
- [ ] API documentation
- [ ] More code examples
- [ ] Translations

## 💻 Development Setup

### 1. Fork the Repository

Click the "Fork" button on GitHub

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/vuln-scanner-dashboard.git
cd vuln-scanner-dashboard
```

### 3. Add Upstream Remote

```bash
git remote add upstream https://github.com/nainaisrat/vuln-scanner-dashboard.git
```

### 4. Create Branch

```bash
git checkout -b feature/your-feature-name
```

### 5. Install Development Dependencies

```bash
pip install -r requirements.txt
pip install pytest black flake8  # For testing and linting
```

### 6. Make Changes

- Write clean, documented code
- Follow existing code style
- Add comments where necessary
- Update documentation

### 7. Test Your Changes

```bash
# Run the application
python app.py

# Test manually in browser
# Check for errors in console
```

### 8. Commit Changes

```bash
git add .
git commit -m "feat: Add awesome new feature"
```

Commit message format:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance tasks

### 9. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 10. Submit Pull Request

- Go to your fork on GitHub
- Click "New Pull Request"
- Fill in the template
- Submit!

## 🔄 Pull Request Process

### Before Submitting

- [ ] Test your changes thoroughly
- [ ] Update documentation if needed
- [ ] Follow coding standards
- [ ] Write meaningful commit messages

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Other (specify)

## Testing
How did you test this?

## Screenshots
If applicable

## Checklist
- [ ] Code follows project style
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings
```

### Review Process

1. Maintainer reviews code
2. Feedback provided if needed
3. You make requested changes
4. Approval and merge

## 📝 Coding Standards

### Python Style

```python
# Follow PEP 8
# Use meaningful variable names
# Add docstrings to functions

def scan_target(target, scan_type):
    """
    Scans a target for vulnerabilities
    
    Args:
        target (str): Target domain or IP
        scan_type (str): Type of scan to perform
        
    Returns:
        list: List of vulnerabilities found
    """
    pass
```

### HTML/CSS/JavaScript

```html
<!-- Use Bootstrap classes when possible -->
<!-- Add comments for complex sections -->
<!-- Keep JavaScript organized -->
```

```javascript
// Use const/let instead of var
// Add comments for complex logic
// Follow existing naming conventions

const loadScanResults = async (scanId) => {
    // Implementation
};
```

### Database

- Use SQLAlchemy ORM
- Add migrations for schema changes
- Don't commit database files

## 🐛 Debugging

### Enable Debug Mode

```python
# In app.py
app.run(debug=True)
```

### Check Logs

```bash
# Flask logs will show in console
# Browser console for JavaScript errors
```

### Common Issues

1. **Database errors**: Delete `instance/vulnerabilities.db` and restart
2. **Import errors**: Reinstall dependencies
3. **Port conflicts**: Change port in `app.py`

## 📞 Getting Help

- Open an issue on GitHub
- Email: isratnaina1995@gmail.com
- Check existing issues and PRs

## 🏆 Recognition

Contributors will be:
- Listed in README
- Mentioned in release notes
- Credited in documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Vulnerability Scanner Dashboard!**

Together we can make cybersecurity tools more accessible and user-friendly.
