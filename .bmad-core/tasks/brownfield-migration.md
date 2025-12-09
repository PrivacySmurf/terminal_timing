# Brownfield Project Migration Task

**Purpose:** Analyze an existing codebase and onboard it into the BMAD workflow by detecting project structure, tech stack, existing documentation, and creating appropriate BMAD artifacts.

**When to Use:** When dropping the BMAD template into an existing project that was NOT created with BMAD.

**Instructions for Orchestrator:** Execute each phase sequentially. Present findings to user at checkpoints. Do NOT skip phases.

---

## Phase 1: Environment & VCS Analysis

### 1.1 Git Repository Status

```bash
echo "=== GIT ANALYSIS ==="
git rev-parse --is-inside-work-tree 2>/dev/null && echo "✓ Git initialized" || echo "✗ Not a git repo"
git remote -v 2>/dev/null || echo "No remotes configured"
git branch -a 2>/dev/null | head -20
echo -e "\nCurrent branch: $(git branch --show-current 2>/dev/null || echo 'N/A')"
echo -e "\nRecent commits:"
git --no-pager log --oneline -10 2>/dev/null || echo "No commits"
echo -e "\nUncommitted changes:"
git status --porcelain 2>/dev/null | head -20
```

### 1.2 Project Root Structure

```bash
echo "=== PROJECT STRUCTURE ==="
ls -la
echo -e "\n=== DIRECTORY TREE (2 levels) ==="
find . -maxdepth 2 -type d ! -path '*/\.*' ! -path './node_modules/*' ! -path './.git/*' ! -path './venv/*' ! -path './__pycache__/*' 2>/dev/null | head -50
```

**Checkpoint 1:** Present VCS status and root structure to user. Ask:
```
I've analyzed the repository structure. Before continuing:
1. Is this the correct project root?
2. Are there any directories I should ignore during analysis?
3. Continue with tech stack detection
```

---

## Phase 2: Tech Stack Detection

### 2.1 Language & Framework Detection

```bash
echo "=== LANGUAGE/FRAMEWORK DETECTION ==="

# Python
[ -f "requirements.txt" ] && echo "✓ Python (requirements.txt)" && head -20 requirements.txt
[ -f "pyproject.toml" ] && echo "✓ Python (pyproject.toml)" && head -30 pyproject.toml
[ -f "setup.py" ] && echo "✓ Python (setup.py)"
[ -f "Pipfile" ] && echo "✓ Python (Pipfile)"
[ -d "venv" ] || [ -d ".venv" ] && echo "✓ Python virtualenv detected"

# JavaScript/TypeScript
[ -f "package.json" ] && echo "✓ Node.js (package.json)" && cat package.json | head -50
[ -f "tsconfig.json" ] && echo "✓ TypeScript"
[ -f "bun.lockb" ] && echo "✓ Bun runtime"
[ -d "node_modules" ] && echo "✓ node_modules present"

# Go
[ -f "go.mod" ] && echo "✓ Go (go.mod)" && cat go.mod
[ -f "go.sum" ] && echo "✓ Go dependencies locked"

# Rust
[ -f "Cargo.toml" ] && echo "✓ Rust (Cargo.toml)" && head -30 Cargo.toml

# Ruby
[ -f "Gemfile" ] && echo "✓ Ruby (Gemfile)" && head -20 Gemfile

# Java/Kotlin
[ -f "pom.xml" ] && echo "✓ Java/Maven"
[ -f "build.gradle" ] || [ -f "build.gradle.kts" ] && echo "✓ Gradle"

# .NET
[ -f "*.csproj" ] 2>/dev/null && echo "✓ .NET"
[ -f "*.sln" ] 2>/dev/null && echo "✓ .NET Solution"

# PHP
[ -f "composer.json" ] && echo "✓ PHP (Composer)"

echo -e "\n=== CONFIG FILES ==="
ls -la *.json *.yaml *.yml *.toml *.ini .env* 2>/dev/null | head -20
```

### 2.2 Framework-Specific Detection

