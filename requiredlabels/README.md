# Required-labels

### Description:
This policy requires specified labels to be included for object requests.  
In this specific example, all namespaces and pods require the **created-by** label.

### The Examples:
The file **positive-example.yaml** defines the created-by to security, thus the namespace is approved by this policy.

```
apiVersion: v1
kind: Namespace
metadata:
  labels:
    created-by: security
  name: good-namespace

```
The file **negative-example.yaml** does not contain the required label, This namespace should be denied.

```
apiVersion: v1
kind: Namespace
metadata:
  labels:
    app: test
  name: bad-namespace

```
