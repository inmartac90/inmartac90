#!/usr/bin/env python3
import yaml
from datetime import datetime

# Load profile data
with open('profile.yaml', 'r', encoding='utf-8') as f:
    profile = yaml.safe_load(f)

# Build README
readme = f"""# Hi, I'm {profile['name']} 👋

{profile['title']} | {profile['location']}

{profile['bio']}

---

## 🛠️ Tech Stack

"""

# Add badges
for skill in profile['skills']:
    readme += f"[![{skill['name']}]({skill['badge']})]({profile['socials'].get('portfolio', '#')})\n"

readme += "\n---\n\n## 🎯 What I'm Focused On\n\n"

# Add focus areas
for focus in profile['focus']:
    readme += f"- {focus}\n"

readme += "\n---\n\n## 🎓 AWS Certification Roadmap\n\n"

# Add certifications with progress
for cert in profile['certifications']:
    progress = cert['progress']
    filled = '█' * (progress // 10)
    empty = '░' * (10 - progress // 10)
    status = "✅" if cert['completed'] else "⏳"
    
    readme += f"- [{status}] **{cert['name']}**\n"
    readme += f"  Progress: `{filled}{empty}` {progress}%\n\n"

readme += "---\n\n## 📦 Featured Projects\n\n"

# Add cloud projects
readme += "### ☁️ Cloud & Infrastructure\n\n"
for project in profile['projects']['cloud']:
    readme += f"- **[{project['name']}]({project['url']})** — {project['desc']}\n"

readme += "\n### ⚙️ CI/CD & Automation\n\n"
for project in profile['projects']['cicd']:
    readme += f"- **[{project['name']}]({project['url']})** — {project['desc']}\n"

readme += "\n### 💼 Other Projects\n\n"
for project in profile['projects']['other']:
    readme += f"- **[{project['name']}]({project['url']})** — {project['desc']}\n"

readme += f"""

---

## 🌐 Find Me Online

- 🌍 [Portfolio]({profile['socials']['portfolio']})
- 💼 [LinkedIn]({profile['socials']['linkedin']})
- 🔗 [Linktree]({profile['socials']['linktree']})

---

## 🎮 Beyond the Terminal

When I'm away from cloud dashboards, I enjoy {profile['interests']}.

---

**Learning, building, testing, repeating.**

*Last updated: {datetime.now().strftime('%B %d, %Y')}*
"""

# Write README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("✅ README.md generated successfully!")
