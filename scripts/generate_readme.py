
#!/usr/bin/env python3
 
import yaml
from datetime import datetime
 
# Mapping de tecnologías a shields.io badges
TECH_BADGES = {
    'AWS (EC2, VPC, IAM, CloudWatch, RDS)': '![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat&logo=amazon-aws&logoColor=white)',
    'Linux': '![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)',
    'Windows Server': '![Windows](https://img.shields.io/badge/Windows%20Server-0078D4?style=flat&logo=windows&logoColor=white)',
    'Docker': '![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)',
    'Kubernetes': '![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)',
    'LogicMonitor': '![LogicMonitor](https://img.shields.io/badge/LogicMonitor-0099CC?style=flat)',
    'CloudWatch': '![CloudWatch](https://img.shields.io/badge/CloudWatch-FF9900?style=flat&logo=amazon-cloudwatch&logoColor=white)',
    'Dashboards': '![Dashboards](https://img.shields.io/badge/Dashboards-4285F4?style=flat)',
    'Alerting': '![Alerting](https://img.shields.io/badge/Alerting-FF6B6B?style=flat)',
    'Log Analysis': '![Logs](https://img.shields.io/badge/Log%20Analysis-FFA500?style=flat)',
    'Terraform': '![Terraform](https://img.shields.io/badge/Terraform-623CE4?style=flat&logo=terraform&logoColor=white)',
    'GitHub Actions': '![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=github-actions&logoColor=white)',
    'Bash': '![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat&logo=gnu-bash&logoColor=white)',
    'Python': '![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)',
    'AWS CLI': '![AWS CLI](https://img.shields.io/badge/AWS%20CLI-FF9900?style=flat&logo=amazon-aws&logoColor=white)',
    'Root-Cause Analysis': '![RCA](https://img.shields.io/badge/Root%20Cause%20Analysis-DC3545?style=flat)',
    'Incident Response': '![IR](https://img.shields.io/badge/Incident%20Response-FF6B6B?style=flat)',
    'SNMP': '![SNMP](https://img.shields.io/badge/SNMP-4B8BBE?style=flat)',
    'WMI/WinRM': '![WMI](https://img.shields.io/badge/WMI%2FWinRM-0078D4?style=flat)',
    'ServiceNow': '![ServiceNow](https://img.shields.io/badge/ServiceNow-00B050?style=flat)',
    'Jira': '![Jira](https://img.shields.io/badge/Jira-0052CC?style=flat&logo=jira&logoColor=white)',
}
 
# Load profile data
with open('profile.yaml', 'r', encoding='utf-8') as f:
    profile = yaml.safe_load(f)
 
# Build README
readme = f"""# Hi, I'm {profile['name']} 👋
 
**{profile['title']}** | {profile['location']}
 
{profile['bio']}
 
---
 
## 🛠️ Tech Stack
"""
 
# Add skills by category with badges
if 'skills' in profile and profile['skills']:
    for skill in profile['skills']:
        readme += f"\n### {skill['category']}\n"
        badges = []
        for item in skill['items']:
            badge = TECH_BADGES.get(item, f"![{item}](https://img.shields.io/badge/{item.replace(' ', '%20')}-gray?style=flat)")
            badges.append(badge)
        readme += " ".join(badges) + "\n"
 
# Add focus areas if they exist
if 'focus' in profile and profile['focus']:
    readme += "\n---\n## 🎯 What I'm Focused On\n"
    for focus in profile['focus']:
        readme += f"- {focus}\n"
 
# Add certifications if they exist
if 'certifications' in profile and profile['certifications']:
    readme += "\n---\n## 🎓 AWS Certification Roadmap\n"
    for cert in profile['certifications']:
        progress = cert.get('progress', 0)
        filled = '█' * progress
        empty = '░' * (10 - progress)
        status = '✅' if cert.get('completed', False) else '⏳'
        readme += f"- {status} **{cert['name']}**\n"
        readme += f"  Progress: `{filled}{empty}` {progress}%\n"
 
# Add projects if they exist
if 'projects' in profile and profile['projects']:
    readme += "\n---\n## 📦 Featured Projects\n"
 
    # Cloud projects
    if 'cloud' in profile['projects'] and profile['projects']['cloud']:
        readme += "\n### ☁️ Cloud & Infrastructure\n"
        for project in profile['projects']['cloud']:
            readme += f"- **[{project['name']}]({project['url']})** — {project['desc']}\n"
 
    # CI/CD projects
    if 'cicd' in profile['projects'] and profile['projects']['cicd']:
        readme += "\n### ⚙️ CI/CD & Automation\n"
        for project in profile['projects']['cicd']:
            readme += f"- **[{project['name']}]({project['url']})** — {project['desc']}\n"
 
    # Other projects
    if 'other' in profile['projects'] and profile['projects']['other']:
        readme += "\n### 💼 Other Projects\n"
        for project in profile['projects']['other']:
            readme += f"- **[{project['name']}]({project['url']})** — {project['desc']}\n"
 
# Add social links and footer
readme += f"""
---
 
## 🌐 Find Me Online
 
- 🌍 [Portfolio]({profile['socials']['portfolio']})
- 💼 [LinkedIn]({profile['socials']['linkedin']})
- 🔗 [Linktree]({profile['socials']['linktree']})
 
---
 
## 🎮 Beyond the Terminal
 
When I'm away from cloud dashboards, I enjoy {profile.get('interests', 'coding')}
 
**{profile.get('philosophy', 'Learning, building, testing, repeating.')}**
 
*Last updated: {datetime.now().strftime('%B %d, %Y')}*
"""
 
# Write README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
 
print("✅ README.md generated successfully with badges!")