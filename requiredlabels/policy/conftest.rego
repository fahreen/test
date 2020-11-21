package k8srequiredlabels

required_namespace_labels {
    input.metadata.labels["created-by"]
}

violation[{"msg": msg}] {
  input.kind == "Namespace"
  not required_namespace_labels
  msg = "You must provide created-by labels"
}


