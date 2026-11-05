
# Internship Tools

Custom tools for ERPNext built using the Frappe Framework.

Internship Tools is a demo application designed to manage internship tasks between interns and mentors. It allows mentors to assign tasks, monitor progress through task statuses, and manage tasks across interns.

## Features

- Create and manage internship tasks.
- Assign tasks to individual interns.
- Track task status and priority.
- Set due dates for tasks.
- Validate task titles to prevent empty values.
- Prevent due dates from being changed to dates in the past.
- Mark tasks as completed using a custom **Complete Task** button.
- Restrict interns to viewing and managing their own assigned tasks.
- Allow mentors to view and manage tasks across interns.
- Prevent interns from deleting tasks.
- Apply server-side permission checks for secure task access.

## Tech Stack

- **Framework:** Frappe Framework v16
- **ERP Platform:** ERPNext
- **Backend:** Python
- **Frontend:** JavaScript
- **Database:** MariaDB

## Main DocType

### Internship Task

The `Internship Task` DocType is used to manage task information.

| Field | Description |
|---|---|
| Task Title | Title of the task |
| Description | Details about the task |
| Status | Current task status |
| Due Date | Task deadline |
| Assigned To | User responsible for the task |
| Priority | Task priority |

## Roles and Permissions

| Role | Access |
|---|---|
| Intern | View and update assigned tasks; cannot delete tasks |
| Mentor | View and manage tasks across interns |
| System Manager | Administrative task management |

The application uses permission query conditions and document-level permission checks to enforce access restrictions.

## Validations

### Task Title

The Task Title field is required and cannot contain only whitespace.

### Due Date

When the Due Date is changed, the application checks that the new date is not in the past.

## Task Completion Workflow

1. A mentor creates a task and assigns it to an intern.
2. The intern views the assigned task.
3. The intern works on the task and updates its status.
4. The task can be marked as completed using the **Complete Task** button.
5. The status changes to `Completed`, and a green Completed indicator is displayed.

## Installation

You can install this app using the [Bench CLI](https://github.com/frappe/bench):

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch version-16
bench --site $SITE_NAME install-app internship_tools
```

Replace `$URL_OF_THIS_REPO` with the repository URL and `$SITE_NAME` with your Frappe site name.

## Development

Start the development environment:

```bash
bench start
```

To apply changes to the site:

```bash
bench --site $SITE_NAME migrate
```

## Contributing

This app uses `pre-commit` for code formatting and linting.

Install and enable it:

```bash
cd apps/internship_tools
pre-commit install
```

Pre-commit is configured to use the following tools:

- Ruff
- ESLint
- Prettier
- PyUpgrade

## CI

This app can use GitHub Actions for continuous integration.

The configured workflows include:

- **CI:** Installs the app and runs unit tests on pushes to the `develop` branch.
- **Linters:** Runs Frappe Semgrep rules and `pip-audit` checks on pull requests.

## What I Learned

- Creating custom DocTypes using the Frappe Framework.
- Implementing server-side validation using Python.
- Working with document lifecycle methods.
- Implementing role-based access control.
- Using permission query conditions and document-level permission checks.
- Creating whitelisted methods and custom form actions.
- Testing permissions across different user roles.
- Debugging issues in a Frappe application.

## License

MIT