```bash
echo "=== FRAMEWORK DETECTION ==="

# Web Frameworks
[ -d "src/app" ] || [ -d "app" ] && echo "? Possible Next.js/Rails/Laravel app structure"
[ -f "next.config.js" ] || [ -f "next.config.mjs" ] && echo "✓ Next.js"
[ -f "nuxt.config.js" ] || [ -f "nuxt.config.ts" ] && echo "✓ Nuxt.js"
[ -f "vite.config.js" ] || [ -f "vite.config.ts" ] && echo "✓ Vite"
[ -f "webpack.config.js" ] && echo "✓ Webpack"
[ -f "angular.json" ] && echo "✓ Angular"
[ -f "svelte.config.js" ] && echo "✓ SvelteKit"

# Python Frameworks
grep -l "fastapi\|FastAPI" *.py 2>/dev/null && echo "✓ FastAPI"
grep -l "flask\|Flask" *.py 2>/dev/null && echo "✓ Flask"
grep -l "django\|Django" *.py 2>/dev/null && echo "✓ Django"
[ -f "manage.py" ] && echo "✓ Django (manage.py)"

# API/Backend
[ -f "openapi.yaml" ] || [ -f "openapi.json" ] || [ -f "swagger.yaml" ] && echo "✓ OpenAPI spec found"
[ -d "prisma" ] && echo "✓ Prisma ORM"
[ -f "schema.prisma" ] && echo "✓ Prisma schema"

# Infrastructure
[ -f "Dockerfile" ] && echo "✓ Docker"
[ -f "docker-compose.yml" ] || [ -f "docker-compose.yaml" ] && echo "✓ Docker Compose"
[ -f "Makefile" ] && echo "✓ Makefile"
[ -d ".github/workflows" ] && echo "✓ GitHub Actions" && ls .github/workflows/
[ -f ".gitlab-ci.yml" ] && echo "✓ GitLab CI"
[ -f "Jenkinsfile" ] && echo "✓ Jenkins"
[ -d "terraform" ] || [ -f "*.tf" ] 2>/dev/null && echo "✓ Terraform"
[ -f "serverless.yml" ] && echo "✓ Serverless Framework"
```

### 2.3 Testing Setup

```bash
echo "=== TESTING SETUP ==="
[ -f "jest.config.js" ] || [ -f "jest.config.ts" ] && echo "✓ Jest"
[ -f "vitest.config.js" ] || [ -f "vitest.config.ts" ] && echo "✓ Vitest"
[ -f "pytest.ini" ] || [ -f "pyproject.toml" ] && grep -q "pytest" pyproject.toml 2>/dev/null && echo "✓ Pytest"
[ -d "tests" ] || [ -d "test" ] || [ -d "__tests__" ] && echo "✓ Test directory found"
[ -f "cypress.config.js" ] || [ -d "cypress" ] && echo "✓ Cypress"
[ -f "playwright.config.ts" ] && echo "✓ Playwright"

echo -e "\n=== TEST FILES ==="
find . -name "*test*" -o -name "*spec*" 2>/dev/null | grep -v node_modules | grep -v __pycache__ | head -20
```

**Checkpoint 2:** Present detected tech stack. Ask user to confirm/correct:
```
Based on my analysis, here's the detected tech stack:

Languages: [list]
Frameworks: [list]
Build Tools: [list]
Testing: [list]
Infrastructure: [list]

1. Confirm this is accurate
2. Add missing technologies
3. Correct any misdetections
```

---

## Phase 3: Existing Documentation Analysis

### 3.1 Documentation Discovery

```bash
echo "=== DOCUMENTATION DISCOVERY ==="

# Standard docs
[ -f "README.md" ] && echo "✓ README.md" && wc -l README.md
[ -f "CONTRIBUTING.md" ] && echo "✓ CONTRIBUTING.md"
[ -f "CHANGELOG.md" ] && echo "✓ CHANGELOG.md"
[ -f "LICENSE" ] || [ -f "LICENSE.md" ] && echo "✓ LICENSE"
[ -f "ARCHITECTURE.md" ] && echo "✓ ARCHITECTURE.md (existing)"
[ -f "DESIGN.md" ] && echo "✓ DESIGN.md"
[ -f "API.md" ] && echo "✓ API.md"

# Docs directories
[ -d "docs" ] && echo "✓ docs/ directory" && ls -la docs/ | head -20
[ -d "documentation" ] && echo "✓ documentation/ directory"
[ -d "wiki" ] && echo "✓ wiki/ directory"
[ -d ".github" ] && echo "✓ .github/ directory" && ls .github/

echo -e "\n=== MARKDOWN FILES ==="
find . -name "*.md" ! -path '*/node_modules/*' ! -path '*/.git/*' 2>/dev/null | head -30
```

