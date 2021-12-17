> Create a bash script to deploy your lambda functions

The bash script for the lambda function is writtern as: 

```
#!/bin/bash

zip lam.zip lambda_function.py

aws lambda update-function-code \
        --function-name "prajesh-hello" \
        --zip-file "fileb://./lam.zip" \
        --region "us-east-1"
```

---

> Create a bash script to deploy your react app to S3

The bash script to deploy react app:

```
#!/bin/bash

npm run build

aws s3 sync build s3://prajesh-react
```

---

> Integrate both these scripts with one of Jenkins, Github Actions, CircleCI or TravisCI

I used **Github Actions** as I am familiar with it, and have used it once in the past.


So for the lambda the github repo https://github.com/prajeshpradhan/cicd-lamda is used.

with the workflow written as 

```
# This is a basic workflow to help you get started with Actions

name: Deploy Lamda Code

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel

jobs:
  deploy:
    name: Upload to lambda
    runs-on: ubuntu-latest
    # These permissions are needed to interact with GitHub's OIDC Token endpoint.
    permissions:
      id-token: write
      contents: read
    steps:
    - name: Checkout
      uses: actions/checkout@v2

    - name: Configure AWS credentials from Test account
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1
        
    - name: Run Deploy Bash
      run: |
         chmod +x ./lambda.sh
         ./lambda.sh
      shell: bash
```
![Lambda Deploy](screenshots/Lambda%20Deploy.png)

For the deployment of react app to S3 Bucket: https://github.com/prajeshpradhan/cicd-react

```

name: Deploy Lamda Code

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel

jobs:
  deploy:
    name: Upload to Amazon S3
    runs-on: ubuntu-latest
    # These permissions are needed to interact with GitHub's OIDC Token endpoint.
    permissions:
      id-token: write
      contents: read
    steps:
    - name: Checkout
      uses: actions/checkout@v2

    - name: Configure AWS credentials from Test account
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1
        
    - uses: actions/setup-node@v2
      with:
        node-version: '14'
        cache: 'npm'
    - run: npm install
        
    - name: Run Deploy Bash
      run: |
         chmod +x ./deploy.sh
         ./deploy.sh
      shell: bash
```

Now if any changes are pushed to the repo, its automatically deployed, which is the essence of CI/CD

![React deploy](screenshots/react%20deploy.png)

