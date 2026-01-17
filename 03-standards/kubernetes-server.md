---
title: Servidor Kubernetes - Infraestrutura Doze Crew
status: active
version: 1.0.0
owners:
  - Gabriel
updated: 2026-01-17
tags:
  - infrastructure
  - kubernetes
  - server
  - deploy
---

# Servidor Kubernetes - Doze Crew

## Informações do Servidor

| Atributo | Valor |
|----------|-------|
| **IP** | 78.109.16.236 |
| **Acesso** | SSH (root) |
| **Provider** | [A definir] |
| **Localização** | [A definir] |

> ⚠️ **IMPORTANTE**: Credenciais de acesso devem ser armazenadas em gerenciador de senhas seguro, NUNCA em código ou documentação pública.

## Configuração do Cluster

### Ingress NGINX

O cluster utiliza **Ingress NGINX** como controller padrão para roteamento de tráfego.

```yaml
# Padrão de Ingress para novos projetos
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: <projeto>-ingress
  namespace: <projeto>-prod
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  tls:
    - hosts:
        - <subdomain>.dozecrew.com
      secretName: <projeto>-tls
  rules:
    - host: <subdomain>.dozecrew.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: <projeto>-service
                port:
                  number: 80
```

### Cert-Manager

Certificados TLS são gerenciados automaticamente via **Let's Encrypt**.

```yaml
# ClusterIssuer configurado
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: contato@dozecrew.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      - http01:
          ingress:
            class: nginx
```

## Serviços Existentes no Cluster

| Namespace | Serviço | Domínio | Status |
|-----------|---------|---------|--------|
| dozecrew-prod | portal | tech.dozecrew.com | Planejado |

## Padrões de Deploy

### Estrutura de Namespace

Cada projeto deve ter seu próprio namespace:

```
<projeto>-prod    # Produção
```

> **Nota**: Staging removido para projetos menores.

### Estrutura de Manifests

```
k8s/
├── namespace.yaml
├── configmap.yaml
├── secrets.yaml
├── deployment.yaml
├── service.yaml
├── ingress.yaml
└── hpa.yaml
```

### Deployment Padrão

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: <projeto>-app
  namespace: <projeto>-prod
spec:
  replicas: 2
  selector:
    matchLabels:
      app: <projeto>
  template:
    metadata:
      labels:
        app: <projeto>
    spec:
      containers:
        - name: app
          image: ghcr.io/gabartista/<projeto>:latest
          ports:
            - containerPort: 8000
          envFrom:
            - configMapRef:
                name: <projeto>-config
            - secretRef:
                name: <projeto>-secrets
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /api/health
              port: 8000
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /api/health
              port: 8000
            initialDelaySeconds: 5
            periodSeconds: 5
```

## Comandos Úteis

```bash
# Verificar status do cluster
kubectl get nodes

# Listar todos os pods
kubectl get pods --all-namespaces

# Verificar ingresses
kubectl get ingress --all-namespaces

# Logs de um pod
kubectl logs <pod-name> -n <namespace>

# Describe de um recurso
kubectl describe pod <pod-name> -n <namespace>

# Rollback de deployment
kubectl rollout undo deployment/<nome> -n <namespace>

# Verificar certificados
kubectl get certificates --all-namespaces
```

## Processo de Deploy

### Via GitHub Actions

1. Push para branch `prod`
2. GitHub Actions builda imagem Docker
3. Push para GitHub Container Registry
4. Apply dos manifests K8s
5. Rollout do deployment

### Manual (Emergência)

```bash
# 1. Conectar ao servidor
ssh root@78.109.16.236

# 2. Aplicar manifests
kubectl apply -f k8s/

# 3. Verificar rollout
kubectl rollout status deployment/<nome> -n <namespace>

# 4. Verificar pods
kubectl get pods -n <namespace>
```

## Segurança

### Boas Práticas

- [ ] Secrets nunca em código
- [ ] RBAC configurado por namespace
- [ ] Network policies entre namespaces
- [ ] Imagens sempre de registries confiáveis
- [ ] Scan de vulnerabilidades em CI

---

## Histórico

| Data | Alteração |
|------|-----------|
| 2026-01-17 | Documento criado |

