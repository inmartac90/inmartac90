#!/usr/bin/env python3

import yaml
from datetime import datetime

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

# Add skills by category
if 'skills' in profile and profile['skills']:
    for skill in profile['skills']:
        readme += f"\n**{skill['category']}:** {', '.join(skill['items'])}\n"

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

print("✅ README.md generated successfully!")
