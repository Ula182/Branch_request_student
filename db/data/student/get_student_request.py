from utils import core
from fastapi import HTTPException
from boto3.dynamodb.conditions import Key
from db.entity.branch import ReqSample
from typing import List


def get_request_of_student(student_id: str) -> List:
    gsi2pk = ReqSample.get_gsi2pk(student_id)
    response = core.table.query(
        IndexName='GSI2',
        KeyConditionExpression=Key('GSI2PK').eq(gsi2pk)
    )
    items = response.get('Items', [])
    if not items:
        raise HTTPException(status_code=404, detail='Not Found')
    return items