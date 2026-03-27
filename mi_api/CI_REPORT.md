# CI REPORT

## Pipeline

```mermaid
graph TD;
A[Push] --> B[Install]
B --> C[Lint]
C --> D[Test]
D --> E[Coverage]