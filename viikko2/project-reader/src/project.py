class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}" +
            f"\nLicense {self.license or '-'}\n" +
            self._nicer_authors() +
            self._nicer_dependencies() +
            self._nicer_dev_dependencies()
        )
    def _nicer_authors(self):
        authors = ""
        for author in self.authors:
            authors += f"\n- {author}"
        return f"\nAuthors:" + authors

    def _nicer_dependencies(self):
        return f"\n\nDependencies:\n {self._stringify_dependencies(self.dependencies)}"

    def _nicer_dev_dependencies(self):
        return f"\n\nDevelopment dependencies:\n {self._stringify_dependencies(self.dev_dependencies)}"
