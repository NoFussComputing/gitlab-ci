---
title: Ansible Collection
description: How to use No Fuss Computings gitlab-ci job for running Ansible Collection CI/CD Pipelines
date: 2024-02-16
template: project.html
about: https://gitlab.com/nofusscomputing/projects/gitlab-ci
---

This CI/CD template contains all of the CI jobs required for a pipeline for an Ansible Collection Project.


## Requirements

The following requirements are needed to run these CI/CD jobs. As we use [commitizen](https://commitizen-tools.github.io/commitizen/) for the versioning system, your commits will be required to be in [conventional commit format](https://www.conventionalcommits.org/en/v1.0.0/). The configuration for commitizen is within a `.cz.yaml` file which you will need to add to your repository root directory.


### Gitlab Features

| Feature | Setting | Notes |
|:---|:---:|:---|
| Package Registry | On | Storage of pipeline artifacts and the built package. |
| Releases | On | Gitlab releases are created as part of the pipeline. |


### Variables

To be able to upload to Ansible Galaxy, you will be required to provide the jobs, the following Variables That should be set as CI/CD variables (`<Project> -> Settings -> CI/CD Settings -> Variables`).

| Variable | Settings | Notes |
|:---|:---:|:---|
| `ANSIBLE_GALAXY_UPLOAD_TOKEN` | `masked`, `protected` |  |
| `VERSION_BUMP_INCREMENT` | `major`, `minor`, `patch` | Used for manual run of the job. After setting the variable, that type of version bump will occur. |

Within your `.gitlab-ci.yml` file there are varibales to be set, please see below.


### .gitlab-ci.yaml Changes

To include these jobs in your CI/CD Project add our gitlab-ci project as a submodule to your project `git submodule add https://gitlab.com/nofusscomputing/projects/gitlab-ci/`. Then update your projects `.gitlab-ci.yml` file to include the following:

``` yaml
variables:
  ANSIBLE_GALAXY_SERVER_URL: https://galaxy.ansible.com    # Optional, default=(as displayed)String. URL to the Galaxy server for uploads
  ANSIBLE_GALAXY_NAMESPACE: ""                             # Mandatory, String. The ansible galaxy upload namespace
  ANSIBLE_GALAXY_PACKAGE_NAME: ""                          # Mandatory, String. The Ansible Galaxy package name

include:
  - project: nofusscomputing/projects/gitlab-ci
    ref: <git ref>    # branch, git tag, commit etc
    file:
      - .gitlab-ci_common.yaml
      - template/ansible-collection.gitlab-ci.yaml
```


## CI/CD Jobs

This template contains the following CI/CD Jobs

- `Create Release`

- `Ansible Lint`

- `Ansible Lint (galaxy.yml)`

- `Build Collection`

- `Stage Collection`

- `Gitlab Release`

- `Ansible Galaxy`

for a detail description of each job, please see below.


### Create Release

Triggered:

- **Feature branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **development branch**: 
    
    - **push**: `manual`

    - **merge to**: `manual`

- **master branch**: 
    
    - **push**: `always`

    - **merge to**: `always`

- **git tag**: `never`

Create a release. It's only triggered on merge to the `development` and `master` branches. The last stage of this job is to create a git tag which matches the version to be released. The creation of the git tag, starts the remainder of the release cycle. On the `development` branch (when the job is triggered as it's a manual job) an `alpha` release is created and on the `master` branch, a full release is created.


### Ansible Lint

Triggered:

- **Feature branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **development branch**: 
    
    - **push**: `manual`

    - **merge to**: `manual`

- **master branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **git tag**: `never`

Lints the yaml files in directories `meta`, `playbooks` and `roles`. This job will not fail the pipeline. There are XUnit test reports created for thyis job so you can see any liniting errors.


### Ansible Lint (galaxy.yml)

Triggered:

- **Feature branch**: 
    
    - **push**: `always`

    - **merge to**: `always`

- **development branch**: 
    
    - **push**: `always`

    - **merge to**: `always`

- **master branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **git tag**: `always`

Lints the `galaxy.yml` file. This job is designed to fail the pipeline, as an incorrectly formated `galaxy.yml` file can prevent an upload of the collection to Ansible Galaxy. There is a XUnit test report created for thyis job so you can see any liniting errors.


### Build Collection

Triggered:

- **Feature branch**: 
    
    - **push**: `always`

    - **merge to**: `always`

- **development branch**: 
    
    - **push**: `always`

    - **merge to**: `always`

- **master branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **git tag**: `always`

Builds the collection.

### Stage Collection

Triggered:

- **Feature branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **development branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **master branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **git tag**: `always`

Adds the collection to Gitlab Packages Regsitry as a generic package. This location is used to store the package.


### Gitlab Release

Triggered:

- **Feature branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **development branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **master branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **git tag**: `always`

Creates a Gitlab release.


### Ansible Galaxy

Triggered:

- **Feature branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **development branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **master branch**: 
    
    - **push**: `never`

    - **merge to**: `never`

- **git tag**: `always`

Uploads the package to Ansible Galaxy.


## CI Tests

Still to be developed


## Definition

``` yaml title="template/ansible-collection.gitlab-ci.yaml" linenums="1"

--8<-- "template/ansible-collection.gitlab-ci.yaml"

```

----

``` yaml title=".gitlab-ci_common.yaml" linenums="1"

--8<-- ".gitlab-ci_common.yaml"

```
