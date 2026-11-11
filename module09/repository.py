# class structure: __init__, self, instance vs class attributes

class Repository:
    default_branch = "main"  # class attribute — shared across all instances

    def __init__(self, name, owner):
        self.name = name        # instance attributes — unique per object
        self.owner = owner
        self.stars = 0
        self.branches = []

    def star(self):
        self.stars += 1

    def info(self):
        return f"{self.owner}/{self.name} [{self.default_branch}] stars:{self.stars}"


repo = Repository("django", "django")
repo.star()
repo.star()
print(repo.info())

repo2 = Repository("flask", "pallets")
print(repo2.info()) 

# class attribute is accessible on the class itself and on any instance
print(Repository.default_branch)
print(repo.default_branch)
# mutating a class attribute on an instance creates a new instance attribute (shadows it)
repo.default_branch = "develop"
print(repo.default_branch)         # develop  (instance shadow)
print(Repository.default_branch)   # main     (class attr unchanged)