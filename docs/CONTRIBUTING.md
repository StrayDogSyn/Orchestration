# Contributing to The AI Orchestrator

<div align="center">

<img src="assets/branding/straydog-syndications-llc-main.png" alt="StrayDog Syndications LLC" width="350">

</div>

Thank you for your interest in contributing to The AI Orchestrator! This project exists to create second-chance career opportunities in tech, and your contributions help make that mission possible.

### ©️ Copyright Notice

This curriculum is © 2025 Eric "Hunter" Petross | StrayDog Syndications LLC | Second Story Initiative. This is proprietary educational content. By contributing, you agree that your contributions become part of the proprietary work and will be subject to the same license terms. Please see [LICENSE](LICENSE) for details.

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/clipboard-list.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Table of Contents

- [Code of Conduct](#code-of-conduct)
- [The Eric-Claude Workflow](#the-eric-claude-workflow)
- [How to Contribute](#how-to-contribute)
- [Development Process](#development-process)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Documentation Standards](#documentation-standards)
- [Testing Requirements](#testing-requirements)
- [Style Guidelines](#style-guidelines)

---

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/scroll.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Code of Conduct

### Our Pledge

We are committed to making participation in this project a harassment-free experience for everyone, with special consideration for justice-impacted individuals and non-traditional learners.

### Our Standards

**Positive behaviors include:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behaviors include:**
- Discriminatory language or actions based on background, including justice involvement
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the project maintainers. All complaints will be reviewed and investigated promptly and fairly.

---

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/robot.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> The Eric-Claude Workflow

This project uses a unique collaborative development model between **Eric "Hunter" Petross** (human instructor, founder of [StrayDog Syndications LLC](http://www.straydog-syndications-llc.com/) and [Second Story Initiative](https://straydog-secondstory.org/)) and **Claude** (AI partner). Here's how it works:

### How Decisions Are Made

1. **Eric** provides vision, requirements, and domain expertise
2. **Claude** provides implementation, research synthesis, and systematic analysis
3. **Both** iterate on ideas through structured conversation
4. **Eric** makes final decisions on all curriculum and architectural choices

### Contributing Within This Model

When proposing changes:
- Understand that major curriculum decisions involve Eric-Claude collaboration
- Provide clear rationale for suggestions
- Be open to AI-assisted review and refinement
- Document your reasoning so it can be evaluated systematically

---

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/target.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> How to Contribute

### Types of Contributions

| Type | Description | Difficulty |
|------|-------------|------------|
| <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/bug.svg" width="16" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Bug Fixes | Fix typos, broken links, code errors | Easy |
| <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/file-text.svg" width="16" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Documentation | Improve clarity, add examples | Easy-Medium |
| <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/video.svg" width="16" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Content | Create videos, exercises, examples | Medium |
| <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/books.svg" width="16" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Curriculum | Propose module content, learning paths | Medium-Hard |
| <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/tool.svg" width="16" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Infrastructure | Build tools, automation, templates | Hard |

### Getting Started

1. **Fork the repository**
   ```bash
   # Fork via GitHub UI, then:
   git clone https://github.com/YOUR-USERNAME/Orchestration.git
   cd Orchestration
   git remote add upstream https://github.com/StrayDogSyn/Orchestration.git
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

3. **Make your changes**
   - Follow the style guidelines below
   - Add tests if applicable
   - Update documentation

4. **Submit a pull request**
   - Fill out the PR template completely
   - Link any related issues
   - Request review from maintainers

---

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/refresh.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Development Process

### Branch Naming

Use these prefixes:
- `feature/` - New features or content
- `fix/` - Bug fixes
- `docs/` - Documentation only
- `refactor/` - Code restructuring
- `test/` - Test additions or fixes

Examples:
- `feature/module-01-lab-exercises`
- `fix/broken-links-readme`
- `docs/improve-quickstart`

### Commit Messages

Follow conventional commits:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

Examples:
```
feat(module-01): add binary search tree exercise

docs(readme): update prerequisites section

fix(lab-02): correct Python syntax error in starter code
```

---

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/git-branch.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Pull Request Guidelines

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] All tests pass
- [ ] Commit messages follow conventions
- [ ] Branch is up to date with main

### PR Template

```markdown
## Description
[What does this PR do?]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## Related Issues
Fixes #[issue number]

## Checklist
- [ ] I have read the CONTRIBUTING.md
- [ ] My code follows the style guidelines
- [ ] I have updated documentation as needed
- [ ] My changes generate no new warnings

## Screenshots (if applicable)
[Add screenshots here]
```

### Review Process

1. **Automated checks** run on all PRs
2. **Maintainer review** within 48 hours
3. **Feedback addressed** by contributor
4. **Final approval** and merge

---

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/book.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Documentation Standards

### Markdown Guidelines

- Use ATX-style headers (`#`, `##`, `###`)
- One sentence per line for easier diffs
- Use fenced code blocks with language specifiers
- Include alt text for images

### File Structure

```markdown
# Title

Brief introduction paragraph.

## Table of Contents (for long docs)

- [Section 1](#section-1)
- [Section 2](#section-2)

## Section 1

Content...

## Section 2

Content...
```

### Code Examples

Always include:
- Language identifier in code blocks
- Comments explaining non-obvious parts
- Expected output where helpful

```python
# Example: Binary search implementation
def binary_search(arr: list, target: int) -> int:
    """
    Find target in sorted array using binary search.
    
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

# Expected: 3
print(binary_search([1, 2, 3, 4, 5], 4))
```

---

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/flask.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Testing Requirements

### For Code Contributions

- Include unit tests for new functions
- Ensure all existing tests pass
- Aim for >80% coverage on new code

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=.
```

### For Content Contributions

- Verify all code examples run correctly
- Check all links are valid
- Test on multiple Python versions if applicable

---

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/palette.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Style Guidelines

### Python

Follow PEP 8 with these tools:
- **Formatter**: Black
- **Linter**: Flake8
- **Type Checker**: MyPy

```bash
# Format code
black .

# Check style
flake8 .

# Check types
mypy .
```

### Markdown

- Use consistent heading levels
- Keep line length under 100 characters
- Use reference-style links for repeated URLs

### File Organization

```
modules/XX-name/
├── README.md           # Module overview
├── lectures/           # Lecture content
│   ├── 01-topic.md
│   └── 02-topic.md
├── labs/               # Hands-on exercises
│   ├── lab-01/
│   │   ├── README.md
│   │   ├── starter.py
│   │   └── solution.py
│   └── lab-02/
├── projects/           # Assessment projects
│   └── project-01/
│       ├── README.md
│       ├── rubric.md
│       └── starter/
└── resources/          # Supplementary materials
    └── README.md
```

---

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/hand-stop.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Getting Help

- **Questions**: Open a GitHub Discussion
- **Bugs**: Open a GitHub Issue
- **Ideas**: Open a GitHub Discussion with `[Idea]` prefix

### Response Times

- Issues: Within 48 hours
- PRs: Within 72 hours
- Discussions: Within 1 week

---

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/trophy.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Recognition

Contributors are recognized in:
- README.md acknowledgments
- Release notes
- Course credits (for significant contributions)

---

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/file-text.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> License

By contributing, you agree that your contributions become part of the proprietary work owned by Eric "Hunter" Petross and StrayDog Syndications LLC, subject to the terms in the [LICENSE](LICENSE) file.

---

Thank you for helping create opportunities for second-chance learners! <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/heart.svg" width="14" style="filter: invert(54%) sepia(64%) saturate(1073%) hue-rotate(222deg) brightness(93%) contrast(91%);" />
