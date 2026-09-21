from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.utils.access_control import require_permission
from app.schemas.permission_schema import Resource, Action, AccessScope
from app.database import get_db

from app.controllers.admin_controller import (
    approve_user,
    reject_user,
    resend_approval,
    view_user_document
)

router = APIRouter(prefix="/notify", tags=["Notify"])

@router.get("/admin/approval/resend")
def resend_approval_route(
    user_id: int,
    db: Session = Depends(get_db),
    scope: AccessScope = Depends(require_permission(Resource.USER_MGMT, Action.MANAGE))
):   
    return resend_approval(user_id, scope.user_id, db)

@router.get("/admin/approval/approve")
def approve_user_route(token: str, db: Session = Depends(get_db)):
    return approve_user(token, db)


@router.get("/admin/approval/reject")
def reject_user_route(token: str, db: Session = Depends(get_db)):
    return reject_user(token, db)

@router.get("/admin/document/view")
def view_user_document_route(token: str, db: Session = Depends(get_db)):
    return view_user_document(token, db)