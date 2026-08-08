# aws-devops-sdlc-automation

Application source for the DOP-C02 Domain 1 (SDLC Automation) labs.

This repository is the **source artifact** consumed by pipelines. It deliberately contains
**no pipeline infrastructure** — the CloudFormation templates that build the pipelines,
ECS/CodeDeploy, EventBridge rules and EKS deploy projects live in a separate repository
(`aws-devops-engineer`, under `scenarios/domain-1-sdlc/`).

## Layout

| Path | Purpose |
| --- | --- |
| `app/handler.py` | Lambda handler. Reads `ENV_NAME` / `LOG_LEVEL`. Carries one deliberate unused import so flake8 has something to report. |
| `tests/test_handler.py` | Unit tests. `FORCE_FAIL=1` turns the third one red. |
| `tests/integration/test_api.py` | Integration test against a deployed HTTP API, URL from `API_URL`. |
| `buildspec.yml` | Main build. Declares the same JUnit XML in both `reports:` and `artifacts:`, and emits two secondary artifacts. |
| `buildspec-integration.yml` | Integration test stage. Resolves the endpoint from CloudFormation stack outputs at run time. |
| `infra/app-template.yaml` | Plain CloudFormation for the app. One body, deployed to several environments. |
| `params/{dev,staging,prod}.json` | CodePipeline `TemplateConfiguration` files — parameters and tags per environment. |
| `docker/Dockerfile` | nginx image built twice with a `COLOR` build-arg to produce `:blue` and `:green`. |
| `ecs/appspec.yaml` | CodeDeploy AppSpec, ECS format. |
| `sam-canary/` | SAM template with `AutoPublishAlias` + `DeploymentPreference` and the two CodeDeploy lifecycle hooks. |
| `eks/` | Manifests and the two buildspecs for the manifests-plus-image-URI artifact pattern. |

## Note on placeholders

This repository is public. Values that embed the AWS account ID are committed as placeholders
and substituted at deploy time:

- `ecs/appspec.yaml` → `TASK_DEFINITION_ARN_PLACEHOLDER`
- `eks/k8s/deployment.yaml` → `IMAGE_URI_PLACEHOLDER`

## Running the tests locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/test_handler.py
flake8 app/
```
