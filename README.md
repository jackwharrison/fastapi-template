# fastapi-template

Template repo for FastAPI + CI/CD with Github Actions.

### Deploy to Azure with GitHub Actions

1. Create a Azure Container Registry or choose a pre-existing one.
   * Go to the registry -> `Access keys` -> Enable `Admin user` -> Copy the username and password
2. Create a new App Service Plan in Azure, or choose a pre-existing one.
2. Create a new Web App in Azure:
   * choose a meaningful name, e.g. `fastapi-template-jacopo`
   * select `Publish`: `Docker Container`
   * select `Operating System`: `Linux`
   * select `Region`: `West Europe`
   * select the App Service Plan you created in step 1
   * Create the Web App
3. Get a Web App Publish Profile, to deploy from GitHub
   * Go to your app service in the Azure portal. 
   * On the Overview page, select `Download publish profile`. 
   * Save the downloaded file. You'll use the contents of the file to create a GitHub secret.
4. Create the GitHub secrets and variables
   * Go to your GitHub repository
   * Go to `Settings` -> `Secrets and variables` -> `Actions` -> `New repository secret`
   * Add the following **secrets**:
     * `AZURE_WEBAPP_PUBLISH_PROFILE`: the contents of the downloaded file from step 3
     * `REGISTRY_USERNAME`: the username of the Azure Container Registry, e.g. `fastapiregister`
     * `REGISTRY_PASSWORD`: the password of the Azure Container Registry
   * Go to `Settings` -> `Secrets and variables` -> `Actions` -> `New repository variable`
   * Add the following **variables**:
     * `AZURE_WEBAPP_NAME`: the name of your web app, e.g. `fastapi-template-jacopo`
     * `REGISTRY_URL`: the Azure Container Registry URL, e.g. `fastapiregister.azurecr.io`
5. Push a change to the repository to trigger the GitHub Actions workflow.
4. Wait 5-10 minutes, then go to `<my-api-name>.azurewebsites.net` and see the app running.


### Run locally

```
cp example.env .env
pip install -r requirements.txt
uvicorn main:app --reload
```
