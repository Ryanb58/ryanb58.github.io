---
title: "Spinnaker"
date: 2019-02-05T09:46:53-05:00
draft: true
toc: false
images:
tags:
  - spinnaker
---

I tried using this [click-to-deploy](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/spinnaker) image but I was unable to access a working version of the UI quickly.

I moved on to installing it via Cloud Console:

1) Download and install the halyard CLI tool.

https://www.spinnaker.io/setup/install/halyard/#install-on-debianubuntu-and-macos

2) Auth `kubctl` w/ the `gcloud` command.

```
gcloud container clusters get-credentials spinnaker --zone us-central1-a
```

3) Skip to part 2.

https://www.spinnaker.io/setup/quickstart/halyard-gke/


### Need to upgrade Spinnaker later on?

https://www.spinnaker.io/setup/install/deploy/#upgrade-spinnaker


## Resources:

https://cloud.google.com/blog/products/gcp/spinnaker-10-continuous-delivery

### Kubernetes Comics

https://cloud.google.com/kubernetes-engine/kubernetes-comic/?utm_source=free-trial-2&utm_medium=email&utm_campaign=2018-FTON-Experiment-Engagement-GKE1-en&utm_content=ft-en

### Amazing CodeLab that walks you through deploying your first image:

https://codelabs.developers.google.com/codelabs/cloud-hello-kubernetes/index.html#0
