# user-service

## Deploy manually on Docker

Run `docker-compose` command, remember to provide GITHUB_TOKEN because user-service needs it to install package from private repositories.

```bash
echo 'GITHUB_TOKEN=your_github_token' >> .env
docker-compose up -d
```

Application will be available at `http://localhost:8000`

## Deploy on Kubernetes

Not supported yet but in the future, there is something like:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: user-service-secret
type: Opaque
data:
  GITHUB_TOKEN: your_base64_encoded_github_token
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 1
  selector:
    matchLabels:
    app: user-service
  template:
    metadata:
    labels:
      app: user-service
    spec:
    containers:
    - name: user-service
      image: ghcr.io/your_github_username/user-service:latest
      envFrom:
      - secretRef:
        name: user-service-secret
      ports:
      - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: user-service
spec:
  selector:
    app: user-service
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
```
