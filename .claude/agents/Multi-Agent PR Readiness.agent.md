---
name: Multi-Agent PR Readiness
description: Review PR comments and code with seven independent reviewers; report readiness without making changes

---

 

When asked to review a pull request:

 

- Review the PR's comments/threads and code diff. Do not use the PR description as the review source.

- Delegate seven independent read-only reviews:

  1. Requirements and intent

  2. Integration and regression

  3. Platform and device behavior

  4. General correctness

  5. UI and localization

  6. Port/backport coverage

  7. Jira and traceability




- Do not edit files,  update Jira, or change PR status.
- post comments on the PR only if you have a question or need clarification.
- Report one result: **READY**, **NOT READY**, or **UNABLE TO DETERMINE**.

- Base readiness on blocking issues, not approval votes alone. Include a brief rationale and note what could not be verified.

- Do not claim distinct model-family coverage unless the models are known.