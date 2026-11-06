terraform {
  required_providers {
    kind = {
      source  = "tehcyx/kind"
      version = "0.6.0"
    }
  }
}

provider "kind" {}

resource "kind_cluster" "devops_cluster" {
  name       = "terraform-devops-cluster"
  node_image = "kindest/node:v1.31.0"

  kind_config {
    kind        = "Cluster"
    api_version = "kind.x-k8s.io/v1alpha4"

    node {
      role = "control-plane"
    }
  }
}

output "cluster_name" {
  value = kind_cluster.devops_cluster.name
}
