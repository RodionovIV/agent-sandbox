from jira import JIRA


class JiraTool:
    def __init__(self):
        self.jira = JIRA(
            server="https://your-jira-server", basic_auth=("username", "password")
        )

    def create_task(self, email, assignee):
        issue_dict = {
            "project": {"key": "YOUR_PROJECT_KEY"},
            "summary": email["subject"],
            "description": email["body"],
            "issuetype": {"name": "Task"},
            "assignee": {"name": assignee},
        }
        self.jira.create_issue(fields=issue_dict)
