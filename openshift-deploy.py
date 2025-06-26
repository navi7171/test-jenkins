from kubernetes import client, config

# Load kube config
config.load_kube_config()

# Delete existing pod if it exists
try:
    v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
    print(f"Deleted existing pod: {pod_name}")
    # Wait for deletion to complete
    import time
    time.sleep(2)
except ApiException as e:
    if e.status == 404:
        print("Pod does not exist, creating new one.")
    else:
        raise

# Define pod spec
pod_manifest = {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {"name": "demo-pod"},
    "spec": {
        "containers": [
            {
                "name": "demo-container",
                "image": "nginx",
                "ports": [{"containerPort": 80}]
            }
        ]
    }
}

# Create pod
v1 = client.CoreV1Api()
namespace = "main"  # Change to your OpenShift namespace/project

resp = v1.create_namespaced_pod(body=pod_manifest, namespace=namespace)
print(f"Pod '{resp.metadata.name}' created in namespace '{namespace}'")
