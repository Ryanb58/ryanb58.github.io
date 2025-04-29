title = "Power Automate Flow - Download File From SAP"
date = 2025-04-28T18:23:00+02:00
tags = [
  "power automate",
  "automation",
  "sap integration",
  "flow",
  "microsoft power platform",
  "data extraction",
  "workflow",
  "cloud flows",
  "connectors",
  "process automation",
  "business process",
  "rpa",
]
published = true
+++++

With the low-key launch of the "Reconstruct Attachments" action inside of the SAP ERP Connector for Power Automate, you can download files from SAP. 

Below we will construct a flow that enables this process. The resulting file will land inside of sharepoint.

## Prerequisites

- Sharepoint
- Power Automate License
- Valid SAP credentials
- Proper Permissions
- Previously setup a successful connection between Power Automate & SAP

## Flow Construction

Replace the placeholder `XXX` with your specific configuration and items as needed.

### Manual Trigger

As-Is

### Initialize Variable

```json
{
  "type": "InitializeVariable",
  "inputs": {
    "variables": [
      {
        "name": "Document",
        "type": "string",
        "value": "300001000701152024"
      }
    ]
  }
  ...
}
```

### Call SAP Function

RFC: BDS_BUSINESSDOCUMENT_QUERY_D 

Use the latest version of this. At the time of this writing, it is version 3.

```json
{
  "type": "OpenApiConnection",
  "inputs": {
    "parameters": {
      "x-ms-sap-system": "{\"AppServerHost\":\"XXX\",\"Client\":\"XXX\",\"SystemNumber\":\"XX\",\"LogonType\":\"ApplicationServer\"}",
      "rfcName": "BDS_BUSINESSDOCUMENT_QUERY_D",
      "rfcGroupFilter": "*",
      "autoCommit": false,
      "rfcInputs/CLASSNAME": "BKPF",
      "rfcInputs/CLASSTYPE": "BO",
      "rfcInputs/OBJECT_KEY": "@variables('Document')"
    },
    ...
}
```

### Call SAP Function

RFC: BDS_DOCUMENT_GET_TABLE

```json
{
  "type": "OpenApiConnection",
  "inputs": {
    "parameters": {
      "x-ms-sap-system": "{\"AppServerHost\":\"XXX\",\"Client\":\"XXX\",\"SystemNumber\":\"XX\",\"LogonType\":\"ApplicationServer\"}",
      "rfcName": "BDS_DOCUMENT_GET_TABLE",
      "rfcGroupFilter": "*",
      "autoCommit": false,
      "rfcInputs/DOC_ID": "@body('BDS_BUSINESSDOCUMENT_QUERY_D')['CONNECTIONS'][0]['DOC_ID']",
      "rfcInputs/BINARY_FLAG": "X"
    },
    "host": {
      "apiId": "/providers/Microsoft.PowerApps/apis/shared_saperp",
      "connection": "shared_saperp",
      "operationId": "CallRfcJsonV3"
    }
  },
  ...
}
```

### Create Array

```json
{
  "type": "Select",
  "inputs": {
    "from": "@outputs('BDS_DOCUMENT_GET_TABLE')?['body/CONTENT']",
    "select": "@item()?['LINE']"
  },
  ...
}
```

### Reconstruct Attachment

```json
{
  "type": "OpenApiConnection",
  "inputs": {
    "parameters": {
      "payload": "@body('Create_Base64_Array')"
    },
    "host": {
      "apiId": "/providers/Microsoft.PowerApps/apis/shared_saperp",
      "connection": "shared_saperp",
      "operationId": "AttachmentReconstruct"
    }
  },
  ...
}
```

### Create File - Sharepoint

```json
{
  "type": "OpenApiConnection",
  "inputs": {
    "parameters": {
      "dataset": "https://microsoft.sharepoint.com/teams/XXX",
      "folderPath": "/Shared Documents",
      "name": "@concat(guid(), '.xls')",
      "body": "@base64ToBinary(body('Reconstructs_attachments_from_base64_encoded_parts')?['data'])"
    },
    "host": {
      "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
      "connection": "shared_sharepointonline",
      "operationId": "CreateFile"
    }
  },
  "runAfter": {
    "Reconstructs_attachments_from_base64_encoded_parts": [
      "Succeeded"
    ]
  },
  "runtimeConfiguration": {
    "contentTransfer": {
      "transferMode": "Chunked"
    }
  }
}
```

After running the flow, you'll find your file within your sharepoint directory.


## Successful Flow Run:

![FileDownloadFromSAP Success Screenshot](</static/images/2025/Screenshot 2025-04-29 at 9.27.56 AM.jpg>)

