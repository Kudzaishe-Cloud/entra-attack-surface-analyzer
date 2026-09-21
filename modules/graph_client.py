import os
from dotenv import load_dotenv
import requests
from typing import Dict, List, Any

load_dotenv()

class GraphAPIClient:
    """Wrapper for Microsoft Graph API calls"""

    def __init__(self):
        self.tenant_id = os.getenv("TENANT_ID")
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.token = None
        self.base_url = "https://graph.microsoft.com/v1.0"

    def authenticate(self):
        """Get access token from Entra ID"""
        auth_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"

        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": "https://graph.microsoft.com/.default",
            "grant_type": "client_credentials"
        }

        response = requests.post(auth_url, data=payload)
        response.raise_for_status()
        self.token = response.json()["access_token"]
        print("✅ Authentication successful")

    def get_headers(self):
        """Return headers with token"""
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get_all_users(self) -> List[Dict[str, Any]]:
        """Fetch all users in the organization"""
        url = f"{self.base_url}/users?$select=id,userPrincipalName,accountEnabled,createdDateTime"

        users = []
        while url:
            response = requests.get(url, headers=self.get_headers())
            response.raise_for_status()
            data = response.json()
            users.extend(data.get("value", []))
            url = data.get("@odata.nextLink")

        return users

    def get_all_applications(self) -> List[Dict[str, Any]]:
        """Fetch all registered applications"""
        url = f"{self.base_url}/applications?$select=id,appId,displayName,createdDateTime,lastModifiedDateTime,publisherDomain"

        apps = []
        while url:
            response = requests.get(url, headers=self.get_headers())
            response.raise_for_status()
            data = response.json()
            apps.extend(data.get("value", []))
            url = data.get("@odata.nextLink")

        return apps

    def get_service_principals(self) -> List[Dict[str, Any]]:
        """Fetch all service principals (app instances)"""
        url = f"{self.base_url}/servicePrincipals?$select=id,appId,displayName,createdDateTime,accountEnabled,appOwnerOrganizationId"

        sps = []
        while url:
            response = requests.get(url, headers=self.get_headers())
            response.raise_for_status()
            data = response.json()
            sps.extend(data.get("value", []))
            url = data.get("@odata.nextLink")

        return sps

    def get_conditional_access_policies(self) -> List[Dict[str, Any]]:
        """Fetch all conditional access policies"""
        url = f"{self.base_url}/identity/conditionalAccess/policies"

        policies = []
        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        policies = response.json().get("value", [])

        return policies

    def get_authentication_methods_policy(self) -> Dict[str, Any]:
        """Fetch MFA/authentication policy"""
        url = f"{self.base_url}/policies/authenticationMethodsPolicy"

        response = requests.get(url, headers=self.get_headers())
        response.raise_for_status()
        return response.json()
