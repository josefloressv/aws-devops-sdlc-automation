"""CodeDeploy PreTraffic lifecycle hook.

CodeDeploy blocks the deployment until this reports back, so the
put_lifecycle_event_hook_execution_status call is the whole contract.
"""

import boto3

codedeploy = boto3.client("codedeploy")


def lambda_handler(event, context):
    print("PreTraffic hook event: %s" % event)
    codedeploy.put_lifecycle_event_hook_execution_status(
        deploymentId=event["DeploymentId"],
        lifecycleEventHookExecutionId=event["LifecycleEventHookExecutionId"],
        status="Succeeded",
    )
    return {"status": "Succeeded"}
