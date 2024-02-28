# Virtual Environments
[Click here for the steps to create a virtual environment.](./steps.md)

## What is a virtual environment?

A virtual environment is a directory that we create on our computers that contains some files. It consists of two main components.

1. The Python interpreter that the virtual environment runs on.
2. Any third-party libraries or packages that are installed in the virtual environment.

We will be creating one virtual environment per project going forward.

With virtual environments, we will be able to keep separate sets of dependencies from project to project. This isolation of dependencies helps to keep our project from interfering with other projects or system-wide packages.

Virtual environments are one of the most important tools that Python developers use.

## Why do we use virtual environments?
Imagine that we are developing two different projects that depend on different versions of the same package, one that uses third_party_pkg v2.2 and one that uses third_party_pkg v3.5. This would lead to compatibility issues because Python cannot simultaneously use multiple versions of the same package.

To better understand why this is so important, imagine you're working on Flask applications for two different clients.

One client is comfortable with with their existing application, which uses Flask 1.7, while client #2 wants to create a new app, which uses the latest version of Flask, version 2.3.

If you installed Flask globally, you could only have one of the two versions installed. The second version you install would overwrite the previous version.

Looks like you won’t be able to work on one of the two projects with this setup! However, if you create a virtual environment for each of your clients’ projects, then you can install a different version of Flask into each of them.

## Visualizing virtual environments
![virtual-environments](./images/virtual-environments.png)

Imagine you are a handyman or a craftsperson working on different projects. Each project requires specific tools, materials, and settings. To keep things organized and prevent conflicts, you set up separate workspaces or toolboxes for each project.

In the context of programming and virtual environments:

**Workspace:** Think of your computer's system as a large workshop where you develop software projects. The system has its default set of tools and libraries that are available globally.

**Virtual Environment:** A virtual environment is like creating a separate workspace or toolbox within the larger workshop. It provides a self-contained and isolated environment specifically tailored for a particular project.

**Tools and Dependencies:** Just like different projects may require different tools and materials, each project in programming may rely on specific versions of programming languages, libraries, and dependencies. A virtual environment allows you to install and manage these project-specific tools and dependencies without affecting the global system or other projects.

**Isolation and Compatibility:** By creating a virtual environment, you ensure that the tools, libraries, and dependencies used within that environment do not conflict with those used in other projects or the system itself. It provides a controlled and isolated space where you can work without worrying about interference from other projects.

**Portability:** Virtual environments are portable, meaning you can package and share the entire environment with others. It ensures that anyone working on the project can set up the same environment with the necessary tools and dependencies, ensuring consistency across different development environments.

Further Reading:  
[Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)