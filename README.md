# {{FULL_NAME}} — Data Engineering Portfolio

> Cohort: `{{COHORT}}` · Abnuel Analytics — Data Engineering (GCP)

This repository holds my three capstone projects from the track, each built on Google Cloud with production practices: infrastructure as code, orchestration, testing, CI/CD, and observability.

## portfolio-template — Pre-commit & Quality Checks

Quality checks that run automatically before every commit (and in CI). They keep the repo
clean, consistent, and — because this repo is **public** — free of accidentally-committed secrets.

## One-time setup

```bash
pip install pre-commit      # or: uv tool install pre-commit
pre-commit install          # hooks now run on every `git commit`
```

That's it — from now on the checks run automatically when you commit. To also run them at
push time: `pre-commit install --hook-type pre-push`.

## Everyday use

- They run on the files you changed each time you `git commit`.
- If a hook **fixes** something (formatting, trailing whitespace), re-stage and commit again.
- Run everything by hand any time: `pre-commit run --all-files`.
- Skip once in an emergency: `git commit --no-verify` (avoid — CI will still catch it).
- Update hook versions: `pre-commit autoupdate`.

## What runs

| Hook | What it checks |
|------|----------------|
| `trailing-whitespace`, `end-of-file-fixer`, `mixed-line-ending` | Clean line endings and file endings. |
| `check-yaml`, `check-json`, `check-toml` | Config files actually parse. |
| `check-added-large-files` | Blocks files over 5 MB (keep data out of git). |
| `check-merge-conflict`, `check-case-conflict` | No conflict markers; no case-clashing filenames. |
| `check-executables-have-shebangs`, `check-shebang-scripts-are-executable` | Scripts are consistent. |
| `detect-private-key` + **`gitleaks`** | **Secret scanning** — blocks keys/tokens before they reach a public repo. |
| `ruff`, `ruff-format` | Python linting + formatting. |
| **`sqlfluff-lint`** | SQL linting — BigQuery dialect, dbt-aware (understands `ref()`/`source()` with no credentials). |
| `yamllint` | YAML style (tuned for GitHub Actions / dbt / k8s). |
| `markdownlint` | Markdown style (relaxed for technical docs). |
| `terraform_fmt` | Terraform formatting (only when `.tf` files change). |

Config lives in `.pre-commit-config.yaml`, `.sqlfluff`, `.yamllint.yaml`, and `.markdownlint.yaml` —
edit those to tune rules for your work.

## CI backstop

`.github/workflows/checks.yml` runs the **same** hooks on every pull request and push to `main`,
so the checks hold even if someone commits with `--no-verify`. One source of truth
(`.pre-commit-config.yaml`), enforced both locally and remotely.

## Projects

| # | Project | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 1 | [Batch ELT Pipeline](./capstone-1-batch-elt) | Terraform-provisioned batch ELT into BigQuery | 🚧 |
| 2 | [Orchestrated Lakehouse](./capstone-2-orchestrated-lakehouse) | Airflow + dbt + BigQuery medallion, multi-env | 🚧 |
| 3 | [Production Data Platform](./capstone-3-production-platform) | Streaming + batch, GKE/Cloud Run, CI/CD, observability | 🚧 |

## How to read this repo

- Each `capstone-*/` folder has its own `README.md` with the architecture, how to run it, and what I'd do differently.
- [`docs/decisions.md`](./docs/decisions.md) is my running decision journal — the *why* behind the choices.
- [`docs/architecture/`](./docs/architecture) holds the diagrams.

## About me

<!-- One or two lines: who you are, what you're targeting. Replace at graduation. -->

---
_Built during the Abnuel Analytics Data Engineering Production Track._