### 3.2 README Analysis

```bash
echo "=== README CONTENT ANALYSIS ==="
if [ -f "README.md" ]; then
  echo "--- README.md sections ---"
  grep "^#" README.md | head -20
  echo -e "\n--- README.md full content ---"
  cat README.md
fi
```

### 3.3 Code Comments & Inline Docs

```bash
echo "=== INLINE DOCUMENTATION ==="
# Check for JSDoc, docstrings, etc.
echo "Checking for documentation patterns..."

# Python docstrings
find . -name "*.py" ! -path '*/venv/*' ! -path '*/__pycache__/*' -exec grep -l '"""' {} \; 2>/dev/null | head -10 && echo "✓ Python docstrings found"

# JSDoc
find . -name "*.js" -o -name "*.ts" ! -path '*/node_modules/*' -exec grep -l '/\*\*' {} \; 2>/dev/null | head -10 && echo "✓ JSDoc comments found"

# Go doc comments
find . -name "*.go" -exec grep -l '^//' {} \; 2>/dev/null | head -10 && echo "✓ Go doc comments found"
```

**Checkpoint 3:** Present documentation findings:
```
Existing documentation found:

README: [exists/missing] - [brief summary if exists]
Architecture docs: [exists/missing]
API docs: [exists/missing]
Other docs: [list]

1. Continue to source code analysis
2. Show me the README content
3. Show me other documentation
```

---

## Phase 4: Source Code Structure Analysis

### 4.1 Entry Points & Main Files

```bash
echo "=== ENTRY POINTS ==="
# Common entry points
[ -f "main.py" ] && echo "✓ main.py"
[ -f "app.py" ] && echo "✓ app.py"
[ -f "index.js" ] || [ -f "index.ts" ] && echo "✓ index.js/ts"
[ -f "src/index.js" ] || [ -f "src/index.ts" ] && echo "✓ src/index.js/ts"
[ -f "src/main.js" ] || [ -f "src/main.ts" ] && echo "✓ src/main.js/ts"
[ -f "cmd/main.go" ] && echo "✓ cmd/main.go"
[ -f "main.go" ] && echo "✓ main.go"
[ -f "src/main.rs" ] && echo "✓ src/main.rs"
[ -f "lib/main.dart" ] && echo "✓ lib/main.dart"

# Check package.json scripts
if [ -f "package.json" ]; then
  echo -e "\n=== NPM SCRIPTS ==="
  cat package.json | grep -A 20 '"scripts"' | head -25
fi

# Check Makefile targets
if [ -f "Makefile" ]; then
  echo -e "\n=== MAKEFILE TARGETS ==="
  grep "^[a-zA-Z].*:" Makefile | head -20
fi
```

### 4.2 Directory Purpose Inference

```bash
echo "=== DIRECTORY ANALYSIS ==="
for dir in src lib app api components pages routes models controllers services utils helpers hooks types interfaces schemas migrations seeds fixtures config public static assets; do
  [ -d "$dir" ] && echo "✓ $dir/" && ls "$dir" 2>/dev/null | head -10
done
```

### 4.3 Database & Data Layer

