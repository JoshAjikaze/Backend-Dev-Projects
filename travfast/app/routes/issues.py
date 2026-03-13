import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueStatus, IssueOut, IssueUpdate
from app.storage import load_data, save_data

router = APIRouter(prefix="/api/vi/issues", tags=["issues"])

# Get all Issues
@router.get("/", response_model=list[IssueOut])
async def get_issues():
    """Retrieve all issues"""
    issues = load_data()
    return issues

# Get single Issue
@router.get("/{id}", response_model=IssueOut)
async def get_issue(id:str):
    """get single issue"""
    issues = load_data()
    for issue in issues:
        if issue["id"] == id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Issue not found")

# Create Issue
@router.post("/", response_model=IssueOut, status_code= status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate):
    """Create new Issue"""
    issues = load_data()
    new_issue = {
        "id" : str(uuid.uuid4()),
        "title" : payload.title,
        "description" : payload.description,
        "priority" : payload.priority,
        "status" : IssueStatus.open
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue

# Update issue
@router.patch("/{id}", response_model=IssueOut)
async def update_issue(id:str, payload:IssueUpdate):
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == id:
            current_issue = issue
            if payload.title is not None:
                current_issue["title"] = payload.title
            if payload.description is not None:
                current_issue["description"] = payload.description
            if payload.priority is not None:
                current_issue["priority"] = payload.priority
            if payload.status is not None:
                current_issue["status"] = payload.status
            
            issues[index] = current_issue
            save_data(issues)
            return current_issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

# delete issue 
@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_issue(id:str):
    """Delete an issue"""
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == id:
            current_issue = issues[index]
            issues.remove(current_issue)
            save_data(issues)
            return issues
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")