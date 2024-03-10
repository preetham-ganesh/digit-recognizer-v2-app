# Digit Recognizer v2 (App)

This repository contains UI & API code used in the Digit Recognizer project.

## Contents

- [Related Repositories](https://github.com/preetham-ganesh/digit-recognizer-v2-app#related-repositories)
- [Installation](https://github.com/preetham-ganesh/digit-recognizer-v2-app#installation)
- [Usage](https://github.com/preetham-ganesh/digit-recognizer-v2-app#usage)
- [Releases](https://github.com/preetham-ganesh/digit-recognizer-v2-app#releases)

## Related Repositories

- [Digit Recognizer v2 (Training)](https://github.com/preetham-ganesh/digit-recognizer-v2-training)

- [Digit Recognizer v2 (Serving)](https://github.com/preetham-ganesh/digit-recognizer-v2-serving)

## Installation

```bash
git clone https://github.com/preetham-ganesh/digit-recognizer-v2-app
cd digit-recognizer-v2-app
```

## Usage

Requires: [Docker](https://www.docker.com)

### Local Deployment

Update app.py & Dockerfile based on deployment choice (instructions provided in code files).

Use the following code snippet to deploy the docker container locally:

```bash
docker build -t digit-recognizer-v2-app .
docker run -p 3000:3000 digit-recognizer-v2-app
```
