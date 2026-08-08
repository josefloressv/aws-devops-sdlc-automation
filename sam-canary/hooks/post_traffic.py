"""CodeDeploy PostTraffic lifecycle hook."""

import boto3

codedeploy = boto3.client("codedeploy")


def lambda_handler(event, context):
    print("PostTraffic hook event: %s" % event)
    codedeploy.put_lifecycle_event_hook_execution_status(
        deploymentId=event["DeploymentId"],
        lifecycleEventHookExecutionId=event["LifecycleEventHookExecutionId"],
        status="Succeeded",
    )
    return {"status": "Succeeded"}