```bash
echo "=== DATA LAYER ==="
# Database configs
[ -f "prisma/schema.prisma" ] && echo "✓ Prisma schema" && head -50 prisma/schema.prisma
[ -d "migrations" ] && echo "✓ migrations/" && ls migrations/ | head -10
[ -f "alembic.ini" ] && echo "✓ Alembic (SQLAlchemy migrations)"
[ -d "alembic" ] && echo "✓ alembic/" && ls alembic/versions/ 2>/dev/null | head -10
[ -f "knexfile.js" ] && echo "✓ Knex.js"
[ -f "ormconfig.json" ] || [ -f "ormconfig.js" ] && echo "✓ TypeORM"

# Look for model/schema files
echo -e "\n=== MODELS/SCHEMAS ==="
find . -name "*model*" -o -name "*schema*" -o -name "*entity*" 2>/dev/null | grep -v node_modules | grep -v __pycache__ | head -20
```

---

## Phase 5: BMAD Gap Analysis

Based on all collected information, assess what BMAD artifacts are needed:

### 5.1 Required BMAD Structure

```bash
echo "=== BMAD STRUCTURE CHECK ==="
[ -d ".bmad-core" ] && echo "✓ .bmad-core/ exists" || echo "✗ .bmad-core/ missing - NEEDS SETUP"
[ -d "docs" ] && echo "✓ docs/ exists" || echo "✗ docs/ missing - NEEDS CREATION"
[ -d "docs/stories" ] && echo "✓ docs/stories/ exists" || echo "✗ docs/stories/ missing"
[ -d "docs/prd" ] && echo "✓ docs/prd/ exists" || echo "✗ docs/prd/ missing"
[ -d "docs/architecture" ] && echo "✓ docs/architecture/ exists" || echo "✗ docs/architecture/ missing"
[ -d ".ai" ] && echo "✓ .ai/ exists" || echo "✗ .ai/ missing - NEEDS CREATION"
[ -f "WARP.md" ] && echo "✓ WARP.md exists" || echo "✗ WARP.md missing"
```

### 5.2 Gap Summary

Present to user:
```
=== BMAD Migration Gap Analysis ===

HAVE (from existing project):
- [x] Source code in [detected structure]
- [x] Tech stack: [summary]
- [x] README with [summary]
- [existing docs list]

NEED TO CREATE:
- [ ] docs/ directory structure
- [ ] docs/prd.md (PRD) - can bootstrap from README
- [ ] docs/architecture.md - can bootstrap from detected stack
- [ ] docs/architecture/tech-stack.md
- [ ] docs/architecture/coding-standards.md
- [ ] docs/architecture/source-tree.md
- [ ] .ai/workflow-state.json
- [ ] .bmad-core/ (copy from template)

OPTIONAL:
- [ ] Project brief (if starting fresh planning)
- [ ] Story sharding (if starting development)
```

**Checkpoint 4:** Present gap analysis. Ask:
```
Based on analysis, here's what needs to be created:

[gap list]

How would you like to proceed?
1. Auto-generate all BMAD artifacts from detected info
2. Step through each artifact manually
3. Just create the structure, I'll fill it in
4. Show me what would be generated first
```

---

## Phase 6: BMAD Structure Creation

### 6.1 Create Directory Structure

```bash
echo "=== CREATING BMAD STRUCTURE ==="
mkdir -p docs/stories
mkdir -p docs/prd
mkdir -p docs/architecture
mkdir -p docs/qa
mkdir -p .ai
echo "✓ Directory structure created"
```

### 6.2 Copy .bmad-core (if not present)

```bash
# This assumes template is available - adjust path as needed
if [ ! -d ".bmad-core" ]; then
  echo "Copying .bmad-core from template..."
  # cp -r /path/to/bmad-template/.bmad-core .
  echo "NOTE: Copy .bmad-core manually from template location"
fi
```

### 6.3 Generate tech-stack.md

Based on Phase 2 detection, create `docs/architecture/tech-stack.md`:

```markdown
# Tech Stack

## Core Technologies
[Auto-fill from detection]

## Dependencies
[Auto-fill from package.json/requirements.txt/etc]

## Build & Development
[Auto-fill from detected build tools]

## Testing
[Auto-fill from detected test frameworks]

## Infrastructure
[Auto-fill from detected infra configs]
```

### 6.4 Generate source-tree.md

Based on Phase 4 detection, create `docs/architecture/source-tree.md`:

