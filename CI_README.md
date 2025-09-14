
# DevSecOps CI/CD (GitHub Actions)

## Includes
- SCA: `pip-audit`
- SAST: `bandit`
- Tests: `pytest`
- Container build: Docker
- Image & FS scanning: Trivy
- DAST: OWASP ZAP Baseline against http://localhost:8000

## Use
1. Copy `.github/workflows/security-ci.yml` into your repo.
2. Add `Dockerfile` at the repo root.
3. (Optional) Add `.zap/rules.tsv` to tune ZAP alerts.
4. Commit and push to `main`/`master`. The workflow runs on push and PRs.

## Enforce blocking
- Remove `|| true` in SCA/SAST steps.
- Change Trivy `exit-code: '0'` to `1` to fail on findings.
- Replace the demo HTTP server with your real app to scan it with ZAP.
