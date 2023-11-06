# jk-test

[![Docker Hub](https://img.shields.io/badge/Docker-Hub-blue.svg)](https://hub.docker.com/r/jgkirschbaum/jk-test)
[![Kubernetes YAML manifests](https://img.shields.io/badge/Kubernetes-manifests-blue.svg)](https://github.com/jgkirschbaum/jk-test/tree/main/kubernetes)
[![Helm chart](https://img.shields.io/badge/Helm-Chart-informational?style=flat-square)](https://github.com/jgkirschbaum/jk-test/tree/main/charts/jk-test)
[![codebeat badge](https://codebeat.co/badges/1003871b-6ac0-4552-b139-5477b8cfaf4a)](https://codebeat.co/projects/github-com-jgkirschbaum-jk-test-main)
[![release](https://img.shields.io/github/v/release/jgkirschbaum/jk-test.svg)](https://github.com/jgkirschbaum/jk-test/releases)
[![license](https://img.shields.io/badge/license-GPLv3-green)](https://github.com/jgkirschbaum/jk-test/blob/main/LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

## Features

Provides a naked alpine container for testing only with bash and python added.

## Deploy to Kubernetes

### Manifests

Get the K8s manifests from the folder `/kubernetes`.

### Helm

#### Helm repo setup

Once Helm is locally installed, add the repo as follows:

```bash
helm repo add jk-test https://jgkirschbaum.github.io/jk-test
```

If you had already added this repo earlier, run `helm repo update` to retrieve the latest versions of the packages. You can then run `helm search repo jgkirschbaum` to see the charts.

#### App installation

To install the jk-test chart:

```bash
helm upgrade --install -n mynamespace my-jk-test jgkirschbaum/jk-test
```

#### App uninstallation

To uninstall the chart:

```bash
helm delete -n mynamespace my-jk-test
```