```markdown
# Source Tree

## Directory Structure
[Auto-generated tree]

## Key Directories
[Purpose of each detected directory]

## Entry Points
[List detected entry points]
```

### 6.5 Bootstrap PRD from README

If README exists, create initial `docs/prd.md` skeleton:

```markdown
# Product Requirements Document

## Project Overview
[Extract from README intro]

## Problem Statement
[Extract or mark as TODO]

## Goals
[Extract from README if present, else TODO]

## Features
[Extract from README features section if present]

## Technical Requirements
[Reference architecture.md]

---
*This PRD was bootstrapped from existing README. Review and expand each section.*
```

### 6.6 Bootstrap Architecture from Detection

Create initial `docs/architecture.md`:

```markdown
# Architecture Document

## System Overview
[Brief description based on detected stack]

## Tech Stack
See: [tech-stack.md](architecture/tech-stack.md)

## Source Structure
See: [source-tree.md](architecture/source-tree.md)

## Key Components
[List main directories/modules detected]

## Data Layer
[Database/ORM info if detected]

## External Integrations
[APIs/services if detected]

---
*This architecture doc was bootstrapped from codebase analysis. Review and expand.*
```

### 6.7 Create workflow-state.json

```bash
cat > .ai/workflow-state.json << EOF
{
  "currentPhase": "BROWNFIELD_ONBOARDED",
  "activeAgent": null,
  "activeStory": null,
  "lastCheckpoint": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "uncommittedWork": false,
  "currentBranch": "$(git branch --show-current 2>/dev/null || echo 'main')",
  "completedArtifacts": ["brownfield-migration"],
  "pendingActions": ["review-prd", "review-architecture", "create-stories"],
  "migrationSource": {
    "originalReadme": true,
    "detectedStack": "[STACK_SUMMARY]",
    "migrationDate": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  }
}
EOF
```

### 6.8 Update .gitignore

```bash
# Add BMAD-specific ignores if not present
if ! grep -q ".ai/\*" .gitignore 2>/dev/null; then
  echo -e "\n# BMAD AI files\n.ai/*\n!.ai/workflow-state.json.template" >> .gitignore
  echo "✓ Updated .gitignore"
fi
```

---

## Phase 7: Migration Report

Present final report:

```
🔄 BMAD Brownfield Migration Complete

📊 Project Analysis:
   Repository: [name from git remote or folder]
   Languages: [detected]
   Frameworks: [detected]
   Lines of Code: [if calculated]

📁 Created Structure:
   ✓ docs/
   ✓ docs/stories/
   ✓ docs/prd/ 
   ✓ docs/architecture/
   ✓ .ai/workflow-state.json

📄 Generated Artifacts:
   ✓ docs/prd.md (bootstrapped from README)
   ✓ docs/architecture.md (bootstrapped from detection)
   ✓ docs/architecture/tech-stack.md
   ✓ docs/architecture/source-tree.md

⚠️ Requires Manual Review:
   - docs/prd.md - expand requirements
   - docs/architecture.md - add design decisions
   - docs/architecture/coding-standards.md - define standards

🔮 Recommended Next Steps:
   1. Review and refine docs/prd.md with PM agent
   2. Review and refine docs/architecture.md with Architect agent
   3. Run PO to validate and shard documents
   4. Begin story creation with SM agent

Would you like me to:
1. Switch to PM to review/refine the PRD
2. Switch to Architect to review/refine architecture
3. Show detailed migration log
4. Commit migration changes now
```

---

## Rollback (if needed)

If migration needs to be undone:

```bash
# Remove created directories (CAREFUL - only if empty or newly created)
rm -rf docs/stories docs/prd docs/architecture .ai
# Remove generated files
rm -f docs/prd.md docs/architecture.md
# Restore .gitignore if backed up
```

---

## Post-Migration Checklist

- [ ] Review docs/prd.md - ensure it captures actual requirements
- [ ] Review docs/architecture.md - ensure it reflects actual design
- [ ] Create docs/architecture/coding-standards.md based on existing patterns
- [ ] Verify .bmad-core/ is properly installed
- [ ] Run `*help` to confirm orchestrator is functional
- [ ] Create first story to test workflow
