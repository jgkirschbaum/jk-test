# Helm Chart jk-test

Use it like any other Helm Chart.

## Helm repo setup

Once Helm is locally installed, add the repo as follows:

```bash
helm repo add jk-test https://jgkirschbaum.github.io/jk-test
```

If you had already added this repo earlier, run `helm repo update` to retrieve
the latest versions of the packages.  You can then run `helm search repo jk-test`
to see the charts.

## App installation

To install the `jk-test` chart:

```bash
helm upgrade --install -n mynamespace my-jk-test jgkirschbaum/jk-test
```

## App uninstallation

To uninstall the chart:

```bash
helm delete -n mynamespace my-jk-test
```
