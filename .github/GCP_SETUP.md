# GCP Deployment Setup

## Prerequisites

1. **GCP Project**: Create or have access to a Google Cloud Project
2. **Enable APIs**: Enable the following APIs in your GCP project:
   - Cloud Run API
   - Artifact Registry API
   - Cloud Build API

## Setup Steps

### 1. Create Service Account

```bash
# Set your project ID
export PROJECT_ID="your-project-id"

# Create service account
gcloud iam service-accounts create github-actions \
    --description="Service account for GitHub Actions" \
    --display-name="GitHub Actions"

# Grant necessary permissions
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:github-actions@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/run.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:github-actions@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:github-actions@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/artifactregistry.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:github-actions@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountUser"

# Create and download service account key
gcloud iam service-accounts keys create key.json \
    --iam-account=github-actions@$PROJECT_ID.iam.gserviceaccount.com
```

### 2. Create Artifact Registry Repository

```bash
# Create repository for Docker images
gcloud artifacts repositories create wealth-assistant-frontend \
    --repository-format=docker \
    --location=us-central1 \
    --description="Docker repository for wealth assistant frontend"
```

### 3. Configure GitHub Secrets

In your GitHub repository, go to Settings > Secrets and variables > Actions, and add these repository secrets:

- **GCP_PROJECT_ID**: Your Google Cloud Project ID
- **GCP_SA_KEY**: Contents of the `key.json` file created above (the entire JSON)

### 4. Environment Variables (Optional)

You can modify these in the workflow file if needed:
- **GAR_LOCATION**: us-central1 (Artifact Registry location)
- **SERVICE**: wealth-assistant-frontend (Cloud Run service name)
- **REGION**: us-central1 (Cloud Run deployment region)

## Manual Deployment Test

To test deployment manually:

```bash
# Build and run locally
cd frontend
docker build -t wealth-assistant-frontend .
docker run -p 8501:8501 wealth-assistant-frontend

# Deploy to Cloud Run manually
gcloud run deploy wealth-assistant-frontend \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
```

## Cleanup

To remove resources:

```bash
# Delete service account
gcloud iam service-accounts delete github-actions@$PROJECT_ID.iam.gserviceaccount.com

# Delete Artifact Registry repository
gcloud artifacts repositories delete wealth-assistant-frontend --location=us-central1

# Delete Cloud Run service
gcloud run services delete wealth-assistant-frontend --region=us-central1
```