# enumerate — display git log with commit index
commits = [
    "fix: correct off-by-one error in pagination",
    "feat: add JWT authentication",
    "refactor: extract db connection to module",
    "docs: update README with setup steps",
    "test: add unit tests for user model",
]

print("Recent commits:")
for index, message in enumerate(commits, start=1):
    print(f"  {index}. {message}")
