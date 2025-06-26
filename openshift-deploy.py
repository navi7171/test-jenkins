from kubernetes import client, config

# Load kube config
config.load_kube_config()

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
